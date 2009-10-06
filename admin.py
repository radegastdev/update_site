#!/usr/bin/env python
# $Id: $

import wsgiref.handlers
import cgi
import radupdater
from radupdater import Settings
from radupdater import UpdateInfo
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.api import users

class MainHandler(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
        
        if user:
            if not users.is_current_user_admin():
                self.redirect(users.create_logout_url("/noaccess"))
                return
            
            if self.request.get("set_version") != "":
                new_version = self.request.get('new_version')
                if new_version != '':
                    settings = Settings(key_name = "current_version", value = new_version)
                    settings.put();
                    
                
                new_site = self.request.get("new_site")
                if new_site != '':
                    settings = Settings(key_name = "current_site", value = new_site)
                    settings.put();
                
                new_motd = self.request.get("new_motd")
                if new_motd != '':
                    settings = Settings(key_name = "current_motd", value = new_motd)
                    settings.put();
    
                new_display_motd = self.request.get("new_display_motd")
                settings = Settings(key_name = "current_display_motd", value = ("false", "true")[new_display_motd != ""])
                settings.put();

            info = UpdateInfo()

            self.response.out.write(
              template.render('templates/adm_main.html', {
                "version": cgi.escape(info.CurrentVersion),
                "site": cgi.escape(info.DownloadSite),
                "motd": cgi.escape(info.MOTD),
                "display_motd": ("", " checked")[info.DisplayMOTD],
                "logouturl": users.create_logout_url("/")
                }))
            return
        else:
            self.redirect(users.create_login_url(self.request.uri))
            return


def main():
    app = webapp.WSGIApplication([
      (r'/admin/', MainHandler),
      ], debug=False)
    wsgiref.handlers.CGIHandler().run(app)


if __name__ == '__main__':
  main()

