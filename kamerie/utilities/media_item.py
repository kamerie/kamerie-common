from consts import MEDIA_TYPE, TYPE_SERIES, TYPE_MOVIE
from db import db, ObjectId, query_by_id, attrs_to_db_set, sanitize_name, \
    FIELD_ID, FIELD_NAME, FIELD_SEASON, FIELD_EPISODE, \
    FIELD_SANITIZED_NAME
from series_item import SeriesItem
from movie_item import MovieItem
from os import path
import re

ITEM_TYPES = {
    TYPE_SERIES: SeriesItem,
    TYPE_MOVIE: MovieItem,
}


class MediaItem(object):

    def __init__(self, **media_info):
        if media_info[MEDIA_TYPE] not in ITEM_TYPES:
            raise InputError("item.type must be one of: %s" % ITEM_TYPES.keys())

    def __new__(self, **media_info):
        klass = ITEM_TYPES[media_info[MEDIA_TYPE]]
        self.instance = klass(**media_info)
        self.instance.parse_media_info(**media_info)
        self.instance.save_to_db()
        return self.instance
