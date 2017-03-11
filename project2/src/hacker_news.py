#!/usr/bin/env python
#
# Copyright 2017 team1@course_bigdata, Saint Joseph's University
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""This module includes helper functions for the big queries to Hacker News.
Developers shall implement the query function here to separate such from the web controllers.
The controllers shall be implemented in other modules/classes.
"""

# built-in libs
import json
# google bigquery

# project home brews
from settings import GOOG_PROJECT_ID, GOOG_DATASET_NAME,\
    GOOG_PUBLIC_DATA_PROJ_ID, GOOG_HACKER_NEWS_SOURCE, GOOG_HACKER_NEWS_TABLE,\
    STORY_COUNT_TABLE_NAME, LOWEST_SCORE_TABLE_NAME, \
    BEST_STORY_URL_AVG_TABLE_NAME, STORY_COUNT_PER_AUTHOR
from bigquery import BigQuery


def get_story_count():
    bq = BigQuery()
    bq.get_client()
    sql = """
        SELECT COUNT(id) as storyCount
        FROM `%s.%s.%s`
        WHERE
          type = 'story'
    """ % (GOOG_PUBLIC_DATA_PROJ_ID, GOOG_HACKER_NEWS_SOURCE, GOOG_HACKER_NEWS_TABLE)
    rs, row_count = bq.async_query(sql)
    return rs
