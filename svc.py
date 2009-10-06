#!/usr/bin/env python
# $Id: svc.py 7 2009-09-22 14:20:21Z lkalif $

import wsgiref.handlers
import radupdater
from radupdater import Settings
from radupdater import UpdateInfo
from google.appengine.ext import webapp

class MainHandler(webapp.RequestHandler):
    def get(self):
        ret = UpdateInfo()
        self.response.headers["Content-Type"] = "text/plain"
#        self.response.headers["Content-Type"] = "application/json"
        self.response.out.write(ret.json())

def main():
    app = webapp.WSGIApplication([
      (r'/svc/get_latest', MainHandler),
      ], debug=False)
    wsgiref.handlers.CGIHandler().run(app)

if __name__ == '__main__':
  main()

