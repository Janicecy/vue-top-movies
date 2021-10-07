from pymongo import MongoClient
from mongoengine import connect, Document, ListField, StringField, DecimalField
import json
connect(db='top_movie', host="localhost", port=27017)


# define base Movie Schema
class Movie(Document):
    title = StringField(required=True, max_length=70)
    rating = DecimalField(precision=1)
    genres = ListField(StringField(max_length=20))
    plot = StringField()
    directors = ListField(StringField(max_length=50))
    writers = ListField(StringField(max_length=50))
    stars = ListField(StringField(max_length=50))
    poster_path = StringField()
    detail_path = StringField()

    meta = {
        'allow_inheritance': True
    }


class IMDB_Movie(Movie):
    user_review_count = StringField(max_length=10)


def get_imdb_movies():
    IMDB_Movie.objects().to_json()
