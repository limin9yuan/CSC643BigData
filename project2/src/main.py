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

__doc__ = """Main entrance of this web app which plays as an 'index.html'
like in good old days.
"""

import os

import webapp2
from google.appengine.ext.webapp import template

from urls import ROUTES


class MainHandler(webapp2.RequestHandler):
    def get(self):
        # self.response.write('Hello world!')
        objects = os.listdir(os.curdir)
        temp_vals = {
            'headline': 'Objects under the Current Folder',
            'objects': objects
        }
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(template.render(path, temp_vals))


app = webapp2.WSGIApplication(ROUTES, debug=True)


def main():
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port='8080')


# sanity test
if __name__ == '__main__':
    main()