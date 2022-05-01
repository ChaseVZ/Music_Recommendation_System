from typing import Dict, Text

import numpy as np
import tensorflow as tf

import tensorflow_datasets as tfds
import tensorflow_recommenders as tfrs


class SongModel(tfrs.Model):
   def __init__(
      self,
      user_model: tf.keras.Model,
      song_model: tf.keras.Model,
      task: tfrs.tasks.Retrieval):
      super().__init__()

      # Set up user and song representations.
      self.user_model = user_model
      self.movie_model = song_model

       # Set up a retrieval task.
      self.task = task

   def compute_loss():
      pass