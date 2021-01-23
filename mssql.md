# Docker commands

## run the mssql docker container
```
docker run  \
-e 'ACCEPT_EULA=Y' \
-e 'SA_PASSWORD=secretPassword1' \
-v sqldata1:/var/opt/mssql \
-p 1433:1433 \
--name sql17 \
-d \
mcr.microsoft.com/mssql/server:2017-latest
```

## connect to the database
```
docker exec -it sql17 /opt/mssql-tools/bin/sqlcmd \
-S localhost \
-U sa \
-P 'secretPassword1'
```

## run queries against the database from local terminal
```
docker exec -it sql17 /opt/mssql-tools/bin/sqlcmd \
-S localhost,1433 \
-U sa \
-Q 'SELECT @@version' \
-P secretPassword1 \
-W
```
### or
``` 
docker exec -it sql17 /opt/mssql-tools/bin/sqlcmd \
-S localhost,1433 \
-U sa \
-Q 'SELECT name, physical_name from sys.master_files' \
-P secretPassword1 \
-W
```

---

# SQL

## create database
```
CREATE database foo
```

## use database
```
use foo
```

## create table
```
CREATE table foo (id int)
```

## show tables in database
```
SELECT Distinct TABLE_NAME FROM information_schema.TABLES
```
---

## optional -> use local connector
```
npm install -g sql-cli
mssql -u sa -p secretPassword1
```

### additional env

``` 
MSSQL_PID=<your_product_id | edition_name> (default: Developer)
```

### additional versions

2019-latest


# Links:

[docker INSTALL](https://hub.docker.com/editions/community/docker-ce-desktop-mac/)

[docker hub](https://hub.docker.com/_/microsoft-mssql-server)

[docker get-started](https://www.docker.com/get-started)

[gui mssql tools](https://stackoverflow.com/a/34153/3993662)

[Microsoft Help Page](https://docs.microsoft.com/de-de/sql/linux/sql-server-linux-docker-container-deployment?view=sql-server-ver15&pivots=cs1-bash)
