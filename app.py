from flask import Flask, json, jsonify
import os
# import imdb_crawler
from models import IMDB_Movie

app = Flask(__name__)
app.run(debug=True)


print(os.getenv('USER_AGENT'))


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/api/movie/imdb')
def get_imdb_movies():
    return IMDB_Movie.objects().to_json()


@app.route('/api/movie/imdb/ratings')
def get_imdb_movie_ratings():

    result = IMDB_Movie.objects.aggregate([
        {
            '$project': {
                "_id": 0,
                "_cls": 0
            }
        },

        {
            '$group': {
                '_id': '$rating',
                'movies': {'$push': "$$ROOT"}
            },
        },
        {
            "$sort": { "_id": 1 }
        }
    ])

    return (jsonify(list(result)))
