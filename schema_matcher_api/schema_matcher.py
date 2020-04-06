import py_cdrive_api
import requests
from .application import Application
from .mapper import Mapper
from .blocker import Blocker
from .featurizer import Featurizer

class SchemaMatcher:
    def __init__(self, cdrive_client):
        self.cdrive_client = cdrive_client
    def create_app_client(self, app_name): 
        token = self.cdrive_client.app_token(app_name)
        domain = self.cdrive_client.domain
        username = self.cdrive_client.username
        if app_name == "sm-mapper":
            return Mapper(domain, username, app_name, token)
        elif app_name == "blocker":
            return Blocker(domain, username, app_name, token)
        elif app_name == "featurizer":
            return Featurizer(domain, username, app_name, token)
