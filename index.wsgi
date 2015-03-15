import sae
from bcrobot import wsgi

application = sae.create_wsgi_app(wsgi.application)
