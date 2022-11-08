CREATE TABLE project (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description VARCHAR(1024) NOT NULL,
    technology VARCHAR(20) NOT NULL,
    image VARCHAR(255) NOT NULL
);

CREATE TABLE category (
    id SERIAL PRIMARY KEY,
    name VARCHAR(20) NOT NULL
);

CREATE TABLE post (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    body VARCHAR NOT NULL,
    created_on DATE NOT NULL,
    last_modified DATE NOT NULL
);

CREATE TABLE post_categories (
    post_id INT NOT NULL REFERENCES post (id) ON UPDATE CASCADE,
    category_id INT NOT NULL REFERENCES category (id) ON UPDATE CASCADE,
    CONSTRAINT post_category_pkey PRIMARY KEY (post_id, category_id)
);

CREATE TABLE comment (
    id SERIAL PRIMARY KEY,
    post_id INT NOT NULL REFERENCES post (id) ON DELETE CASCADE ON UPDATE CASCADE, 
    author VARCHAR(60) NOT NULL,
    body VARCHAR NOT NULL,
    created_on DATE NOT NULL
);
