from media_item_base import MediaItemBase
from consts import YEAR_PATTERN, MEDIA_TYPE, MEDIA_PATH
from os import path
from db import FIELD_NAME, FIELD_SANITIZED_NAME, FIELD_ID, sanitize_name, ObjectId
import re


class MovieItem(MediaItemBase):

    def parse_media_info(self, **media_info):
        if self.name is None:
            basename = path.basename(self.path)

            match = re.compile(YEAR_PATTERN).search(basename)

            if match is None:
                raise AttributeError("Couldn't find movie information for %s." % basename)

            year = match.group(0)
            year_index = match.span(0)[0]

            self.name = self.trim_name(basename[0:year_index])

    def dump_attributes(self):
        return {
            MEDIA_PATH: self.path,
            MEDIA_TYPE: self.type,
            FIELD_NAME: self.name,
            FIELD_SANITIZED_NAME: sanitize_name(self.name),
            FIELD_ID: ObjectId(self.db_info['_id']['$oid'])
        }
