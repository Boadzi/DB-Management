

book_library =[] # list to store book imfo

def add_book(title, ID, author, year):

    book={'title':title, 'id':ID, 'author':author, 'year':year} # dictionary to take in book info

    book_library.append(book) # addidng book to list


def remove_book(ID):

    for book in book_library: # finding book using ID
        if book_library['id']==ID

        book_library.remove(book) # removing book from list.

def retrive_book(ID):

    for book in book_library: # finding book using ID
        if book_library['id']==ID
        return book 




def update_book(ID, title:None, author:None, year:None):
    
    for book in book_library:

        if title is not None:
            book['title'] = title
        if author is not None:
            book['author'] = author
        if year is not None:
            book['year'] = year
        break



import json

def save_to_json("C":"\Users\Nana Boadzi\Desktop\DB PROJECT\bk_management.js"):

    with open(file_path, 'w') as file:
        json.dump(book_library, file, indent=4)

def load_from_json(file_path):
    global book_collection
    with open(file_path, 'r') as file:
        book_library = json.load(file)

