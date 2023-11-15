-- full-creation
-- creates a table second_table and assign the specified rows to it, while the databe will be passed as an argument to mysql command.
CREATE TABLE IF NOT EXISTS second_table (id INT,
name VARCHAR(256),
score INT);
INSERT INTO second_table (id, name, score)
VALUES (1, "John", 10),
(2, "Alex", 3),
(3, "Bob", 14),
(4, "George", 8);
