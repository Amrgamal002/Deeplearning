import tensorflow
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

model = load_model(r'C:\Users\Amr\Documents\grad_project\skin_disease_model.h5')
class_names = ['BA- cellulitis', 'BA-impetigo', 'FU-athlete-foot', 'FU-nail-fungus','FU-ringworm','PA-cutaneous-larva-migrans','VI-chickenpox','VI-shingles']  # غيّر حسب التصنيفات بتاعتك

def predict_skin_disease(img_file):
    img_path = "temp.jpg"
    img_file.save(img_path)

    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    predicted_class = class_names[np.argmax(prediction)]

    os.remove(img_path)

    return predicted_class
