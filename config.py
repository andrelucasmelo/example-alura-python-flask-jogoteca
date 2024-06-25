import os
SECRET_KEY = 'alura'

SQLALCHEMY_DATABASE_URI = "{SGDB}://{usuario}:{senha}@{servidor}:{port}/{database}".format( \
    SGDB="mysql+mysqlconnector",
    usuario="root",
    senha="senha123",
    database="jogoteca",
    servidor="localhost",
    port="13306"
)

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'