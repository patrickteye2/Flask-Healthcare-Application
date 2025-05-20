from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
import os

app = Flask(__name__)
uri = "mongodb+srv://razbinokelly01:DO9SznxYxfzr22uc@cluster0.pkxj0ek.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# MongoDB connection
client = MongoClient(uri)
db = client['healthcare_survey']
collection = db['user_data']

@app.route('/')
def index():
    # accept messages for feedback
    message = request.args.get('message')
    return render_template('index.html', message=message)

@app.route('/submit', methods=['POST'])
def submit():
    # get and clean form input
    age_input = request.form.get('age', '').strip()
    gender = request.form.get('gender', '').strip()
    income_input = request.form.get('income', '').strip()

    # safely deal with input
    try:
        age = int(age_input)
    except (ValueError, TypeError):
        return render_template('index.html', message='Invalid age. Please enter a valid number')

        
    try:
        income = float(income_input)
    except (ValueError, TypeError):
        return render_template('index.html', message='Invalid income. Please enter a valid number')


    expenses = {}
    categories = ['utilities', 'entertainment', 'school_fees', 'shopping', 'healthcare']
    for category in categories:
        if request.form.get(f'{category}_check'):
            amount = request.form.get(f'{category}_amount', '0').strip()
            try:
                expenses[category] = float(amount) 
            except (ValueError, TypeError):
                expenses[category] = 0.0

    # check if all required fields are filled
    user_data = {
        'age' : int(age),
        'gender' : gender,
        'income' : float(income),
        'expenses': expenses
    }

    collection.insert_one(user_data)
    #return redirect('/')
    return redirect('/?message=Data submitted successfully!')

if __name__ == '__main__':
    app.run(debug=True)