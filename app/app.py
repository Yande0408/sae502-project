import os
import pymysql

from flask import Flask

app = Flask(__name__)


# Récupérer les informations de connexion à MariaDB
# depuis les variables d'environnement du conteneur.
DB_HOST = os.getenv("DB_HOST", "db-server")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


@app.route("/")
def index():
    return "Application SAE5.02 - Flask fonctionne"


@app.route("/db-test")
def db_test():
    try:
        # Ouvrir une connexion vers MariaDB.
        connection = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )

        # Fermer la connexion après le test.
        connection.close()

        return "Connexion MariaDB OK"

    except Exception as erreur:
        return f"Erreur de connexion MariaDB : {erreur}", 500


if __name__ == "__main__":
    # 0.0.0.0 permet d'accepter les connexions venant
    # de l'extérieur du conteneur.
    app.run(host="0.0.0.0", port=5000)
