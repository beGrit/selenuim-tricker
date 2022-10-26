import numpy
from tensorflow.python.keras import Sequential

from dataset_overview import load_testing_data
import tensorflow as tf

from workspace.tensorflow_mnist.dataset_overview import load_testing_data

testing_data = load_testing_data()
mnist_model: Sequential = tf.keras.models.load_model('./models/mnist_model')

tf.keras.utils.plot_model(mnist_model)
