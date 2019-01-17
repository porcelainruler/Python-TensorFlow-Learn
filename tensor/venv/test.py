import tensorflow as tf;
import bs4 as bs4;

node1 = tf.constant(3.0, tf.float32);
node2 = tf.constant(4.0);

c = node1*node2;

sess = tf.Session ();

File_writer = tf.summary.FileWriter('/home/shubham/PycharmProjects/tensor/venv/graph', sess.graph);

print(sess.run(c));

#print(node1, node2);