import py_cdrive_api
import schema_matcher_api

def schema_matching_example():
    session = py_cdrive_api.Session(domain="dev1.columbustech.io", username="kaushik", password="kc1234")
    client = session.create_client()
    #schema_matcher = schema_matcher_api.SchemaMatcher(client)
    #
    #client.upload("/home/ubuntu/lakes/siebel", client.home)

    #app_name = client.install_app("docker.io/columbustech/sm-mapper:latest")
    #client.share(client.home + "/siebel", "E", target_type="application", target_name=app_name)
    #mapper = create_app_client(app_name)

    #app_name = client.install_app("docker.io/columbustech/blocker:latest")
    #client.share(client.home + "/siebel", "E", target_type="application", target_name=app_name)
    #blocker = create_app_client(app_name)

    #app_name = client.install_app("docker.io/columbustech/feature-vector-generator:latest")
    #client.share(client.home + "/siebel", "E", target_type="application", target_name=app_name)
    #fgen = create_app_client(app_name)

    mapper = create_app_client("sm-mapper")
    mapper.map(client.home + "/siebel/csv", client.home + "/siebel", "registry.dev1.columbstech.io/kaushik/map-final", 4)

if __name__ == "__main__":
    schema_matching_example()
