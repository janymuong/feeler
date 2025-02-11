#!usr/bin/python3
'''
module: sentient/keras/train.py;
    this script trains a TensorFlow model on the Sentiment140 dataset.
    moodlens; ML binary classifier model; save the model as a keras file;
'''


import os
import tensorflow as tf
import pandas as pd

from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint


# load and preprocess the Sentiment140 dataset
def load_dataset():
    dataset_path = './data/training_cleaned.csv'
    df = pd.read_csv(dataset_path, encoding='utf-8', header=None)

    # create custom column headers: eg 'text' represents a tweet
    df.columns = ['polarity', 'id', 'date', 'query', 'user', 'text']

    # convert polarity 4 (positive) to 1, and 0 (negative) remains as 0
    # values are from the dataset column on sentiment (equivalenbtly replace w/ the 'polarity' dataframe column)
    df['polarity'] = df['polarity'].replace(4, 1)

    texts = df['text'].values
    labels = df['polarity'].values
    return texts, labels


# model architecture with TextVectorization layer and embedding
def build_model():
    # define vectorizer - this convert words into numbers the model can easily process
    vectorizer = tf.keras.layers.TextVectorization(
        max_tokens=10000,  # max number of tokens to include - word segments from bag of words
        output_mode='int',
        output_sequence_length=100  # fixed length for sequences; should match input layer shape
    )

    # define the model architecture
    model = tf.keras.Sequential([
        vectorizer,  # TextVectorization layer
        tf.keras.layers.Embedding(input_dim=10000, output_dim=128),  # embedding layer
        tf.keras.layers.Conv1D(128, 5, activation='relu'),  # convolutional layer
        tf.keras.layers.GlobalMaxPooling1D(),  # global max pooling
        tf.keras.layers.Dense(64, activation='relu'),  # fully connected layer(hideen layer)
        tf.keras.layers.Dropout(0.4),  # regularization/dropout to prevent overfitting
        tf.keras.layers.Dense(1, activation='sigmoid')  # 1-neuron output layer; binary classifier
    ])

    # compile the model
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    return model, vectorizer


# train and save the model with callbacks for early stopping and checkpointing
def train_and_save_model():
    # load the sentiment140 dataset
    texts, labels = load_dataset()

    # build the model and vectorizer
    model, vectorizer = build_model()

    # adapt the vectorizer on the input texts
    vectorizer.adapt(texts)

    # callbacks to prevent overfitting and save the best model
    early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
    model_checkpoint = ModelCheckpoint(
        filepath='keras/sentient73.keras',
        save_best_only=True,
        monitor='val_loss',
        mode='min'
    )

    # train the model
    model.fit(
        texts, labels,
        epochs=20,
        batch_size=64,  # training batch size
        validation_split=0.2,  # 20% of the data for validation
        callbacks=[early_stopping, model_checkpoint]
    )

    # save the model as .keras f0r inference
    model_path = 'keras/sentient73.keras'
    model.save(model_path)
    print(f'Model saved to {model_path}')

    # save the vocabulary to a file
    vocab_path = 'keras/vectorizer_vocab.txt'
    with open(vocab_path, 'w', encoding='utf-8') as f:
        for word in vectorizer.get_vocabulary():
            f.write(word + '\n')

if __name__ == '__main__':
    train_and_save_model()
