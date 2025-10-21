from application import create_app
import os
import socket

if os.getenv("FLASK_ENV") == "development":
    from config.dev import DevConfig as Config
elif os.getenv("FLASK_ENV") == "testing":
    from config.mock import MockConfig as Config
else:
    from config.prod import ProdConfig as Config

ip_address = socket.gethostbyname(socket.gethostname())

if __name__ == "__main__":
    app = create_app(Config)
    app.run(host=ip_address, port=os.getenv("PORT", 80))
