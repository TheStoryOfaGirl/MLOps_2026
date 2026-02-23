from sklearn.preprocessing import StandardScaler
import pandas as pd

data_train = pd.read_csv('data/train/train.csv')
data_test = pd.read_csv('data/test/test.csv')

x_train = data_train.drop('target', axis=1)
x_test = data_test.drop('target', axis=1)

scaler = StandardScaler()
scaled_x_train = pd.DataFrame(
    scaler.fit_transform(x_train),
    columns=x_train.columns
)
scaled_x_test = pd.DataFrame(
    scaler.fit_transform(x_test),
    columns=x_test.columns
)

scaled_x_train['target'] = data_train['target']
scaled_x_test['target'] = data_test['target']

scaled_x_train.to_csv('data/train/preproc_train.csv', index=False)
scaled_x_test.to_csv('data/test/preproc_test.csv', index=False)