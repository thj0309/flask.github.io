  
import os

BASE_DIR = os.path.dirname(__file__)

#SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_DATABASE_URI=  'mysql://root:root@localhost/wiki'
#참고자료 app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "dev"