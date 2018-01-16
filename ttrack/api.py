# Copyright (C) 2018 HiPro IT Solutions Private Limited. All
# rights reserved.
#
# This program and the accompanying materials are made available under
# the terms described in the LICENSE file which accompanies this
# distribution. If the LICENSE file was not attached to this
# distribution or for further clarifications, please contact
# legal@hipro.co.in.

import logging
log = logging.getLogger(__name__)

import colander

from cornice import Service
from cornice.validators import colander_body_validator


class LoginSchema(colander.MappingSchema):
    userid = colander.SchemaNode(colander.String())
    password = colander.SchemaNode(colander.String())

login_service = Service("login", path="/api/login", description="Login")

@login_service.post(schema=LoginSchema(),
                    validators=(colander_body_validator, ))
def post_login(request):
    userid = request.validated['userid']
    return {
        'result': 'ok',
        'token': request.create_jwt_token(userid)
    }
