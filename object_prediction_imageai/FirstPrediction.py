from imageai.Prediction import ImagePrediction
import os

execution_path = os.getcwd()

prediction = ImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath(os.path.join(execution_path, "resnet50_weights_tf_dim_ordering_tf_kernels.h5"))
prediction.loadModel()

predictions, probabilities = prediction.predictImage(os.path.join(execution_path, "1.jpg"), result_count=5)
for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction, " : ", eachProbability)

# Output

# Call initializer instance with the dtype argument instead of passing it to the constructor
# 2020-02-05 14:31:40.177327: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
# toyshop  :  40.152984857559204
# plastic_bag  :  11.917813122272491
# fountain  :  8.724948018789291
# seashore  :  7.222890108823776
# paintbrush  :  4.997722432017326
