from book import Book
from author import Author

a1 = Author('abc', 'm', 5)
a2 = Author('jane', 'f', 4)

b1 = Book('book1', 100, 400)
b2 = Book('book2', pages=700, price=900, authors=[a1, a2])

#print b1.has_authors()
print b1.get_details()
print '--------------'
print b2.get_details()
#print b2.has_authors()
print '--------------'
print Author.count