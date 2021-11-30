import pandas as pd 
import json
import numpy as np
import joblib
import requests

# Get Data (make sure flask server is on by running CollectData.py script first)
res = requests.get('http://localhost:5000/getData')
df = pd.DataFrame(res.json()['current'])
print(df)

df['value'] = df['value'].apply(lambda x: np.array(x).flatten())
X = pd.DataFrame(df['value'].tolist(), index= df.index).to_numpy()
y = df['letter'].to_numpy()

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=101, stratify=y)
clf = RandomForestClassifier()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

joblib.dump(clf, 'model_test.joblib')