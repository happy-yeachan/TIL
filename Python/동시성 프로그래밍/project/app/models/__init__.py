from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine
from app.config import MONGO_DB_NAME, MONGO_URL


class MongoDB:
    def __init__(self):
        self.client = None
        self.engine = None
    def connect(self):
        self.client = AsyncIOMotorClient(MONGO_URL)
        self.engine = AIOEngine(client=self.client, database=MONGO_DB_NAME)
        print("DB연결 성공")
    def close(self):
        self.client.close()
        print("DB연결 해제")

mongodb = MongoDB()