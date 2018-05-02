Goog$\cdot$li$\cdot$bre
---------
a Google Play Books $\times$ Calibre plug-in :metal::books:

### Getting ID of Play Books Bookshelf
OAuth 2.0 scope information for the Books API:
`https://www.googleapis.com/auth/books`

get shelf id:
```python
bookshelves <- books.mylibrary.bookshelves.list

for bookshelf in bookshelves:
	if bookshelf[title] == "My Google eBooks":
		shelfID <- bookshelf[id]
```

add a book to Play Books:
```pythont
bookshelves <- books.mylibrary.bookshelves.list

for bookshelf in bookshelves:
	if bookshelf[title] == "My Google eBooks":
		shelfID <- bookshelf[id]
```

remove a book from Play Books:
```python
bookshelves <- books.mylibrary.bookshelves.list

for bookshelf in bookshelves:
	if bookshelf[title] == "My Google eBooks":
		shelfID <- bookshelf[id]
```
