import os
import mongomock


class ProdConfig:
    MONGODB_SETTINGS = {
        'host': os.getenv("MONGODB_ATLAS_URI"),
    }


class DevConfig():
    MONGODB_SETTINGS = {
        'db': os.getenv('MONGODB_DB'),
        'host': os.getenv('MONGODB_HOST'),
        'port': int(os.getenv('MONGODB_PORT', 27017)),
        'username': os.getenv('MONGODB_USERNAME'),
        'password': os.getenv('MONGODB_PASSWORD'),
    }


class MockConfig:
    MONGODB_SETTINGS = {
        'db': 'mockdb',
        'host': 'mongodb://localhost',
        'mongo_client_class': mongomock.MongoClient,
    }
