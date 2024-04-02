import motor.motor_asyncio
from config import MONGO_URL
# AMAX UB # DATABSE #
cli = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
dbb = cli.program
