import tensorflow as tf

#Note: Variables maintain state across executions of graph

var = tf.Variable(0, name="counter")     #create variable initialized to scalar value 0

one = tf.constant(1)
new_value = tf.add(var, one)
update = tf.assign(var, new_value)


init_op = tf.initialize_all_variables()

#Launch graph and run ops

with tf.Session() as sess:
    sess.run(init_op)             #Run the initialization operation
    print sess.run(var)           #Print the initial value of var
    for _ in range(3):
        sess.run(update)
        print sess.run(var)       #Run the op that updates var and print it
    
