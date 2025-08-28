from . import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


# Pour exécuter l’application localement : python -m flask run --host=
# Pour exécuter les tests : python -m unittest discover -s app/tests