import preprocess as pre
import tensorflow as tf
import numpy as np
import math

batch_size = 10
iteration = 10

training_set_X = np.load("data/training_set_X.npy")
training_set_y = np.load("data/training_set_y.npy")
ureduce_mat = np.load("data/ureduce.npy")

hidden_neuron_cnt = 3

cv_set_X = np.load("data/cv_set_X.npy")
cv_set_y = np.load("data/cv_set_y.npy")

accu = []

with tf.Session() as sess:
    saver = tf.train.import_meta_graph("models/nn2-model-"+str(hidden_neuron_cnt)+".meta")
    saver.restore(sess, "models/nn2-model-cont-"+str(hidden_neuron_cnt))

    x_str = tf.get_collection("x_str")[0]
    y_str = tf.get_collection("y_str")[0]
    
    ureduce = tf.get_collection("ureduce")[0]

    train_step = tf.get_collection("train_step")[0]
    cross_entropy = tf.get_collection("cross_entropy")[0]
    accuracy = tf.get_collection("accuracy")[0]
    merged = tf.get_collection("merged")[0]

    cv_accuracy = accuracy.eval({x_str: cv_set_X, y_str: cv_set_y, ureduce: ureduce_mat})
    print('cv accuracy %g' % cv_accuracy)

    train_writer = tf.summary.FileWriter('train', sess.graph)
    for k in range(iteration):
        print('iter %d' % k)
        index = 0    
        for i in range(math.ceil(len(training_set_X)/batch_size)):
            batch = []
            end = min(index+batch_size, len(training_set_X))
            batch.append(training_set_X[index:end, :])
            batch.append(training_set_y[index:end])
            if i % 10 == 0:
                summary = sess.run(merged, {x_str: batch[0], y_str: batch[1], ureduce: ureduce_mat})
                train_writer.add_summary(summary, i)
            if i % 100 == 0:
                train_accuracy = accuracy.eval({x_str: batch[0], y_str: batch[1], ureduce: ureduce_mat})
                train_ce = cross_entropy.eval({x_str: batch[0], y_str: batch[1], ureduce: ureduce_mat})
                print('step %d accuracy %g loss %g\r' % (i, train_accuracy, train_ce), end='', flush=True)
            train_step.run(feed_dict={x_str: batch[0], y_str: batch[1], ureduce: ureduce_mat})
            index = index+batch_size
        print()
    train_accuracy = accuracy.eval({x_str: training_set_X, y_str: training_set_y, ureduce: ureduce_mat})
    print('training accuracy (whole set) %g' % train_accuracy)
    cv_accuracy = accuracy.eval({x_str: cv_set_X, y_str: cv_set_y, ureduce: ureduce_mat})
    # cv_auc = auc_val.eval({x_str: cv_set_X, y_str: cv_set_y, ureduce: ureduce_mat})
    # print(output.eval({x_str: cv_set_X, y_str: cv_set_y, ureduce: ureduce_mat}))
    # print("auc %g\n" % cv_auc)
    accu.append(cv_accuracy)
    # aucs.append(cv_auc)

    saver = tf.train.Saver()
    saver.save(sess, "models/nn2-model-cont"+str(hidden_neuron_cnt))
    # saver.export_meta_graph("models/nn2-model-"+str(hidden_neuron_cnt)+".meta")

print("hidden neuron", hidden_neuron_cnt)
print("accuracy", accu)
