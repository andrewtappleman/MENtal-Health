from flask import Flask, render_template, request, jsonify
from flask_pymongo import PyMongo
from bson import ObjectId
from pymongo.mongo_client import MongoClient

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('food.html')

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
    collection = db['Food']


    data = request.json
    name = data.get('name')
    food = data.get('food')
    after = data.get('after')

    food = [{"food": food, "after": after, "name": name}]
    result = collection.insert_many(food)

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
    collection = db['Food']

    print('data request name')

    data = request.json
    nameFull = data.get('name')

    print('name: '+ nameFull)

    foodList1 = []
    foodList2 = []
    foodList3 = []
    
    foods = collection.find({'name': nameFull})
    for food in foods:
        if int(food['after']) < 2:
            foodList3.append({'food': food['food']})
        elif int(food['after']) > 1 and int(food['after']) < 4:
            foodList2.append({'food': food['food']})
        elif int(food['after']) > 3:
            foodList1.append({'food': food['food']})
    print('Unique')
    print(foodList1)
    print('')
    print(foodList2)
    print('')
    print(foodList3)
    return jsonify({
        "food7U": foodList1,
        "food47": foodList2,
        "foodU4": foodList3
    })
if __name__ == '__main__':
    app.run(port=5001)
