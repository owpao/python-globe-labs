from peewee import *
import config
from playhouse.db_url import connect

# db = MySQLDatabase(config.DATABASE, user=config.DB_USERNAME, password=config.DB_PASSWORD,
                        #  host=config.DB_HOST, port=config.DB_PORT)

db = connect("mysql://uq5gvkp7c7x7hcof:d1160477gm6lmgel@thzz882efnak0xod.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/tv0uepgefu8vukqi")

class Subscriber(Model):
    address = CharField()
    access_token = CharField

    class Meta:
        database = db

print(config.DATABASE)
print(config.DB_USERNAME)
print(config.DB_PASSWORD)
print(config.DB_PORT)
print(config.DB_HOST)

db.connect()
# db.create_tables([Subscriber])