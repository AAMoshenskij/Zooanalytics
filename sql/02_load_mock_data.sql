-- Создание таблицы mock_data
CREATE TABLE IF NOT EXISTS mock_data (
    id SERIAL PRIMARY KEY,
    customer_first_name VARCHAR(100),
    customer_last_name VARCHAR(100),
    customer_age INT,
    customer_email VARCHAR(100),
    customer_country VARCHAR(100),
    customer_postal_code VARCHAR(20),
    customer_pet_type VARCHAR(50),
    customer_pet_name VARCHAR(100),
    customer_pet_breed VARCHAR(100),
    seller_first_name VARCHAR(100),
    seller_last_name VARCHAR(100),
    seller_email VARCHAR(100),
    seller_country VARCHAR(100),
    seller_postal_code VARCHAR(20),
    product_name VARCHAR(100),
    product_category VARCHAR(50),
    product_price DECIMAL(10, 2),
    product_quantity INT,
    sale_date DATE,
    sale_customer_id INT,
    sale_seller_id INT,
    sale_product_id INT,
    sale_quantity INT,
    sale_total_price DECIMAL(10, 2),
    store_name VARCHAR(100),
    store_location VARCHAR(100),
    store_city VARCHAR(100),
    store_state VARCHAR(100),
    store_country VARCHAR(100),
    store_phone VARCHAR(20),
    store_email VARCHAR(100),
    pet_category VARCHAR(100),
    product_weight DECIMAL(10, 2),
    product_color VARCHAR(50),
    product_size VARCHAR(50),
    product_brand VARCHAR(100),
    product_material VARCHAR(100),
    product_description TEXT,
    product_rating DECIMAL(3, 2),
    product_reviews INT,
    product_release_date DATE,
    product_expiry_date DATE,
    supplier_name VARCHAR(100),
    supplier_contact VARCHAR(100),
    supplier_email VARCHAR(100),
    supplier_phone VARCHAR(20),
    supplier_address VARCHAR(100),
    supplier_city VARCHAR(100),
    supplier_country VARCHAR(100)
);

-- Загрузка CSV-файлов в mock_data

COPY mock_data(
    id,
    customer_first_name, customer_last_name, customer_age, customer_email, customer_country, customer_postal_code,
    customer_pet_type, customer_pet_name, customer_pet_breed,
    seller_first_name, seller_last_name, seller_email, seller_country, seller_postal_code,
    product_name, product_category, product_price, product_quantity,
    sale_date, sale_customer_id, sale_seller_id, sale_product_id, sale_quantity, sale_total_price,
    store_name, store_location, store_city, store_state, store_country, store_phone, store_email,
    pet_category, product_weight, product_color, product_size, product_brand, product_material,
    product_description, product_rating, product_reviews, product_release_date, product_expiry_date,
    supplier_name, supplier_contact, supplier_email, supplier_phone, supplier_address, supplier_city, supplier_country
)
FROM '/docker-entrypoint-initdb.d/исходные_данные/mock_1.csv' DELIMITER ',' CSV HEADER;

COPY mock_data(
    id,
    customer_first_name, customer_last_name, customer_age, customer_email, customer_country, customer_postal_code,
    customer_pet_type, customer_pet_name, customer_pet_breed,
    seller_first_name, seller_last_name, seller_email, seller_country, seller_postal_code,
    product_name, product_category, product_price, product_quantity,
    sale_date, sale_customer_id, sale_seller_id, sale_product_id, sale_quantity, sale_total_price,
    store_name, store_location, store_city, store_state, store_country, store_phone, store_email,
    pet_category, product_weight, product_color, product_size, product_brand, product_material,
    product_description, product_rating, product_reviews, product_release_date, product_expiry_date,
    supplier_name, supplier_contact, supplier_email, supplier_phone, supplier_address, supplier_city, supplier_country
)
FROM '/docker-entrypoint-initdb.d/исходные_данные/mock_2.csv' DELIMITER ',' CSV HEADER;

COPY mock_data(
    id,
    customer_first_name, customer_last_name, customer_age, customer_email, customer_country, customer_postal_code,
    customer_pet_type, customer_pet_name, customer_pet_breed,
    seller_first_name, seller_last_name, seller_email, seller_country, seller_postal_code,
    product_name, product_category, product_price, product_quantity,
    sale_date, sale_customer_id, sale_seller_id, sale_product_id, sale_quantity, sale_total_price,
    store_name, store_location, store_city, store_state, store_country, store_phone, store_email,
    pet_category, product_weight, product_color, product_size, product_brand, product_material,
    product_description, product_rating, product_reviews, product_release_date, product_expiry_date,
    supplier_name, supplier_contact, supplier_email, supplier_phone, supplier_address, supplier_city, supplier_country
)
FROM '/docker-entrypoint-initdb.d/исходные_данные/mock_3.csv' DELIMITER ',' CSV HEADER;

COPY mock_data(
    id,
    customer_first_name, customer_last_name, customer_age, customer_email, customer_country, customer_postal_code,
    customer_pet_type, customer_pet_name, customer_pet_breed,
    seller_first_name, seller_last_name, seller_email, seller_country, seller_postal_code,
    product_name, product_category, product_price, product_quantity,
    sale_date, sale_customer_id, sale_seller_id, sale_product_id, sale_quantity, sale_total_price,
    store_name, store_location, store_city, store_state, store_country, store_phone, store_email,
    pet_category, product_weight, product_color, product_size, product_brand, product_material,
    product_description, product_rating, product_reviews, product_release_date, product_expiry_date,
    supplier_name, supplier_contact, supplier_email, supplier_phone, supplier_address, supplier_city, supplier_country
)
FROM '/docker-entrypoint-initdb.d/исходные_данные/mock_4.csv' DELIMITER ',' CSV HEADER;

