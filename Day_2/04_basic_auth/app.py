import connexion

PASSWD = {"admin": "secret", "foo": "bar"}




if __name__ == "__main__":
    app = connexion.FlaskApp(__name__)
    app.add_api("openapi.yaml")
    app.run(port=8080)