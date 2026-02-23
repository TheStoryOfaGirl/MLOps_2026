from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import pickle

data_train = pd.read_csv('data/train/preproc_train.csv')
X = data_train.drop('target', axis=1)
y = data_train['target']

knn_model = KNeighborsClassifier(n_neighbors=3)
knn_model.fit(X, y)

pkl_filename = "knn_model.pkl" 
with open(pkl_filename, 'wb') as file: 
    pickle.dump(knn_model, file) 