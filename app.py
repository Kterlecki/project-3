import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config ['MONGO_DBNAME'] = 'exercise_manager'
app.config['MONGO_URI']= 'mongodb+srv://terlek:@project3-f7d5y.mongodb.net/exercise_manager?retryWrites=true&w=majority'

mongo= PyMongo(app)

@app.route('/')
@app.route('/get_exercise')
def get_exercise():
    return render_template('index.html', tasks=mongo.db.tasks.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)