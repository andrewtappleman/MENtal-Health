from flask import Flask, render_template, request, jsonify
from flask_pymongo import PyMongo
from bson import ObjectId
from pymongo.mongo_client import MongoClient

app = Flask(__name__)

#pp.config["MONGO_URI"] = "mongodb+srv://andrewtappleman:Luna0727!@mentalhealth.w4mgf.mongodb.net/?retryWrites=true&w=majority&appName=MENtalHealth"

#mongo = PyMongo(app)
#db = mongo.db["Exercise"]

@app.route('/')
def home():
    return render_template('exercise.html')

@app.route('/main')
def home_page():
    return render_template('main.html')

@app.route('/calorie')
def calorie():
    return render_template('calorie.html')

@app.route('/goal')
def goal():
    return render_template('goal.html')

@app.route('/add_info', methods=['POST'])
def add_info():
    uri = "mongodb+srv://andrewtappleman:Luna0727!@mentalhealth.w4mgf.mongodb.net/?retryWrites=true&w=majority&appName=MENtalHealth"
    client = MongoClient(uri)

    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    db = client['MENtalHealth']
    collection = db['Exercise']


    data = request.json
    name = data.get('name')
    date = data.get('date')
    type = data.get('type')
    intensity = data.get('intensity')
    after = data.get('after')

    exercise = [{"date": date, "type": type, "intensity": intensity, "after": after, "name": name}]
    result = collection.insert_many(exercise)

    return result

@app.route('/fetch_data', methods=['POST'])
def fetch_data():
    uri = "mongodb+srv://andrewtappleman:Luna0727!@mentalhealth.w4mgf.mongodb.net/?retryWrites=true&w=majority&appName=MENtalHealth"
    client = MongoClient(uri)

    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    db = client['MENtalHealth']
    collection = db['Exercise']

    print('data request name')

    data = request.json
    nameFull = data.get('name')

    print('name: '+ nameFull)

    exerList = []
    
    exercises = collection.find({'name': nameFull})
    for exercise in exercises:
        exerList.append({'type': exercise['type'], 'after': exercise['after']})

    return jsonify({
        "exercises": exerList
    })
if __name__ == '__main__':
    app.run()
