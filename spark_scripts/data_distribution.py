from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DateType, DoubleType
import time
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("DataDistribution")

def clear_table(spark, db_url, properties, table_name):
    """Очистка таблицы перед вставкой новых данных"""
    logger.info(f"Clearing table {table_name}...")
    
    try:
        import psycopg2
        
        # Используем явные параметры подключения вместо парсинга URL
        conn = psycopg2.connect(
            host="db",  # Имя сервиса в docker-compose
            port=5432,  # Стандартный порт PostgreSQL
            database="abd2_db",
            user=properties["user"],
            password=properties["password"]
        )
        
        # Для таблиц с зависимостями используем TRUNCATE с CASCADE
        if table_name in ["customers", "sellers", "products", "stores", "suppliers"]:
            with conn.cursor() as cursor:
                cursor.execute(f"TRUNCATE TABLE {table_name} CASCADE")
                logger.info(f"Table {table_name} truncated with CASCADE")
        else:
            with conn.cursor() as cursor:
                cursor.execute(f"DELETE FROM {table_name}")
                logger.info(f"All records deleted from {table_name}")
        
        conn.commit()
        
    except Exception as e:
        logger.error(f"Error clearing table {table_name}: {str(e)}")
        raise
    finally:
        if 'conn' in locals():
            conn.close()


def wait_for_postgres():
    """Ожидание готовности PostgreSQL"""
    import psycopg2
    while True:
        try:
            conn = psycopg2.connect(
                host="db",
                database="abd2_db",
                user="postgres",
                password="postgres",
                port=5432
            )
            conn.close()
            logger.info("PostgreSQL is ready!")
            return
        except Exception as e:
            logger.info("Waiting for PostgreSQL...")
            time.sleep(5)

def create_spark_session():
    """Создание Spark сессии с настройками для работы с PostgreSQL"""
    return SparkSession.builder \
        .appName("PetShop Data Distribution") \
        .config("spark.jars", "/opt/bitnami/spark/jars/postgresql-42.5.0.jar") \
        .config("spark.executor.memory", "2g") \
        .config("spark.driver.memory", "2g") \
        .config("spark.sql.shuffle.partitions", "10") \
        .getOrCreate()

def read_mock_data(spark, db_url, properties):
    """Чтение данных из таблицы mock_data"""
    logger.info("Reading data from mock_data table...")
    return spark.read.jdbc(
        url=db_url,
        table="mock_data",
        properties=properties
    ).cache()


def distribute_customers(spark, mock_data, db_url, properties):
    """Распределение данных в таблицу customers"""
    logger.info("Processing customers data...")
    customers = mock_data.select(
        col("customer_first_name").alias("first_name"),
        col("customer_last_name").alias("last_name"),
        col("customer_age").alias("age"),
        col("customer_email").alias("email"),
        col("customer_country").alias("country"),
        col("customer_postal_code").alias("postal_code")
    ).distinct()
    
    # Очищаем таблицу перед вставкой
    clear_table(spark, db_url, properties, "customers")
    
    logger.info(f"Writing {customers.count()} customers records...")
    customers.write.jdbc(
        url=db_url,
        table="customers",
        mode="append",
        properties=properties
    )
    
    # Читаем обратно сгенерированные PostgreSQL ID
    customers_with_ids = spark.read.jdbc(
        url=db_url,
        table="customers",
        properties=properties
    )
    
    return customers_with_ids

def distribute_sellers(spark, mock_data, db_url, properties):
    """Распределение данных в таблицу sellers"""
    logger.info("Processing sellers data...")
    sellers = mock_data.select(
        col("seller_first_name").alias("first_name"),
        col("seller_last_name").alias("last_name"),
        col("seller_email").alias("email"),
        col("seller_country").alias("country"),
        col("seller_postal_code").alias("postal_code")
    ).distinct()
    
    # Очищаем таблицу перед вставкой
    clear_table(spark, db_url, properties, "sellers")
    
    logger.info(f"Writing {sellers.count()} sellers records...")
    sellers.write.jdbc(
        url=db_url,
        table="sellers",
        mode="append",
        properties=properties
    )
    
    # Читаем обратно сгенерированные PostgreSQL ID
    sellers_with_ids = spark.read.jdbc(
        url=db_url,
        table="sellers",
        properties=properties
    )
    
    return sellers_with_ids

