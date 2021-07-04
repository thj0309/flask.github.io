# Flask 기반 Python Back-end Framework
PMDS +

# Configuration
Flask
DB : SQLite
--> 추후, MySQL이나 MariaDB로 변경할 예정
참고자료 : https://pythonq.com/so/python/102893

# MacOSX
export FLASK_APP=pybo/__init__.py
export FLASK_ENV=development

# Windows
set FLASK_APP=pybo/__init__.py
set FLASK_ENV=development


# DB
- docker-compose.yml 파일 추가

docker compose up -d
docker exec -it {name} bash

mysql -uroot -p
# 2021PMDS_FLASK
