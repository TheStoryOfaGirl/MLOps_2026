import pandas as pd
import pickle

data_test = pd.read_csv('data/test/preproc_test.csv')
X = data_test.drop('target', axis=1)
y = data_test['target']

pkl_filename = "knn_model.pkl" 
with open(pkl_filename, 'rb') as file: 
    pickle_model = pickle.load(file) 

score = pickle_model.score(X, y) 
print("Test score: {0:.2f} %".format(100 * score)) 
