from application import create_app
import os

if os.getenv("FLASK_ENV") == "development":
    from config.dev import DevConfig as Config
elif os.getenv("FLASK_ENV") == "testing":
    from config.mock import MockConfig as Config
else:
    from config.prod import ProdConfig as Config

if __name__ == "__main__":
    app = create_app(Config)
    app.run(debug=True, host="0.0.0.0", port=os.getenv("PORT", 80))
