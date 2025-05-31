# BigDataSnowflake
Запуск:
1) docker-compose up -d --build
2) docker exec -it abd2_spark pip install psycopg2-binary
2) docker exec -it abd2_spark bash -c "
  export SPARK_HOME=/opt/bitnami/spark && \
  export IVY2_HOME=/tmp/.ivy2 && \
  /opt/bitnami/spark/bin/spark-submit \
    --master spark://spark:7077 \
    --conf spark.jars=/opt/bitnami/spark/jars/postgresql-42.5.0.jar \
    --conf spark.driver.extraClassPath=/opt/bitnami/spark/jars/postgresql-42.5.0.jar \
    --conf spark.executor.extraClassPath=/opt/bitnami/spark/jars/postgresql-42.5.0.jar \
    /app/data_distribution.py
"
3) docker exec -it abd2_spark /opt/bitnami/spark/bin/spark-submit   --driver-class-path /opt/bitnami/spark/jars/postgresql-42.5.0.jar:/opt/bitnami/spark/jars/clickhouse-jdbc-0.4.6.jar   /app/create_reports.py

Примеры запросов:
user@user-GF63-Thin-11UD:~/ABD_labs/lab22$ curl -X POST "http://localhost:8123?user=default&password=your_secure_password"   --data "SELECT * FROM top_customers ORDER BY total_spent DESC LIMIT 5"
30475   Katerine        Screech Croatia 178702.08       384     465.37
34146   Tadio   Care    China   136622.88       306     446.48
27053   Basilius        Lambie  Portugal        132072.96       384     343.94
29208   Paulette        McCooke Portugal        116232.9        294     395.35
34612   Gratiana        Turtle  Indonesia       90253.68        204     442.42

user@user-GF63-Thin-11UD:~/ABD_labs/lab22$ curl -X POST "http://localhost:8123?user=default&password=your_secure_password"   --data "SELECT * FROM top_products LIMIT 5"
27977   Dog Food        Cage    60224   384     2.5     81664
30642   Cat Toy Cage    63502.82        1077    4.5     47763
31515   Dog Food        Food    56757.87        495     2.7     16113
32468   Bird Cage       Cage    58795.16        767     4.1     636
32561   Cat Toy Food    63502.82        1077    1.1     142557

