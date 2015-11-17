import tensorflow as tf

NUM_CORES = 4


# a) Construction phase: Building a graph

matrix1 = tf.constant([[3., 3.]])      #op returns 1x2 matrix 
matrix2 = tf.constant([[2.], [2.]])    #op returns 2x1 matrix
product = tf.matmul(matrix1,matrix2)   #op returns matrix multiplication


# b) Execusion phase: Launching the graph in a session


sess = tf.Session()                    #Launch the default graph
result = sess.run(product)
print result

# c) Close Session to release resources
sess.close()


'''
Or combine b and c:

with tf.Session() as sess:
    result = sess.run([product[)
    print result


'''


