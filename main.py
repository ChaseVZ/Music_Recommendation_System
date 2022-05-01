import tensorflow as tf
 
# import tensorflow_datasets as tfds
# import tensorflow_recommenders as tfrs
tf.compat.v1.disable_eager_execution()
node1 = tf.constant(32.0)
node2 = tf.constant(32.0)
node3 = node1 + node2

# create tensorflow session object
sess = tf.compat.v1.Session()

# evaluating node3 and printing the result
print("Sum of node1 and node2 is:", sess.run(node3))

# closing the session
sess.close()
