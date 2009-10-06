#!/usr/bin/env python
# $Id: $

import wsgiref.handlers
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

class MainHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write(
          template.render('templates/main.html', {}))


class NoAccessHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write(
          template.render('templates/noaccess.html', {}))


def main():
    app = webapp.WSGIApplication([
      (r'/', MainHandler),
      (r'/noaccess', NoAccessHandler),
      ], debug=False)
    wsgiref.handlers.CGIHandler().run(app)


if __name__ == '__main__':
  main()
