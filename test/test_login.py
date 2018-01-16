# Copyright (C) 2018 HiPro IT Solutions Private Limited. All
# rights reserved.
#
# This program and the accompanying materials are made available under
# the terms described in the LICENSE file which accompanies this
# distribution. If the LICENSE file was not attached to this
# distribution or for further clarifications, please contact
# legal@hipro.co.in.

import json

import requests


class TestLogin(object):
    _api_url = "http://localhost:6543/api"

    def test_login(self):
        login_url = "%s/login" % (self._api_url, )
        payload = {
            'userid': "joe",
            'password': "hola",
        }
        response = requests.post(login_url, json=payload)
        r = response.json()
        print(r)
        assert r['result'] == 'ok'
