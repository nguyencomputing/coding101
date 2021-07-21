import pandas as pd
import sklearn.neural_network
from sklearn.linear_model import LogisticRegression
from sklearn import tree
import sklearn.pipeline
import sklearn.metrics
import seaborn as sns
import matplotlib.pyplot as plt

df_xTrain = pd.read_csv("data_sneaker_vs_sandal/x_train.csv")
df_yTrain = pd.read_csv("data_sneaker_vs_sandal/y_train.csv")
df_xTest = pd.read_csv("data_sneaker_vs_sandal/x_test.csv")
df_yTest = pd.read_csv("data_sneaker_vs_sandal/y_test.csv")

xTrain = df_xTrain.to_numpy()
yTrain = df_yTrain.to_numpy()
xTest = df_xTest.to_numpy()
yTest = df_yTest.to_numpy()

logistic = LogisticRegression(verbose=1,n_jobs=1)
logistic.fit(xTrain, yTrain)
test_results_logistic = sklearn.metrics.log_loss(yTest, logistic.predict_proba(xTest))


dtree = tree.DecisionTreeClassifier()
dtree.fit(xTrain, yTrain)
test_results_dtree = sklearn.metrics.log_loss(yTest, dtree.predict_proba(xTest))

mlp = sklearn.neural_network.MLPClassifier(activation='relu', alpha=0.17152165622510307, batch_size='auto',
              beta_1=0.9, beta_2=0.999, early_stopping=False, epsilon=1e-08,
              hidden_layer_sizes=11, learning_rate='constant',
              learning_rate_init=0.001, max_iter=200,
              momentum=0.9, n_iter_no_change=10, nesterovs_momentum=True,
              power_t=0.5, random_state=202, shuffle=True, solver='adam',
              tol=0.0001, validation_fraction=0.1, verbose=True)
mlp.fit(xTrain, yTrain)
test_results_mlp = sklearn.metrics.log_loss(yTest, mlp.predict_proba(xTest))

print("Logistic Regression Results:", test_results_logistic)
print("Decision Tree Classifier Results:", test_results_dtree)
print("MLP Results:", test_results_mlp)

for classifier in [logistic,dtree,mlp]:
  predicted = classifier.predict(xTest)
  cfmt = sklearn.metrics.confusion_matrix(yTest, predicted)
  figure = plt.figure(figsize=(10, 10))
  sns.heatmap(cfmt, annot=True)
