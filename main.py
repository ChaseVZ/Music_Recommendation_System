# pip install -r requirements.txt
# python3 main.py

import pandas

data_file = 'http://millionsongdataset.com/sites/default/files/AdditionalFiles/unique_tracks.txt'

song_df_1 = pandas.read_table(data_file, delimiter='<SEP>', header = None, on_bad_lines='skip')
song_df_1.columns = ['track_id', 'song_id', 'artist_name', 'song_title']
song_df_1 = song_df_1.drop('track_id', 1)

# Link to full dataset: http://millionsongdataset.com/tasteprofile/#desc
song_df_2 = pandas.read_table('sample_triplets_data_1')
song_df_2.columns = ['user_id', 'song_id', 'listen_count']

song_df = pandas.merge(song_df_1, song_df_2, on='song_id')
print(song_df.head())


