from flask import Flask, request, jsonify
import pymongo
import json
import numpy as np
import joblib

app = Flask(__name__)

# Open Database
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient["test_data"]
coll = db["train_data"]

@app.route('/predictData', methods=['POST'])
def predictData():
	data = json.loads(request.data.decode('utf-8'))
	print(data)
	arr = np.array(data).flatten().reshape(-1,1).T
	print(arr)
	return jsonify({'result': str(clf.predict(arr)[0])})

if __name__ == "__main__":
	clf = joblib.load("model_test.joblib") # file won't run until you have collected and trained data first
	app.run(debug=True, host='0.0.0.0', port=5000)