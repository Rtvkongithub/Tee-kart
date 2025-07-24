CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    price INTEGER NOT NULL
);

INSERT INTO products (name, price) VALUES
('Classic Tee', 499),
('Premium Tee', 799);
