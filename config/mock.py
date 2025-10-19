import mongomock


class MockConfig:
    MONGODB_SETTINGS = {
        'db': 'mockdb',
        'host': 'mongodb://localhost',
        'mongo_client_class': mongomock.MongoClient,
    }
