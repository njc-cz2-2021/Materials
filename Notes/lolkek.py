import pandas as pd
pd.set_option('display.max_columns',6)

from sklearn.decomposition import PCA
import seaborn
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 

h = pd.read_csv('./resources/pointcloud.csv')
h = pd.DataFrame(h, columns='x y z'.split())
h = h.sample(1000).copy()
print(h)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(h.x, h.y, h.z, c='b', zdir='z', depthshade=True)
plt.show()