def distribute_products(spark, mock_data, db_url, properties):
    """Распределение данных в таблицу products"""
    logger.info("Processing products data...")
    products = mock_data.select(
        col("product_name").alias("name"),
        col("product_category").alias("category"),
        col("product_price").alias("price"),
        col("product_weight").alias("weight"),
        col("product_color").alias("color"),
        col("product_size").alias("size"),
        col("product_brand").alias("brand"),
        col("product_material").alias("material"),
        col("product_description").alias("description"),
        col("product_rating").alias("rating"),
        col("product_reviews").alias("reviews"),
        col("product_release_date").alias("release_date"),
        col("product_expiry_date").alias("expiry_date"),
        col("pet_category").alias("pet_category")
    ).distinct()
    
    # Очищаем таблицу перед вставкой
    clear_table(spark, db_url, properties, "products")
    
    logger.info(f"Writing {products.count()} products records...")
    products.write.jdbc(
        url=db_url,
        table="products",
        mode="append",
        properties=properties
    )
    
    # Читаем обратно сгенерированные PostgreSQL ID
    products_with_ids = spark.read.jdbc(
        url=db_url,
        table="products",
        properties=properties
    )
    
    return products_with_ids

def distribute_stores(spark, mock_data, db_url, properties):
    """Распределение данных в таблицу stores"""
    logger.info("Processing stores data...")
    stores = mock_data.select(
        col("store_name").alias("name"),
        col("store_location").alias("location"),
        col("store_city").alias("city"),
        col("store_state").alias("state"),
        col("store_country").alias("country"),
        col("store_phone").alias("phone"),
        col("store_email").alias("email")
    ).distinct()
    
    # Очищаем таблицу перед вставкой
    clear_table(spark, db_url, properties, "stores")
    
    logger.info(f"Writing {stores.count()} stores records...")
    stores.write.jdbc(
        url=db_url,
        table="stores",
        mode="append",
        properties=properties
    )
    
    # Читаем обратно сгенерированные PostgreSQL ID
    stores_with_ids = spark.read.jdbc(
        url=db_url,
        table="stores",
        properties=properties
    )
    
    return stores_with_ids

def distribute_suppliers(spark, mock_data, db_url, properties):
    """Распределение данных в таблицу suppliers"""
    logger.info("Processing suppliers data...")
    suppliers = mock_data.select(
        col("supplier_name").alias("name"),
        col("supplier_contact").alias("contact"),
        col("supplier_email").alias("email"),
        col("supplier_phone").alias("phone"),
        col("supplier_address").alias("address"),
        col("supplier_city").alias("city"),
        col("supplier_country").alias("country")
    ).distinct()
    
    # Очищаем таблицу перед вставкой
    clear_table(spark, db_url, properties, "suppliers")
    
    logger.info(f"Writing {suppliers.count()} suppliers records...")
    suppliers.write.jdbc(
        url=db_url,
        table="suppliers",
        mode="append",
        properties=properties
    )
    
    # Читаем обратно сгенерированные PostgreSQL ID
    suppliers_with_ids = spark.read.jdbc(
        url=db_url,
        table="suppliers",
        properties=properties
    )
    
    return suppliers_with_ids

def distribute_pets(spark, mock_data, customers, db_url, properties):
    """Распределение данных в таблицу pets"""
    logger.info("Processing pets data...")
    
    pets_data = mock_data.select(
        col("customer_first_name"),
        col("customer_last_name"),
        col("customer_email"),
        col("customer_pet_type").alias("type"),
        col("customer_pet_name").alias("name"),
        col("customer_pet_breed").alias("breed")
    ).distinct()
    
    pets = pets_data.join(
        customers,
        (pets_data.customer_first_name == customers.first_name) &
        (pets_data.customer_last_name == customers.last_name) &
        (pets_data.customer_email == customers.email),
        "inner"
    ).select(
        col("id").alias("customer_id"),
        col("type"),
        col("name"),
        col("breed")
    )
    
    # Очищаем таблицу перед вставкой
    clear_table(spark, db_url, properties, "pets")
    
    logger.info(f"Writing {pets.count()} pets records...")
    pets.write.jdbc(
        url=db_url,
        table="pets",
        mode="append",
        properties=properties
    )

