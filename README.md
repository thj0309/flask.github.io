# Flask 기반 Python Back-end Framework
PMDS+

# MacOSX
export FLASK_APP=pybo/__init__.py
export FLASK_ENV=development

# Windows
set FLASK_APP=pybo/__init__.py
set FLASK_ENV=development


# DB
SQLite -> MariaDB
참고자료 : https://pythonq.com/so/python/102893

# DB with Docker
docker-compose.yml 파일 추가
docker compose up -d
docker exec -it {name} bash
mysql -uroot -p



# git
git pull

git add .
git commit -m "ddl added"
git push origin main
