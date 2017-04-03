import pandas
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn import preprocessing
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
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from progressbar import ProgressBar
pbar = ProgressBar()

ff = open('../datasets/ML/cellphones_kmeans_label.csv','w+')
path = '../datasets/ML/cellphones.csv'
cols = pandas.read_csv(path, nrows=1).columns
dataset = pandas.read_csv(path,usecols=cols[1:])
reviewers = pandas.read_csv(path,usecols=cols[0:1]).values
data_clean = dataset.dropna()
cluster=data_clean[['negative','neutral','positive','helpfulness','burst','count']]

# Split-out validation dataset
#clustervar = dataset.values.copy()
#clustervar[1] = preprocessing.scale(clustervar[1].astype('float64'))
clustervar=cluster.copy()
clustervar['negative']=preprocessing.scale(clustervar['negative'].astype('float64'))
clustervar['neutral']=preprocessing.scale(clustervar['neutral'].astype('float64'))
clustervar['positive']=preprocessing.scale(clustervar['positive'].astype('float64'))
clustervar['count']=preprocessing.scale(clustervar['count'].astype('float64'))
#print clustervar
'''clus_train = clustervar

from scipy.spatial.distance import cdist
clusters=range(1,11)
meandist=[]

# loop through each cluster and fit the model to the train set
# generate the predicted cluster assingment and append the mean distance my taking the sum divided by the shape
for k in clusters:
    model=KMeans(n_clusters=k)
    model.fit(clus_train)
    clusassign=model.predict(clus_train)
    meandist.append(sum(np.min(cdist(clus_train, model.cluster_centers_, 'euclidean'), axis=1))
    / clus_train.shape[0])

"""
Plot average distance from observations from the cluster centroid
to use the Elbow Method to identify number of clusters to choose
"""
plt.plot(clusters, meandist)
plt.xlabel('Number of clusters')
plt.ylabel('Average distance')
plt.title('Selecting k with the Elbow Method') # pick the fewest number of clusters that reduces the average distance

plt.show()'''
pca = PCA(n_components=2).fit(clustervar)
pca_2d = pca.transform(clustervar)
X = pca_2d 
kmeans = KMeans(n_clusters=5)
kmeans.fit(X)
centroids = kmeans.cluster_centers_
labels = kmeans.labels_

colors = ["g.","r.","y.","b.","black"]

for i in pbar(range(len(X))):
    #print("coordinate:",X[i],reviewers[i], "label:", labels[i])
    ff.write(reviewers[i][0]+','+str(dataset.values[i][0])+","+str(dataset.values[i][1])+","+str(dataset.values[i][2])+","+str(dataset.values[i][3])+","+str(dataset.values[i][4])+","+str(dataset.values[i][5])+","+str(labels[i]))
    ff.write("\n")
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize = 10)


plt.scatter(centroids[:, 0],centroids[:, 1], marker = "x", s=150, linewidths = 5, zorder = 10)


plt.show()
