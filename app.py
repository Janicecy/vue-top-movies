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


# group by ratings
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
                'count': {"$sum": 1 }
            },
        },
        {
            "$sort": { "_id": 1 }
        }
    ])

    return (jsonify(list(result)))

# group by genres
@app.route('/api/movie/imdb/genres')
def get_imdb_movie_by_genres():

    result = IMDB_Movie.objects.aggregate([
        {
            '$project': {
                "_id": 0,
                "_cls": 0
            }
        },
        {
            "$unwind": '$genres'
        },

        {
            '$group': {
                '_id': '$genres',
                'value': {"$sum": 1 }
            },
        },
        {
            "$addFields": {
                "name": "$_id"
            }
        },
        {
            "$sort": { "value": -1 }
        }
    ])

    return (jsonify(list(result)))
