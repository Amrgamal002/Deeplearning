import openai
openai.api_key = "YOUR_API_KEY"  # حط مفتاح OpenAI هنا

def ask_gpt(message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": message}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"خطأ: {str(e)}"
