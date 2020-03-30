class Application:
    def __init__(self, domain, username, app_name, token):
        self.domain = domain
        self.username = username
        self.app_name = app_name
        self.token = token
        self.app_url = "https://" + self.domain + "/app/" + username + "/" + app_name + "/api/"
