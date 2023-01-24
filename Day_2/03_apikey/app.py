import connexion
from connexion.exceptions import OAuthProblem

TOKEN = {"xyv123456": {"uid": 100}}




if __name__ == "__main__":
    app = connexion.FlaskApp(__name__)
    app.add_api("openapi.yaml")
    app.run(port=8080)