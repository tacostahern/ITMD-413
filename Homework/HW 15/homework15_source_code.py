'''
Program Author: Tony Acosta Hernandez
Course: ITMD 413
'''

import sqlite3
import pandas as pd

def ex17_2():
    connection = sqlite3.connect('books.db')
    pd.options.display.max_columns = 10
    print(pd.read_sql('SELECT * FROM authors', connection, index_col=['id']))

    print(pd.read_sql('SELECT * FROM titles', connection))

    df = pd.read_sql('SELECT * FROM author_ISBN', connection)
    print(df.head())

    print(pd.read_sql('SELECT first, last FROM authors', connection))

    print(pd.read_sql("SELECT title, edition, copyright FROM titles WHERE copyright > '2016'", connection))

    print(pd.read_sql("SELECT id, first, last FROM authors WHERE last LIKE 'D%'", connection, index_col=['id']))

    print(pd.read_sql("SELECT id, first, last FROM authors WHERE first LIKE '_b%'", connection, index_col=['id']))

    print(pd.read_sql('SELECT title FROM titles ORDER BY title ASC', connection))

    print(pd.read_sql("SELECT id, first, last FROM authors ORDER BY last, first", connection, index_col=['id']))

    print(pd.read_sql("SELECT id, first, last FROM authors ORDER BY last DESC, first ASC", connection, index_col=['id']))

    print(pd.read_sql("SELECT isbn, title, edition, copyright FROM titles WHERE title LIKE '%How to Program' ORDER BY title", connection))

    print(pd.read_sql("SELECT first, last, isbn FROM authors INNER JOIN author_isbn ON authors.id = author_ISBN.id ORDER BY last, first", connection).head())
    
    cursor = connection.cursor()
    cursor = cursor.execute("INSERT INTO authors (first, last) VALUES ('Sue', 'Red')")

    print(pd.read_sql('SELECT id, first, last FROM authors', connection, index_col=['id']))

    cursor = cursor.execute("UPDATE authors SET last='Black' WHERE last='Red' AND first='Sue'")
    print(pd.read_sql('SELECT id, first, last FROM authors', connection, index_col=['id']))

    cursor = cursor.execute('DELETE FROM authors WHERE id=6')
    print(pd.read_sql('SELECT id, first, last FROM authors', connection, index_col=['id']))

    print(pd.read_sql("""SELECT title, edition FROM titles ORDER BY edition DESC""", connection).head(3))

    print(pd.read_sql("""SELECT * FROM authors WHERE first LIKE 'A%'""", connection))

    print(pd.read_sql("SELECT isbn, title, edition, copyright FROM titles WHERE title NOT LIKE '%How to Program' ORDER BY title", connection))

def ex17_1():
    connection = sqlite3.connect('books.db')
    pd.options.display.max_columns = 10

    # a) Select all authors’ last names from the authors table in descending order
    print(pd.read_sql('SELECT last FROM authors ORDER BY last DESC', connection))

    # b) Select all book titles from the titles table in ascending order
    print(pd.read_sql('SELECT title FROM titles ORDER BY title ASC', connection))

    # c) Use an INNER JOIN to select all the books for a specific author. Include the title, copyright year and ISBN. Order the information alphabetically by title
    print(pd.read_sql("SELECT t.title, t.isbn, t.copyright FROM titles t INNER JOIN author_ISBN a ON t.isbn = a.isbn ORDER BY title ASC", connection))

    # d) Insert a new author into the authors table
    cursor = connection.cursor()
    cursor = cursor.execute("INSERT INTO authors (first, last) VALUES ('Tony', 'Acosta Hernandez')")
    print(pd.read_sql('SELECT * FROM authors', connection, index_col=['id']))

    # e) Insert a new title for an author. Remember that the book must have an entry in the author_ISBN table and an entry in the titles table
    cursor = cursor.execute("INSERT INTO authors (first, last) VALUES ('Tony', 'Acosta Hernandez')")

    cursor = cursor.execute("INSERT into titles (isbn, title, edition, copyright) VALUES (0123456789, 'I thought my life was a tragedy', 1, '2021')")
    print(pd.read_sql('SELECT * FROM titles', connection))

    cursor = cursor.execute("INSERT INTO author_ISBN (id, isbn) VALUES (7, 0123456789)")
    print(pd.read_sql('SELECT * FROM author_isbn', connection))


ex17_2()
ex17_1()