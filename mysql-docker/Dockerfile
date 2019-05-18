FROM mysql
ENV MYSQL_DATABASE embodyvr
COPY ./mysql-script/ /docker-entrypoint-initdb.d/
EXPOSE 3306
