# Music_Recommendation_System

Requirements

- pip version 19 or higher
  - (Install) py -m ensurepip --upgrade
  - (Upgrade) py -m pip install --upgrade pip
- Python 3.7 - 3.10
- (Recommended) create an environment
  - py -m venv virtualenv
  - .\venv\Scripts\activate

TensorFlow

- (Package) pip install --upgrade tensorflow
- (Package) pip install tensorflow-recommenders
- (Package) pip install tensorflow-datasets
- (Package) pip install pandas
- (Package) pip install numpy

Datasets

- data_by_artists(mode,genres,acousticness,danceability,duration_ms,energy,instrumentalness,liveness,loudness,speechiness,tempo,valence,popularity,key)
- data_by_genre(mode,genres,acousticness,danceability,duration_ms,energy,instrumentalness,liveness,loudness,speechiness,tempo,valence,popularity,key)
- data_by_year(mode,year,acousticness,danceability,duration_ms,energy,instrumentalness,liveness,loudness,speechiness,tempo,valence,popularity,key)

Run Program

- py main.py

Notes

- you may get 'Could not load dynamic library ...' at runtime. You can ignore these

For more detailed information visit: https://www.tensorflow.org/install/pip#windows

References:

Example Code
https://colab.research.google.com/github/tensorflow/recommenders/blob/main/docs/examples/basic_retrieval.ipynb

https://www.tensorflow.org/recommenders/examples/quickstart

https://www.kaggle.com/code/vatsalmavani/music-recommendation-system-using-spotify-dataset/notebook

https://www.tensorflow.org/recommenders

https://analyticsindiamag.com/a-complete-guide-to-tensorflow-recommenders-with-python-code/

Alternative: https://towardsdatascience.com/how-to-build-a-simple-song-recommender-296fcbc8c85
