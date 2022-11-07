import numpy
import tensorflow as tf
import matplotlib.pyplot as plt


def load_testing_data() -> numpy.ndarray:
    mnist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    # Load 4th record to plot.
    result: numpy.ndarray = x_test[:4][:28][:28]
    result = result / 255
    return result


if __name__ == '__main__':
    x_show = load_testing_data()

    # Plot it.
    figure, panels = plt.subplots(x_show.shape[0])
    for idx, item in enumerate(x_show):
        panels[idx].imshow(item, cmap='Greys')

    plt.show()
