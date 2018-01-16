from pyramid.config import Configurator

from . import api

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('cornice')
    config.scan()
    return config.make_wsgi_app()
