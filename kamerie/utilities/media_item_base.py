from consts import MEDIA_PATH, MEDIA_TYPE, CLEANUP_PATTERN, PUNC_TO_SPACE_PATTERN
from db import db, query_by_id, attrs_to_db_set
import re


class MediaItemBase(object):

    def __init__(self, **media_info):
        if self.dump_attributes is None:
            raise NotImplementedError("Child of MediaItem must implement dump_attributes")

        self.name = None
        self.path = media_info[MEDIA_PATH]
        self.type = media_info[MEDIA_TYPE]
        self.db_info = media_info
        self.db = db

    def save_to_db(self):
        full_attrs = self.dump_attributes()
        keys = [key for key in full_attrs.keys() if key not in [MEDIA_PATH, MEDIA_TYPE, '_id']]
        attrs = {key: full_attrs[key] for key in keys}

        self.db.Media.update_one(query_by_id(self), attrs_to_db_set(attrs))

    def trim_name(self, name):
        name = re.sub(CLEANUP_PATTERN, '', name)
        name = re.sub(PUNC_TO_SPACE_PATTERN, ' ', name)
        name = name.strip()
        return name
