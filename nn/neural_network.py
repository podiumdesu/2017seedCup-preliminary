import tensorflow as tf
import numpy as np
import math


def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)

def bias_variable(shape):
    initial = tf.constant(0., shape=shape)
    return tf.Variable(initial)


hidden_neuron_cnts = [2]
batch_size = 10
iteration = 30
features = 207

accu = []
# aucs = []

training_set_X = np.load("data/training_set_X.npy")
training_set_y = np.load("data/training_set_y.npy")
ureduce_mat = np.load("data/ureduce.npy")

cv_set_X = np.load("data/cv_set_X.npy")
cv_set_y = np.load("data/cv_set_y.npy")

def variable_summaries(var):
    with tf.name_scope("summaries"):
        mean = tf.reduce_mean(var)
        tf.summary.scalar("mean", mean)
        with tf.name_scope("stddev"):
            stddev = tf.sqrt(tf.reduce_mean(tf.square(var-mean)))
        tf.summary.scalar("stddev", stddev)
        tf.summary.scalar("max", tf.reduce_max(var))
        tf.summary.scalar("min", tf.reduce_min(var))
        tf.summary.histogram("histogram", var)

for hidden_neuron_cnt in hidden_neuron_cnts:
    with tf.Session() as sess:
        x_str = tf.placeholder(tf.string, shape=[None, 544])
        tf.add_to_collection("x_str", x_str)

        x = tf.string_to_number(x_str, tf.float32)
        ureduce = tf.placeholder(tf.float32, shape=[544, features])
        tf.add_to_collection("ureduce", ureduce)
        z = tf.matmul(x, ureduce)

        y_str = tf.placeholder(tf.string, shape=[None, 1])
        tf.add_to_collection("y_str", y_str)
        y_ = tf.string_to_number(y_str, tf.float32)

        W_input = weight_variable([features,hidden_neuron_cnt])
        b_input = bias_variable([hidden_neuron_cnt])

        variable_summaries(W_input)
        variable_summaries(b_input)

        hidden_preactivation = tf.matmul(z,W_input) + b_input
        hidden = tf.nn.sigmoid(hidden_preactivation)

        tf.summary.histogram("hidden_preactivation", hidden_preactivation)
        tf.summary.histogram("hidden", hidden)

        W_hidden = weight_variable([hidden_neuron_cnt, 1])
        b_hidden = bias_variable([1])

        variable_summaries(W_hidden)
        variable_summaries(b_hidden)

        output_raw = tf.matmul(hidden,W_hidden) + b_hidden
        output = tf.nn.sigmoid(output_raw)
        tf.add_to_collection("output", output)

        tf.summary.histogram("output_raw", output_raw)
        tf.summary.histogram("output", output)

        cross_entropy = tf.reduce_mean(
            tf.nn.sigmoid_cross_entropy_with_logits(labels=y_, logits=output_raw)
        )
        tf.summary.scalar('cross_entropy', cross_entropy)

        tf.add_to_collection("cross_entropy", cross_entropy)

        train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
        tf.add_to_collection("train_step", train_step)
        correct_predict = tf.equal(y_, tf.to_float(tf.greater(output_raw, 0.)))
        accuracy = tf.reduce_mean(tf.cast(correct_predict, tf.float32))
        tf.add_to_collection("accuracy", accuracy)
        tf.summary.scalar('accuracy', accuracy)
        # auc_val, _ = tf.metrics.auc(y_, output)

        merged = tf.summary.merge_all()
        tf.add_to_collection("merged", merged)

        sess.run(tf.global_variables_initializer())
        sess.run(tf.local_variables_initializer())
        train_writer = tf.summary.FileWriter('train', sess.graph)
        for k in range(iteration):
            print('iter %d' % k)
            index = 0    
            for i in range(math.ceil(len(training_set_X)/batch_size)):
                batch = []
                end = min(index+batch_size, len(training_set_X))
                batch.append(training_set_X[index:end, :])
                batch.append(training_set_y[index:end])
                if i % 10:
                    summary = sess.run(merged, {x_str: batch[0], y_str: batch[1], ureduce: ureduce_mat})
                    train_writer.add_summary(summary, i+k*math.floor(len(training_set_X)/10))
                if i % 100 == 0:
                    train_accuracy = accuracy.eval({x_str: batch[0], y_str: batch[1], ureduce: ureduce_mat})
                    train_ce = cross_entropy.eval({x_str: batch[0], y_str: batch[1], ureduce: ureduce_mat})
                    print('step %d, training accuracy %g\tloss %g\r' % (i, train_accuracy, train_ce), end='', flush=True)
                train_step.run(feed_dict={x_str: batch[0], y_str: batch[1], ureduce: ureduce_mat})
                index = index+batch_size
            print()

        train_writer.close()

        cv_accuracy = accuracy.eval({x_str: cv_set_X, y_str: cv_set_y, ureduce: ureduce_mat})
        # cv_auc = auc_val.eval({x_str: cv_set_X, y_str: cv_set_y, ureduce: ureduce_mat})
        print(output.eval({x_str: cv_set_X, y_str: cv_set_y, ureduce: ureduce_mat}))
        print("hidden neuron %d  cross validation accuracy %g" % (hidden_neuron_cnt, cv_accuracy))
        # print("auc %g\n" % cv_auc)
        accu.append(cv_accuracy)
        # aucs.append(cv_auc)

        saver = tf.train.Saver()
        saver.save(sess, "models/nn2-model-"+str(hidden_neuron_cnt))
        saver.export_meta_graph("models/nn2-model-"+str(hidden_neuron_cnt)+".meta")

print("accuracy", accu)
# print("auc", aucs)
