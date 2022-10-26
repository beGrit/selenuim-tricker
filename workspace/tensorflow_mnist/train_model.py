import tensorflow as tf

# Load the dataset, and flatten as one-hot type.
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# Create a model.
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10)
])

# Configure the model.
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
model.compile(
    optimizer="adam",
    loss=loss_fn,
    metrics=['accuracy'],
)

# Trains the model.
model.fit(x_train, y_train, epochs=5)

# Evaluate the model.
model.evaluate(x_test, y_test, verbose=2)

# Show the model efficiency.
pass

# Persistent the model.
model.save('./models/mnist_model')
