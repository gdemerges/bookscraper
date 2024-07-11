CREATE DATABASE bookscraper;

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    price FLOAT,
    stock INT,
    rating VARCHAR(50),
    category VARCHAR(255)
);

SELECT * FROM books;

--les 10 produits les plus chers
SELECT title, price
FROM books
ORDER BY price DESC
LIMIT 10;

--les 10 produits les moins chers
SELECT title, price
FROM books
ORDER BY price ASC
LIMIT 10;

--les 5 catégories ayant le plus de produits en stocks
SELECT category, SUM(stock) AS total_stock
FROM books
GROUP BY category
ORDER BY total_stock DESC
LIMIT 5;


--les trois catégories ayant les produits les plus chers
SELECT category, AVG(price) AS avg_price
FROM books
GROUP BY category
ORDER BY avg_price DESC
LIMIT 3;

--les différentes catégories et le nombre de livres dans chacune
SELECT category, COUNT(*) AS book_count
FROM books
GROUP BY category
ORDER BY category;


--le nombre de livre par note
SELECT rating, COUNT(*) AS count
FROM books
GROUP BY rating
ORDER BY rating;