def distribute_sales(spark, mock_data, customers, sellers, products, stores, suppliers, db_url, properties):
    """Распределение данных в таблицу sales"""
    logger.info("Processing sales data...")
    
    # Create aliases for all DataFrames to avoid ambiguity
    sales_df = mock_data.alias("sales_df")
    customers_df = customers.alias("customers")
    sellers_df = sellers.alias("sellers")
    products_df = products.alias("products")
    stores_df = stores.alias("stores")
    suppliers_df = suppliers.alias("suppliers")
    
    # Perform the joins with explicit column references
    joined_df = sales_df.join(
        customers_df,
        (sales_df["customer_first_name"] == customers_df["first_name"]) &
        (sales_df["customer_last_name"] == customers_df["last_name"]) &
        (sales_df["customer_email"] == customers_df["email"]),
        "inner"
    ).join(
        sellers_df,
        (sales_df["seller_first_name"] == sellers_df["first_name"]) &
        (sales_df["seller_last_name"] == sellers_df["last_name"]) &
        (sales_df["seller_email"] == sellers_df["email"]),
        "inner"
    ).join(
        products_df,
        (sales_df["product_name"] == products_df["name"]) &
        (sales_df["product_price"] == products_df["price"]),
        "inner"
    ).join(
        stores_df,
        (sales_df["store_name"] == stores_df["name"]) &
        (sales_df["store_email"] == stores_df["email"]),
        "inner"
    ).join(
        suppliers_df,
        sales_df["supplier_name"] == suppliers_df["name"],
        "inner"
    )
    
    # Select final columns with explicit DataFrame references
    sales = joined_df.select(
        sales_df["sale_date"],
        customers_df["id"].alias("customer_id"),
        sellers_df["id"].alias("seller_id"),
        products_df["id"].alias("product_id"),
        stores_df["id"].alias("store_id"),
        suppliers_df["id"].alias("supplier_id"),
        sales_df["sale_quantity"].alias("quantity"),
        sales_df["sale_total_price"].alias("total_price")
    )
    
    # Clear the table before inserting
    clear_table(spark, db_url, properties, "sales")
    
    logger.info(f"Writing {sales.count()} sales records...")
    sales.write.jdbc(
        url=db_url,
        table="sales",
        mode="append",
        properties=properties
    )

def main():
    try:
        wait_for_postgres()
        spark = create_spark_session()
        
        db_url = "jdbc:postgresql://db:5432/abd2_db"
        properties = {
            "user": "postgres",
            "password": "postgres",
            "driver": "org.postgresql.Driver"
        }
        
        mock_data = read_mock_data(spark, db_url, properties)
        
        # Сначала очищаем все таблицы в правильном порядке
        clear_table(spark, db_url, properties, "sales")
        clear_table(spark, db_url, properties, "pets")
        
        # Затем заполняем таблицы
        customers = distribute_customers(spark, mock_data, db_url, properties)
        sellers = distribute_sellers(spark, mock_data, db_url, properties)
        products = distribute_products(spark, mock_data, db_url, properties)
        stores = distribute_stores(spark, mock_data, db_url, properties)
        suppliers = distribute_suppliers(spark, mock_data, db_url, properties)
        
        distribute_pets(spark, mock_data, customers, db_url, properties)
        distribute_sales(
            spark, mock_data, 
            customers, sellers, products, stores, suppliers,
            db_url, properties
        )
        
        logger.info("Data distribution completed successfully!")
        
    except Exception as e:
        logger.error(f"Error during data distribution: {str(e)}")
        raise
    finally:
        if 'spark' in locals():
            spark.stop()

if __name__ == "__main__":
    main()