# Copyright (C) 2018 HiPro IT Solutions Private Limited. All
# rights reserved.
#
# This program and the accompanying materials are made available under
# the terms described in the LICENSE file which accompanies this
# distribution. If the LICENSE file was not attached to this
# distribution or for further clarifications, please contact
# legal@hipro.co.in.

from pyramid.config import Configurator
from pyramid.authorization import ACLAuthorizationPolicy

from . import api

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('cornice')
    config.include('pyramid_jwt')
    config.set_authorization_policy(ACLAuthorizationPolicy())
    config.set_jwt_authentication_policy('secret')
    config.scan()
    return config.make_wsgi_app()
