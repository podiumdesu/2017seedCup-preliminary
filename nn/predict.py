import preprocess as pre
import tensorflow as tf
import numpy as np

neuron_cnt = 4

inputs = pre.read_data("../seedCup/data/finalTestResult.csv")

ureduce_mat = np.load("data/ureduce.npy")
cv_set_X = np.load("data/cv_set_X.npy")
cv_set_y = np.load("data/cv_set_y.npy")

with tf.Session() as sess:
    saver = tf.train.import_meta_graph("models/nn-model-2.meta")
    saver.restore(sess, "models/nn-model-2")

    accuracy = tf.get_collection("accuracy")[0]


    output = tf.get_collection("output")[0]
    x_str = tf.get_collection("x_str")[0]
    ureduce = tf.get_collection("ureduce")[0]
    y_str = tf.get_collection("y_str")[0]


    prop = 1-output

    print("accuracy")
    print(accuracy.eval({x_str: cv_set_X, y_str: cv_set_y, ureduce: ureduce_mat}))
    result = sess.run(prop, {x_str: inputs, ureduce: ureduce_mat})
    # print(result)

    with open("prediction.csv", "w") as file:
        file.write("主场赢得比赛的置信度\r\n")
        for i in range(len(result)):
            file.write("%g\r\n" % result[i])
