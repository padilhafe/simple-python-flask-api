import os


class ProdConfig:
    MONGODB_SETTINGS = {
        'host': os.getenv("MONGODB_ATLAS_URI"),
    }
