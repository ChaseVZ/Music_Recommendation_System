import tensorflow as tf
import tensorflow_datasets as tfds
import tensorflow_recommenders as tfrs
import numpy as np
import pandas as pd
from SongModel import SongModel

# Read in datasets
artists_df = pd.read_csv('Data/data_by_artist.csv')
genres_df = pd.read_csv('Data/data_by_genres.csv')
# print(artists_df)

artists_model = tf.keras.Sequential()
genres_model = tf.keras.Sequential()
# year_model = tf.keras.Sequential()
   
# Define your objectives.
task = tfrs.tasks.Retrieval(metrics=tfrs.metrics.FactorizedTopK(
    artists_df.batch(128).map(artists_model)
  )
)

# Create a retrieval model.
model = SongModel(genres_model, artists_model, task)
model.compile(optimizer=tf.keras.optimizers.Adagrad(0.5))

# Train.
# model.fit(ratings.batch(4096), epochs=3)

# Set up retrieval using trained representations.
# index = tfrs.layers.ann.BruteForce(model.user_model)
# index.index_from_dataset(
   #  movies.batch(100).map(lambda title: (title, model.movie_model(title)))
# )

# Get recommendations.
# _, titles = index(np.array(["42"]))
# print(f"Recommendations for user 42: {titles[0, :3]}")




