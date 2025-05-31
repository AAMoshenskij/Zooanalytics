-- 1. Customers
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    age INT,
    email VARCHAR(100),
    country VARCHAR(100),
    postal_code VARCHAR(20)
);

-- 2. Sellers
CREATE TABLE sellers (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(100),
    country VARCHAR(100),
    postal_code VARCHAR(20)
);

-- 3. Products
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2),
    weight DECIMAL(10,2),
    color VARCHAR(50),
    size VARCHAR(50),
    brand VARCHAR(100),
    material VARCHAR(100),
    description TEXT,
    rating DECIMAL(3,2),
    reviews INT,
    release_date DATE,
    expiry_date DATE,
    pet_category VARCHAR(100)
);

-- 4. Stores
CREATE TABLE stores (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    location VARCHAR(100),
    city VARCHAR(100),
    state VARCHAR(100),
    country VARCHAR(100),
    phone VARCHAR(20),
    email VARCHAR(100)
);

-- 5. Suppliers
CREATE TABLE suppliers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    contact VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    address VARCHAR(100),
    city VARCHAR(100),
    country VARCHAR(100)
);

-- 6. Pets
CREATE TABLE pets (
    id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(id),
    type VARCHAR(50),
    name VARCHAR(100),
    breed VARCHAR(100)
);

-- 7. Sales
CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    sale_date DATE,
    customer_id INT REFERENCES customers(id),
    seller_id INT REFERENCES sellers(id),
    product_id INT REFERENCES products(id),
    store_id INT REFERENCES stores(id),
    supplier_id INT REFERENCES suppliers(id),
    quantity INT,
    total_price DECIMAL(10,2)
);