COPY mock_data(
    id,
    customer_first_name, customer_last_name, customer_age, customer_email, customer_country, customer_postal_code,
    customer_pet_type, customer_pet_name, customer_pet_breed,
    seller_first_name, seller_last_name, seller_email, seller_country, seller_postal_code,
    product_name, product_category, product_price, product_quantity,
    sale_date, sale_customer_id, sale_seller_id, sale_product_id, sale_quantity, sale_total_price,
    store_name, store_location, store_city, store_state, store_country, store_phone, store_email,
    pet_category, product_weight, product_color, product_size, product_brand, product_material,
    product_description, product_rating, product_reviews, product_release_date, product_expiry_date,
    supplier_name, supplier_contact, supplier_email, supplier_phone, supplier_address, supplier_city, supplier_country
)
FROM '/docker-entrypoint-initdb.d/исходные_данные/mock_5.csv' DELIMITER ',' CSV HEADER;

COPY mock_data(
    id,
    customer_first_name, customer_last_name, customer_age, customer_email, customer_country, customer_postal_code,
    customer_pet_type, customer_pet_name, customer_pet_breed,
    seller_first_name, seller_last_name, seller_email, seller_country, seller_postal_code,
    product_name, product_category, product_price, product_quantity,
    sale_date, sale_customer_id, sale_seller_id, sale_product_id, sale_quantity, sale_total_price,
    store_name, store_location, store_city, store_state, store_country, store_phone, store_email,
    pet_category, product_weight, product_color, product_size, product_brand, product_material,
    product_description, product_rating, product_reviews, product_release_date, product_expiry_date,
    supplier_name, supplier_contact, supplier_email, supplier_phone, supplier_address, supplier_city, supplier_country
)
FROM '/docker-entrypoint-initdb.d/исходные_данные/mock_6.csv' DELIMITER ',' CSV HEADER;

COPY mock_data(
    id,
    customer_first_name, customer_last_name, customer_age, customer_email, customer_country, customer_postal_code,
    customer_pet_type, customer_pet_name, customer_pet_breed,
    seller_first_name, seller_last_name, seller_email, seller_country, seller_postal_code,
    product_name, product_category, product_price, product_quantity,
    sale_date, sale_customer_id, sale_seller_id, sale_product_id, sale_quantity, sale_total_price,
    store_name, store_location, store_city, store_state, store_country, store_phone, store_email,
    pet_category, product_weight, product_color, product_size, product_brand, product_material,
    product_description, product_rating, product_reviews, product_release_date, product_expiry_date,
    supplier_name, supplier_contact, supplier_email, supplier_phone, supplier_address, supplier_city, supplier_country
)
FROM '/docker-entrypoint-initdb.d/исходные_данные/mock_7.csv' DELIMITER ',' CSV HEADER;

COPY mock_data(
    id,
    customer_first_name, customer_last_name, customer_age, customer_email, customer_country, customer_postal_code,
    customer_pet_type, customer_pet_name, customer_pet_breed,
    seller_first_name, seller_last_name, seller_email, seller_country, seller_postal_code,
    product_name, product_category, product_price, product_quantity,
    sale_date, sale_customer_id, sale_seller_id, sale_product_id, sale_quantity, sale_total_price,
    store_name, store_location, store_city, store_state, store_country, store_phone, store_email,
    pet_category, product_weight, product_color, product_size, product_brand, product_material,
    product_description, product_rating, product_reviews, product_release_date, product_expiry_date,
    supplier_name, supplier_contact, supplier_email, supplier_phone, supplier_address, supplier_city, supplier_country
)
FROM '/docker-entrypoint-initdb.d/исходные_данные/mock_8.csv' DELIMITER ',' CSV HEADER;

COPY mock_data(
    id,
    customer_first_name, customer_last_name, customer_age, customer_email, customer_country, customer_postal_code,
    customer_pet_type, customer_pet_name, customer_pet_breed,
    seller_first_name, seller_last_name, seller_email, seller_country, seller_postal_code,
    product_name, product_category, product_price, product_quantity,
    sale_date, sale_customer_id, sale_seller_id, sale_product_id, sale_quantity, sale_total_price,
    store_name, store_location, store_city, store_state, store_country, store_phone, store_email,
    pet_category, product_weight, product_color, product_size, product_brand, product_material,
    product_description, product_rating, product_reviews, product_release_date, product_expiry_date,
    supplier_name, supplier_contact, supplier_email, supplier_phone, supplier_address, supplier_city, supplier_country
)
FROM '/docker-entrypoint-initdb.d/исходные_данные/mock_9.csv' DELIMITER ',' CSV HEADER;

COPY mock_data(
    id,
    customer_first_name, customer_last_name, customer_age, customer_email, customer_country, customer_postal_code,
    customer_pet_type, customer_pet_name, customer_pet_breed,
    seller_first_name, seller_last_name, seller_email, seller_country, seller_postal_code,
    product_name, product_category, product_price, product_quantity,
    sale_date, sale_customer_id, sale_seller_id, sale_product_id, sale_quantity, sale_total_price,
    store_name, store_location, store_city, store_state, store_country, store_phone, store_email,
    pet_category, product_weight, product_color, product_size, product_brand, product_material,
    product_description, product_rating, product_reviews, product_release_date, product_expiry_date,
    supplier_name, supplier_contact, supplier_email, supplier_phone, supplier_address, supplier_city, supplier_country
)
FROM '/docker-entrypoint-initdb.d/исходные_данные/mock.csv' DELIMITER ',' CSV HEADER;

