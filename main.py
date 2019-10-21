import tensorflow as tf
# Simple hello world using TensorFlow
hello = tf.constant('Hello, TensorFlow!')

version = tf.__version__
# Run the op
print(version)
print(hello)
