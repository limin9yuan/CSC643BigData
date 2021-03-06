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

"""This file includes variables for the values that configurable and changing.
Developers shall keep their own versions locally for their own development environments.
The values of the variables will be set to different values for the runtime environment.
"""

# The google project id - Place your project id here
GOOG_PROJECT_ID = r'<project id>'
# The google service credentials.
GOOG_CREDENTIALS_FILE_PATH = r'<service account secret file path>'
# The dataset name
GOOG_DATASET_NAME = r'<project data set name>'

# Query related
MAX_RESULT_COUNT = 500
# Google API timeout
GOOG_API_FETCH_TIMEOUT = 120
