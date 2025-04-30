from flask import Flask, request, jsonify
from model import predict_skin_disease
from gpt_helper import ask_gpt

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'ارفع صورة'}), 400

    image_file = request.files['image']
    disease = predict_skin_disease(image_file)

    prompt = f"اشرح لي مرض {disease} بشكل بسيط، وهل يحتاج زيارة طبيب؟ مع نصيحة مفيدة."
    explanation = ask_gpt(prompt)

    return jsonify({
        'disease': disease,
        'explanation': explanation
    })

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    if 'message' not in data:
        return jsonify({'error': 'ارسل رسالة'}), 400

    reply = ask_gpt(data['message'])
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)
