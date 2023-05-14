import csv
from flask import Flask, render_template, request
import json

app = Flask(__name__)



class User:
    def __init__(self, user, province, contributions, stars, followers):
        self.user = user
        self.province = province
        self.contributions = contributions
        self.stars = stars
        self.followers = followers


class Book:
    def __init__(self, Title, Author, Genre, Height, Publisher, available):
        self.Title = Title
        self.Author = Author
        self.Genre = Genre
        self.Height = Height
        self.Publisher = Publisher
        self.available = available






def showAllUsers(path):
    with open(path, 'r') as p:
        users = []
        data = csv.DictReader(p)
        for i in data:
            users.append(i)
    return users
users = showAllUsers('users.csv')

def showAllBoooks(path):
    with open(path, 'r') as p:
        books = []
        data = csv.DictReader(p)
        for i in data:
            books.append(i)
    return books
books = showAllBoooks('books.csv')


def addBook(Title, Author, Genre, Height, Publisher, avalable):
    with open('books.csv', 'a', newline='') as p:
        k = ["Title", "Author", "Genre", "Height", "Publisher"]
        writer = csv.DictWriter(p, k)
        if p.tell() == 0:
            writer.writeheader()
        writer.writerow({'Title': Title, 'Author': Author, 'Genre': Genre, 'Height': Height, 'Publisher': Publisher})
# addBook('ali', 'opp', 100, 40, 8)
def addUser(user, province, contributions, stars, followers, available):
    with open('users.csv', 'a', newline='')as p:
        k = ["user", "province", "contributions", "stars", "followers"]
        writer = csv.DictWriter(p, k)
        if p.tell() == 0:
            writer.writeheader()
        writer.writerow({"user": user, "province": province, "contributions": contributions, "stars": stars, "followers": followers, "available": available})
# addUser("www", "ooo", 100, 40, 8)

def findBooksByHeight(height):
    mak = []
    for i in books:
        if int(i['Height']) == height:
            mak.append(i)
    print(mak)
    return mak
# findBooksByHeight(228)

def findBookByTitle(title):
    mak = []
    for i in books:
        if i['Title'] == title:
            mak.append(i)
    print(mak)
    return mak
# findBookByTitle('Nature of Statistical Learning Theory, The')

def findBookByAuthor(author):
    mak = []
    for i in books:
        if i['Author'] == author:
            mak.append(i)
    print(mak)
    return mak
# findBookByAuthor('opp')


def checkBookAvailable(nameBook):
    for i in books:
        if i['title'] == nameBook:
            if not i['available']:
                print("this book is not available :)")
            else:
                print("OK! you can take the book")
                i['available'] = False
                with open('books.js', 'w') as p:
                    json.dump(books, p)
                    with open('books.js', 'r') as p:
                        print(p.read())
# checkBookAvailable("Harry Potter")

def returnBook(nameBook):
        for i in books:
            if i['title'] == nameBook and i['available'] == False:
                i['available'] = True
                with open("books.js", "w") as p:
                    json.dump(books, p)
                    with open("books.js", "r") as p:
                        print(p.read())
# returnBook("Anna Karenina")



@app.route('/ContactUs')
def ContactUs():
    return "0548482433.23tmurot24@gmail.com"

@app.route('/searchBook', methods=['post'])# להזין ספר לפי שם ולהדפיס אותו אם הוא קיים
def searchBook():
    searchBook = request.form['searchBook']
    for i in books:
        if i['Title'] == searchBook:
            return i
    return "this book is not exist"

@app.route('/login', methods=['post'])
def login():
    login = request.form['login']
    print(login)
    print(users)
    for i in users:
        if i['user'] == login:
            return f"welcome back {i}"
    return "you not heve login"


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)