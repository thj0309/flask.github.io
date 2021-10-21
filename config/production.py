  
from config.default import *

#SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_DATABASE_URI=  'mysql+pymysql://root:root@localhost/pmds'
#참고자료 app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\xcdPb\x95\x9a\x18\xf1\xf3\x81gjp\xe3\xe1\xaf\xcd'