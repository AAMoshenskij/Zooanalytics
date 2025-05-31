from pyspark.sql import SparkSession
from pyspark.sql.functions import *

def create_reports():
    spark = SparkSession.builder \
        .appName("ClickHouse Reports") \
        .getOrCreate()

    # 1. Подключение к PostgreSQL
    def read_pg(table):
        return spark.read \
            .format("jdbc") \
            .option("url", "jdbc:postgresql://db:5432/abd2_db") \
            .option("dbtable", table) \
            .option("user", "postgres") \
            .option("password", "postgres") \
            .load()

    sales_df = read_pg("sales")
    products_df = read_pg("products")
    customers_df = read_pg("customers")
    stores_df = read_pg("stores")
    suppliers_df = read_pg("suppliers")

    def write_ch(df, table):
        df.write \
            .format("jdbc") \
            .option("url", "jdbc:clickhouse://clickhouse:8123/default") \
            .option("dbtable", table) \
            .option("driver", "com.clickhouse.jdbc.ClickHouseDriver") \
            .option("user", "default") \
            .option("password", "your_secure_password") \
            .option("isolationLevel", "NONE") \
            .option("batchsize", "100000") \
            .option("createTableOptions", "ENGINE = MergeTree() ORDER BY tuple()") \
            .mode("append") \
            .save()

    # Витрина 1: Продажи по продуктам
    product_sales = sales_df.join(products_df, sales_df.product_id == products_df.id) \
        .groupBy("product_id", "name", "category") \
        .agg(
            sum("total_price").alias("total_revenue"),
            sum("quantity").alias("total_sales"),
            avg("rating").alias("avg_rating"),
            sum("reviews").alias("total_reviews")
        ).orderBy(col("total_revenue").desc())
    
    write_ch(product_sales.limit(10), "top_products")

    # Витрина 2: Продажи по клиентам 
    customer_analysis = sales_df.join(customers_df, sales_df.customer_id == customers_df.id) \
        .groupBy("customer_id", "first_name", "last_name", "country") \
        .agg(
            sum("total_price").alias("total_spent"),
            count("*").alias("purchase_count"),
            (sum("total_price") / count("*")).alias("avg_check")
        ).orderBy(col("total_spent").desc())
    
    write_ch(customer_analysis.limit(10), "top_customers")

    # Витрина 3: Продажи по времени 
    time_analysis = sales_df \
        .withColumn("year", year("sale_date")) \
        .withColumn("month", month("sale_date")) \
        .groupBy("year", "month") \
        .agg(
            sum("total_price").alias("monthly_revenue"),
            avg("total_price").alias("avg_order_size"),
            count("*").alias("orders_count")
        )
    
    write_ch(time_analysis, "sales_by_time")

    # Витрина 4: Продажи по магазинам 
    store_analysis = sales_df.join(stores_df, sales_df.store_id == stores_df.id) \
        .groupBy("store_id", "name", "city", "country") \
        .agg(
            sum("total_price").alias("total_revenue"),
            count("*").alias("sales_count"),
            (sum("total_price") / count("*")).alias("avg_check")
        ).orderBy(col("total_revenue").desc())
    
    write_ch(store_analysis.limit(5), "top_stores")

    # Витрина 5: Продажи по поставщикам 
    supplier_analysis = sales_df.join(suppliers_df, sales_df.supplier_id == suppliers_df.id) \
        .join(products_df, sales_df.product_id == products_df.id) \
        .groupBy(
            suppliers_df["id"].alias("supplier_id"), 
            suppliers_df["name"].alias("name"),  
            suppliers_df["country"]
        ) \
        .agg(
            sum("total_price").alias("total_revenue"),
            avg(products_df["price"]).alias("avg_product_price"),
            count("*").alias("sales_count")
        ).orderBy(col("total_revenue").desc())

    write_ch(supplier_analysis.limit(5), "top_suppliers")

    # Витрина 6: Качество продукции 
    product_quality = products_df \
        .select("id", "name", "category", "rating", "reviews") \
        .orderBy(col("rating").desc(), col("reviews").desc())
    
    write_ch(product_quality, "product_quality")

    spark.stop()

if __name__ == "__main__":
    create_reports()