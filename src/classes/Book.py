import statistics

class Book():
    #class attribute:
    all_books = [] #could have been named all

    #class properties:
    def __init__(self, title, author, page_count):
        self.title = title
        self.author = author
        self.page_count = page_count

        Book.all_books.append(self) #how to put the individual books in to the list of all_books

    @property
    def title(self):
        return self._title
        
    @title.setter
    def title(self, value):
        if type(value) == str:
            self._title = value
        else:
            raise TypeError("Title must be a string!") #CC looks for exception not others

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if type(value) == str:
            self._author = value
        else:
            raise Exception("Author must be a string!")
    
    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, value):
        if type(value) == int and value > 0:
        #if isinstance(value, int) and value > 0: #specific to saying integer is a class and that the value is a instance of the class integer and then checking if that instance is greater than 0
            self._page_count = value
        else:
            raise Exception("Page count must be a positive integer!")
    
    #to make it human readable but not needed and can run your code without it  
    def __str__(self):
        return f"Title: {self.title} and Page count: {self.page_count}"
    
    def __repr__(self):
        return f"Title: '{self.title}' and Page count: {self.page_count}"
    
    #class methods:
    def get_all_books():
        return Book.all_books
        pass

    @classmethod
    def get_first_book(cls):
        return cls.all_books[0]

    def get_avg_page_count():
        # sum_page_count = 0
        # for book in Book.all_books:
        #     sum_page_count += book.page_count
        # avg_page_count = sum_page_count / len(Book.all_books)
        # return avg_page_count
        #long way of doing this
        
        #shorter way of doing the above
        # all_page_counts = [book.page_count for book in Book.all_books]
        # return sum(all_page_counts) / len(all_page_counts)
    
        
        #third way of doing this above
        all_page_counts = [book.page_count for book in Book.all_books]
        return statistics.mean(all_page_counts)
        
    # def get_longest():
    #     curr_longest_book = None
    #     curr_longest_count = 0
    #     for book in Book.all_books:
    #         if book.page_count > curr_longest_count:
    #             curr_longest_count = book.page_count
    #             curr_longest_book = book
    #     return curr_longest_book

    @classmethod
    def get_longest(cls):
        curr_max_mapper = {}
        for book in cls.all_books:
            if book not in curr_max_mapper:
                curr_max_mapper[book] = book.page_count
        #dictionary comprehension
        # curr_max_mapper = {book : book.page_count for book in cls.all_books}
        return max(curr_max_mapper, key = curr_max_mapper.get)
        # return max(curr_max_mapper, key = lambda key : curr_max_mapper[key]) #could have used this instead of the above

#making instances of the Book class
twilight = Book("Twilight", "Stephanie Myer", 200)
new_moon = Book("New Moon", "Stephanie Myer", 405)
eclipse = Book("Eclipse", "Stephanie Myer", 375)
breaking_dawn = Book("Breaking Dawn", "Stephanie Myer", 510)
bree_tanner = Book("The Short Second Life of Bree Tanner", "Stephanie Myer", 100)
midnight_sun = Book("Midnight Sun", "Stephanie Myer", 140)

#checking if an instance of the Book class
print(isinstance(twilight, Book))

#can check what the class of something is:
print(twilight.__class__)

#how to print class attribute:
print(Book.all_books)

for book in Book.all_books:
    print(book.title)

#how to print class methods:
print(Book.get_all_books())