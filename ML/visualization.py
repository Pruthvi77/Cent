import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import decomposition
from sklearn import datasets
iris = datasets.load_iris()
x = decomposition.PCA(n_components=3).fit_transform(iris.data)
y = iris.target
figure = plt.figure(1, figsize=(8,6))
ax = Axes3D(figure, elev=-150,azim=110)
ax.scatter(x[:,0],x[:,1],x[:,2], c=y, cmap=plt.cm.rainbow_r)
