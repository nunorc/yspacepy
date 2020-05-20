
import urllib
import urllib.request
import json

# default api base
API = 'http://api.y-space.pw/'

def _get(api, *args):
    url = api + "/".join(args)
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        planet = response.read()
    return json.loads(planet)

class Exoplanets():
    def __init__(self, api=API):
        self.api = api

    def rand(self, num):
        return _get(self.api, 'exoplanets', 'rand', num)

    def list(self):
        return _get(self.api, 'exoplanets', 'list')

    def id(self, pl_name):
        return _get(self.api, 'exoplanets', 'id', pl_name)

    def hostname(self, hs_name):
        return _get(self.api, 'exoplanets', 'hostname', hs_name)

    def stats(self):
        return _get(self.api, 'exoplanets', 'stats')

class Messier():
    def __init__(self, api=API):
        self.api = api

    def rand(self, num):
        return _get(self.api, 'messier', 'rand', num)

    def list(self):
        return _get(self.api, 'messier', 'list')

    def id(self, pl_name):
        return _get(self.api, 'messier', 'id', pl_name)

class Sunspots():
    def __init__(self, api=API):
        self.api = api

    def daily(self):
        return _get(self.api, 'sunspots', 'daily')

    def monthly(self):
        return _get(self.api, 'sunspots', 'monthly')

class ysapi():
    def __init__(self, api=API):
        self.api = api
        self.exoplanets = Exoplanets(self.api)
        self.messier = Messier(self.api)
        self.sunspots = Sunspots(self.api)
