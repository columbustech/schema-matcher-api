from .application import Application
import requests, json

class Blocker(Application):
    def block(self, a_path, n_a, b_path, n_b, container_url, replicas):
        data = {
            "aPath": a_path,
            "nA": n_a,
            "bPath": b_path,
            "nB": n_b,
            "containerUrl": container_url,
            "replicas": replicas
        }
        response = requests.post(self.app_url + "block", data=json.dumps(data), headers={"Authorization": "Bearer " + self.token, "content-type": "application/json"})
        uid = response.json()["uid"]
        while(True):
            res = requests.get(self.app_url + "status?uid=" + uid)
            if res.json()["fnStatus"] == "Complete":
                return uid
    def save(self, uid, path, name):
        data = {
            "uid": uid,
            "path": path,
            "name": name
        }
        response = requests.post(self.app_url + "save", data=json.dumps(data), headers={"Authorization": "Bearer " + self.token, "content-type": "application/json"})
