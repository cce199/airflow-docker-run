# airflow-docker-run

## folder설정

folder<br>
 ├ airflow-dags<br>
 ├ airflow-logs<br>
 ├ airflow-docker-run(현재git)<br>
 └ airflow (git clone https://github.com/apache/airflow)

## airflow docker build

airflow폴더에서<br>
docker build -t apache/airflow .

## .env에 환경변수지정

내부에서 사용할 mysql에 id, password를 지정
mysqlid와 mysql-initdb.sh 에 id는 동일해야함

### fernet key 생성

<https://bcb.github.io/airflow/fernet-key> 참조

```install cryptography
pip install cryptography
```

```python
from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())
```

## airflow db init

docker-compose -f docker-compose-init.yml
table 생성안될경우 다시 실행(airflow init보다 db가 먼저올라와서 그러는데 다시 실행하면 해결됨)

## airflow run

docker-compose up -d

## folder설명

- 현재 git folder : airflow 실행관련script
- ./현재 git folder/../airflow-dags/ : 현재폴더와 같은 level에 airflow-dags 폴더에 dag파일 구성
- ./현재 git folder/../airflow-log/ : 현재폴더와 같은 level인 airflow-log 에 log적재

## 파일 설명

### myconf.cnf

mysql 설정파일
explicit_defaults_for_timestamp
TIMESTAMP 컬럼 데이터 타입에 대한 기본값에 대해 명시적으로 지정을 할지 말지를 결정하는 옵션. 기본은 OFF 이나 그럴 경우에 위와 같이 경고 메시지가 나온다.

TIMESTAMP 를 컬럼에서 사용할때 기본값을 명시하지 않으면 이전 버전에서는 “NOT NULL DEFAULT CURRENT_TIMSTAMP ON UPDATE CURRENT_TIMESTAMP” 가 된다. 하지만 5.7 에선 위 옵션을 이용해서 ON 으로 지정할 경우에 “NULL DEFAULT NULL” 값이 지정이 된다.

### mysql-initdb.sql

mysql 생성시 실행script. 사용할 계정에 권한부여 목적

