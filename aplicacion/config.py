import os

SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
PWD = os.path.abspath(os.curdir)

DEBUG = True  # En despliegue esto pasa a FALSE
SQLALCHEMY_DATABASE_URI = os.getenv(
    'DATABASE_URL',
    'postgresql://oujie:CLQbC1AfjZOk0qSruSBrEaMXOueQWKJ1@dpg-cul6o256l47c73calhmg-a.frankfurt-postgres.render.com/flaskdb_lhvq'
)
SQLALCHEMY_TRACK_MODIFICATIONS = False
