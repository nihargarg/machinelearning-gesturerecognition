from flask import Flask, request, jsonify
import pymongo
import json
import numpy as np
import joblib

app = Flask(__name__)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient["test_data"]
coll = db["train_data"]

@app.route('/getData', methods=['GET'])
def getData():
	response_json = {'current': list(db.train_data.find({}, {"_id":0}))}
	return jsonify(response_json)

@app.route('/collectData', methods=['POST'])
def collectData():
	data_to_save = {}
	data_to_save['value'] = json.loads(request.data.decode('utf-8'))
	data_to_save['letter'] = 'M' # 'C', 'O', 'L', 'U', 'M', 'B', 'I', 'A'
	data_to_save_id = coll.insert_one(data_to_save).inserted_id
	return jsonify({'200': 'OK'})

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=5000)