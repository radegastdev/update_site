#!/usr/bin/env python
# $Id: radupdater.py 7 2009-09-22 14:20:21Z lkalif $

from google.appengine.ext import db
from django.utils import simplejson
from django.core import serializers

class Settings(db.Model):
    value = db.StringProperty(required = True,  multiline=True)

class Serializable:
    def get_dict(self):
        return dict((key, value) for key, value in self.__dict__.iteritems() 
            if not callable(value) and not key.startswith('__'))
        
    def json(self):
        return simplejson.dumps(self.get_dict(), sort_keys=True, indent=4)
    
class UpdateInfo(Serializable):
    def __init__(self):
        self.Error = False
        self.ErrMessage = ''
        self.CurrentVersion = ''
        self.DownloadSite = ''
        self.MOTD = ''
        self.DisplayMOTD = False
        
        setting = Settings.get_by_key_name("current_version")
        if setting is None:
            self.ErrMessage = "Failed fetching data"
            self.Error = True;
        else:
            self.CurrentVersion = setting.value
            
        setting = Settings.get_by_key_name("current_site")
        if setting is None:
            self.ErrMessage = "Failed fetching data"
            self.Error = True;
        else:
            self.DownloadSite = setting.value
            
        setting = Settings.get_by_key_name("current_motd")
        if setting is None:
            self.ErrMessage = "Failed fetching data"
            self.Error = True;
        else:
            self.MOTD = setting.value
            

        setting = Settings.get_by_key_name("current_display_motd")
        if setting is None:
            self.ErrMessage = "Failed fetching data"
            self.Error = True;
        else:
            self.DisplayMOTD = setting.value == "true"
