import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import os

os.makedirs("data/train")
os.makedirs("data/test")

iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
x_train, x_test, y_train, y_test = train_test_split(df, iris.target, test_size=0.2, random_state=23)
x_train['target'] = y_train
x_test['target'] = y_test
x_train.to_csv('data/train/train.csv', index=False)
x_test.to_csv('data/test/test.csv', index=False)
