import json

library = []

# Loading the library
# We are trying to open the JSON file, if there isn't a json file it will return [] an empty table
def load_lib(filename):
    try:
        with open(filename) as file:
            return json.load(file)
    except FileNotFoundError:
        return []

library = load_lib('library.json')
# This is where the magic begins. We are saving the json file each time we add a book. If theres no books that means that aj son file will be created!
def save_lib(library, filename):
    with open(filename, 'w') as file:
        json.dump(library, file, indent=4)

def add_book(title, author):
    library.append({'title': title, 'author': author})
    save_lib(library, 'library.json')
    print(f'{title} has been added to library.')

def remove_book(title):
    global library
    library = [book for book in library if book['title'] != title]
    save_lib(library, 'library.json')
    print(f'{title} has been removed from library.')

def search_book(title):
    results = [book for book in library if title.lower() in book['title'].lower() or title.lower() in book['author'].lower()]
    return results

def list_books():
    if not library:
        print('No books found.')
    else:
        for book in library:
            print(f'\nTitle: {book["title"]}')
            print(f'Author: {book["author"]}')
def main():
    while True:
        print("\n ---/Library\---")
        print("[1]Add a book")
        print("[2]Remove a book")
        print("[3]Search a book")
        print("[4]List books")
        print("[5]Exit")
        print("\n ---------------")
        option = input("Enter your choice: ")

        if option == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            add_book(title, author)
        elif option == '2':
            title = input("Enter book title: ")
            remove_book(title)
        elif option == '3':
            title = input("Enter book title: ")
            results = search_book(title)
            for book in results:
                print(f"\n{book['title']} -- {book['author']}")
        elif option == '4':
            list_books()



if __name__ == '__main__':
    main()