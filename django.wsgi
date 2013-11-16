import os,sys
sys.path.append("/python/webshow") 
os.environ['DJANGO_SETTINGS_MODULE'] = 'webshow.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
