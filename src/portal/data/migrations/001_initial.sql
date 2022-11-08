CREATE TABLE project (
    id INT NOT NULL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description VARCHAR(1024) NOT NULL,
    technology VARCHAR(20) NOT NULL,
    image VARCHAR(255) NOT NULL
);
