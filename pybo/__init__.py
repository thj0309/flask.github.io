from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flaskext.markdown import Markdown
from sqlalchemy import MetaData

#import config
import os

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()


def create_app():
    app = Flask(__name__)
#app.config.from_object(config) #config 폴더 생성에 따라 주석 처리

    FLASK_ENV = os.environ["FLASK_ENV"]
    FLASK_APP = os.environ["FLASK_APP"]
    APP_CONFIG_FILE = os.environ["APP_CONFIG_FILE"]
    
    print("FLASK_APP : " , FLASK_APP)
    #print("APP_CONFIG_FILE : " , APP_CONFIG_FILE)    

    #SECRET_KEY = os.getenv("SECRET_KEY")
    #DB_USERNAME = os.environ["DB_USERNAME"]
    #DB_PASSWORD = os.environ["DB_PASSWORD"]
    #DB_HOST = os.environ["DB_HOST"]
    #DATABASE_NAME = os.environ["DATABASE_NAME"]
    #DB_URI = "mysql+pymysql://%s:%s@%s:3306/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, DATABASE_NAME)
    #SQLALCHEMY_DATABASE_URI = DB_URI
    
    app.config.from_envvar('APP_CONFIG_FILE')

    if(app == ''):
        app.config.from_envvar('..\config\development.py')




    # ORM
    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
    #if SQLALCHEMY_DATABASE_URI.startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)

    from . import models

    # 블루프린트
    from .views import main_views, question_views, answer_views, auth_views, comment_views, vote_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(comment_views.bp)
    app.register_blueprint(vote_views.bp)

    # 필터
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime

    # markdown
    Markdown(app, extensions=['nl2br', 'fenced_code'])

    return app