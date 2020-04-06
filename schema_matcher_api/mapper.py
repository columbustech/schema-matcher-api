from .application import Application
import requests, json

class Mapper(Application):
    def map(self, input_dir, output_dir, container_url, replicas):
        data = {
        "inputDir": input_dir,
        "outputDir": output_dir,
        "containerUrl": container_url,
        "replicas": replicas
        }
        response = requests.post(self.app_url + "map", data=json.dumps(data), headers={"Authorization": "Bearer " + self.token, "content-type": "application/json"})
        uid = response.json()["uid"]
        while(True):
            res = requests.get(self.app_url + "status?uid=" + uid)
            if res.json()["fnStatus"] == "complete":
                return
