CREATE TABLE requests (
    id SERIAL PRIMARY KEY,
    surname VARCHAR(255),
    name VARCHAR(255),
    patronym VARCHAR(255),
    phone VARCHAR(12),
    message TEXT
);
