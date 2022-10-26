import numpy
from tensorflow.python.keras import Sequential

from dataset_overview import load_testing_data
import tensorflow as tf

testing_data = load_testing_data()
mnist_model: Sequential = tf.keras.models.load_model('./models/mnist_model')

probability_mode = tf.keras.Sequential([
    mnist_model,
    tf.keras.layers.Softmax()
])
predict_data: numpy.ndarray = probability_mode.predict(testing_data)

for idx, item in enumerate(predict_data):
    result_predict = item.argmax()
    # print(f"The position {idx}: {item} \n")
    # print(f"The position {idx}: {item.sum()} \n")
    print(f"The position {idx}: {result_predict}")
