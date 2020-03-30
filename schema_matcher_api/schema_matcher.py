import py_cdrive_api
import requests
from .application import Application
from .mapper import Mapper
from .blocker import Blocker
from .fgen import FeatureGenerator

class SchemaMatcher:
    def __init__(self, session, cdrive_client):
        self.cdrive_client = cdrive_client
    def create_app_client(self, app_name): 
        token = cdrive_client.app_token(app_name)
        switch(app_name) {
            case "sm-mapper":
                return Mapper(cdrive_client.domain, cdrive_client.username, app_name, token)
            case "blocker":
                return Blocker(cdrive_client.domain, cdrive_client.username, app_name, token)
            case "feature-vector-generator":
                return FeatureGenerator(cdrive_client.domain, cdrive_client.username, app_name, token)
        }
