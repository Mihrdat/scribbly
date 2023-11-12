import os

MINIO_STORAGE_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY", default="minioadmin")
MINIO_STORAGE_SECRET_KEY = os.getenv("MINIO_SECRET_KEY", default="minioadmin")
MINIO_STORAGE_ENDPOINT = os.getenv("MINIO_STORAGE_ENDPOINT", default="localhost:9000")
MINIO_STORAGE_AUTO_CREATE_MEDIA_BUCKET = True
MINIO_STORAGE_AUTO_CREATE_STATIC_BUCKET = True
MINIO_STORAGE_MEDIA_BUCKET_NAME = "media"
MINIO_STORAGE_STATIC_BUCKET_NAME = "static"