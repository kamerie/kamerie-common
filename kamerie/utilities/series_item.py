from media_item_base import MediaItemBase
from db import query_by_id, attrs_to_db_set, sanitize_name, ObjectId
from os import path
from consts import SEASON_EP_PATTERN, MEDIA_TYPE, MEDIA_PATH
from db import FIELD_NAME, FIELD_SANITIZED_NAME, FIELD_SEASON, FIELD_EPISODE, FIELD_ID
import re


class SeriesItem(MediaItemBase):

    def parse_media_info(self, **media_info):
        if self.name is None or self.episode is None or self.season is None:
            basename = path.basename(self.path)

            matches = re.compile(SEASON_EP_PATTERN, re.IGNORECASE).search(basename)

            if matches is None:
                raise AttributeError("Couldn't find series information for %s." %
                                     path.join(path.basename(path.dirname(self.path)), basename))

            self.season = int(matches.group(1))
            self.episode = int(matches.group(2))

            ep_index = basename.index(matches.group(0))

            if (ep_index > 0):
                self.name = self.trim_name(basename[0:ep_index])
            else:
                name = path.basename(path.dirname(self.path))

                if "season" in name.lower():
                    idx = name.lower().index("season")
                    if idx > 0:
                        self.name = self.trim_name(name[0:idx])
                    else:
                        self.name = self.trim_name(path.dirname(name))
                else:
                    self.name = self.trim_name(path.basename(path.dirname(path.dirname(self.path))))

    def dump_attributes(self):
        return {
            MEDIA_PATH: self.path,
            MEDIA_TYPE: self.type,
            FIELD_NAME: self.name,
            FIELD_SANITIZED_NAME: sanitize_name(self.name),
            FIELD_SEASON: self.season,
            FIELD_EPISODE: self.episode,
            FIELD_ID: ObjectId(self.db_info['_id']['$oid'])
        }
