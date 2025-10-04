import pandas as pd
from aggregator import *

DEFAULT_RANK_SIZE = 10

RankedList = list[str]

"""
Prints a list with your top songs in a given year.
"""
def print_top_songs(
    data : pd.DataFrame,
    year : int, 
    list_size=DEFAULT_RANK_SIZE
    ) -> None:

  whole_year = data[data[TS_COL_NAME].dt.year == year]
  whole_year = whole_year.assign(
    song=whole_year[TRACK_COL_NAME] 
       + " — " 
       + whole_year[ARTIST_COL_NAME]
  )
  top = whole_year.value_counts("song")

  for pos, song in enumerate(top.head(list_size).keys()):
    print(str(pos + 1) + ". " + song)

