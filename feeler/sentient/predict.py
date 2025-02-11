# sentient/predict.py
import tensorflow as tf
import os

# load the model w/ weights
model_path = os.path.join(os.path.dirname(__file__), 'keras', 'sentient73.keras')
model = tf.keras.models.load_model(model_path)

# recreate the vectorizer and load the vocabulary
vectorizer = tf.keras.layers.TextVectorization(
    max_tokens=10000,
    output_mode='int',
    output_sequence_length=100
)

# load the vocabulary from the saved file
vocab_path = os.path.join(os.path.dirname(__file__), 'keras', 'vectorizer_vocab.txt')
with open(vocab_path, 'r', encoding='utf-8') as f:
    vocab = [line.strip() for line in f]
vectorizer.set_vocabulary(vocab)


def predict_emotion(text):
    '''this function defines the logic for making a prediction against the model
    '''
    # vectorize the input text
    input_data = vectorizer([text])

    # make a prediction
    prediction = model.predict(input_data)[0][0]
    sentiment = 'positive' if prediction >= 0.5 else 'negative'
    return sentiment, float(prediction)
