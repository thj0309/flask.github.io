  
from config.default import *

#SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_DATABASE_URI=  'mysql+pymysql://flask@flaskdb:cjnpd12!@flaskdb.mysql.database.azure.com/pmds'
#참고자료 app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\xcdPb\x95\x9a\x18\xf1\xf3\x81gjp\xe3\xe1\xaf\xcd'

from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/flask.log'),
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter': 'default',
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['file']
    }
})