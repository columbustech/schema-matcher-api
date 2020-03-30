from .application import Application
import requests

class Mapper(Application):
    def map(input_dir, output_dir, container_url, replicas):
        data = {
        "inputDir": input_dir,
        "outputDir": output_dir,
        "containerUrl": container_url,
        "replicas": replicas
        }
        response = requests.post(self.app_url + "map", data=data, headers={"Authorization": "Bearer " + self.token
        uid = response.json()["uid"]
        while(True):
            res = requests.get(self.app_url + "status?uid=" + uid)
            if res.json()["fnStatus"] == "Complete":
                return
