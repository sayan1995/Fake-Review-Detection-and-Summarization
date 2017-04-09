# Load libraries
import pandas
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
import numpy as np
import pickle

path = '../../datasets/ML/cellphones_label.csv'
cols = pandas.read_csv(path, nrows=1).columns
X = pandas.read_csv(path,usecols=cols[1:len(cols)-1])
Y = np.array(pandas.read_csv(path,usecols=cols[len(cols)-1:])).ravel()
newpath = '../../datasets/ML/musical_label.csv'
cols = pandas.read_csv(newpath, nrows=1).columns
X_test = pandas.read_csv(newpath,usecols=cols[1:])
scoring = 'accuracy'
X_train, X_validation, Y_train = X, X_test, Y 
seed = 7
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))
# evaluate each model in turn
results = []
names = []
'''for name, model in models:
	kfold = model_selection.KFold(n_splits=10, random_state=seed)
	cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
	results.append(cv_results)
	names.append(name)
	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	print(msg)'''

# Make predictions on validation dataset
knn = KNeighborsClassifier()
knn.fit(X_train, Y_train)
#pickle.dump( knn, open( "save.p", "wb" ) )
predictions = knn.predict(X_validation)
for i in predictions:
	print i
'''print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))'''

