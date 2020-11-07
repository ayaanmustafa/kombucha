from dotenv import load_dotenv
import os

class Config:
    load_dotenv()
    SECRET_KEY = os.getenv('db_secretKey')
    SQLALCHEMY_DATABASE_URI = os.getenv('db_SQL')
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587 
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv('db_userKombucha')
    MAIL_PASSWORD = os.getenv('db_userPassword')

    #os.getenv('db_userKombucha')
    #os.getenv('db_userPassword')