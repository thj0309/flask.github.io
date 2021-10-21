# Flask 기반 Python Back-end Framework
2021 PMDS+

# 0. Framework w/t PJT
자바 기반의 스프링 프레임워크처럼 파이썬 또한 웹 프레임워크가 있다. <br/>
파이썬 웹 프레임워크에는 장고, 플라스크, FastAPI 등 많은 프레임워크가 있다.<br/>
그 중, 타 프레임워크에 보다 매우 가볍지만 기능이 매우 충실해 많은 현장에서 쓰이는 프레임워크인 플라스크를 선정하여 학습을 했다.<br/>
플라스크르 활용하여 회원가입 기능을 포함한 블로그 기능을 만들었다.<br/>


# 1. Flask 실행하기
## MacOSX
```bash
export FLASK_APP=pybo/__init__.py
export FLASK_ENV=development

#211015 (배포내용 추가)
#개발서버 기준
export APP_CONFIG_FILE=..\config\development.py

#운영서버 기준
export APP_CONFIG_FILE=..\config\production.py
```

## Windows
```bash
win_batch_dev.bat 이거나 win_batch_prd.bat 을 실행하면 된다.


아니면 아래 내용을 입력한다
set FLASK_APP=pybo/__init__.py
set FLASK_ENV=development

#211015 (배포내용 추가)
#개발서버 기준
set APP_CONFIG_FILE=..\config\development.py

#운영서버 기준
set APP_CONFIG_FILE=..\config\production.py
```


## 위 명령어 실행 후
flask run


# 2. Docker 활용하기
--> 사전에 docker-compose에 MariaDB 정보 추가하였음. Docker만 설치되어있다면, 별도로 DB를 설치할 필요없다.<br/>
docker-compose.yml 파일 추가<br/>
docker compose up -d<br/>
docker exec -it {name} bash<br/>
mysql -uroot -p


# 3. git w/t CUI
git pull<br/>
git add .<br/>
git commit -m "ddl added"<br/>
git push origin main



# 0. 기타
## DB 변경
SQLite -> MariaDB<br/>
참고자료 : https://pythonq.com/so/python/102893


# 9. Notion 정보
https://thj0309.notion.site/Python-s-backend-Flask-d386bd4a932c4bfda69d94712093090a
