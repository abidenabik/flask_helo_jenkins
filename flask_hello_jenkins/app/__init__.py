from flask import Flask

def create_app():
    app = Flask(__name__)

    # Configuration basique
    app.config['SECRET_KEY'] = 'supersecretkey'

    # Importer les routes
    from .routes import main
    app.register_blueprint(main)

    return app
