ALTER TABLE sales
ADD CONSTRAINT fk_sales_customer FOREIGN KEY (customer_id) REFERENCES customers(id);

ALTER TABLE sales
ADD CONSTRAINT fk_sales_seller FOREIGN KEY (seller_id) REFERENCES sellers(id);

ALTER TABLE sales
ADD CONSTRAINT fk_sales_product FOREIGN KEY (product_id) REFERENCES products(id);

ALTER TABLE sales
ADD CONSTRAINT fk_sales_store FOREIGN KEY (store_id) REFERENCES stores(id);

ALTER TABLE sales
ADD CONSTRAINT fk_sales_supplier FOREIGN KEY (supplier_id) REFERENCES suppliers(id);

ALTER TABLE pets
ADD CONSTRAINT fk_pets_customer FOREIGN KEY (customer_id) REFERENCES customers(id);


