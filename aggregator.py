import typing

import os
import json

import pandas as pd

DATA_DIRECTORY_NAME = "json_data/"
JSON_EXTENSION = ".json"

TS_COL_NAME = "ts"
STREAM_TIME_COL_NAME = "ms_played"
TRACK_COL_NAME = "master_metadata_track_name"
ARTIST_COL_NAME = "master_metadata_album_artist_name"
COUNTRY_COL_NAME = "conn_country"

RELEVANT_COLS = [
  TS_COL_NAME,
  COUNTRY_COL_NAME,
  TRACK_COL_NAME,
  ARTIST_COL_NAME
  ]

# Type aliases for JSON manipulation
StreamValue = typing.Union[str, int, bool, None]
Stream = dict[str, StreamValue]

"""
Assuming the given file contains a valid JSON
array of JSON objects representing streams, appends them
to the provided list of 'Stream' objects.
"""
def load_file(filename : str, strms : list[Stream]) -> None:
  with open(filename, 'r') as file:
    strms += json.load(file)


"""
Takes all the files in DATA_DIRECTORY_NAME ending in
JSON_EXTENSION and aggregates them into a list of
Stream objects.
"""
def aggregate_list() -> list[Stream]:
  strms : list[Stream] = []
  for filename in os.listdir(DATA_DIRECTORY_NAME):
    if filename.endswith(JSON_EXTENSION):
      load_file(DATA_DIRECTORY_NAME + filename, strms)

  return strms

"""
Takes all valid JSON files in DATA_DIRECTORY_NAME and creates
a pandas DataFrame compiling their information; now sorted by
streaming time, from earliest to latest; and only considering
the RELEVANT_COLS columns.
"""
def organize_data() -> pd.DataFrame:

  data = pd.DataFrame(aggregate_list())
  data[TS_COL_NAME] = pd.to_datetime(data[TS_COL_NAME])
  data = data.sort_values(by=TS_COL_NAME)
  data = data[RELEVANT_COLS]

  return data

"""
Filter the data by artist.
"""
def filter_by_artist(data : pd.DataFrame, artist : str) -> pd.DataFrame:
  return data[data[ARTIST_COL_NAME] == artist]