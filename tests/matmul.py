import tensorflow as tf
import time

a = tf.random_normal((100,128000))
b = tf.random_normal((128000,100))
c = tf.matmul(a,b)

sess = tf.Session()

start_time = time.time()
sess.run(c)
end_time = time.time() - start_time

print(end_time)
