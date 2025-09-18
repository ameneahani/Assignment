import sqlite3
def show_menu():
    print("1- show list")
    print("2- add new")
    print("3- edit")
    print("4- remove")

def load_database():
    global con
    global my_cursor
    con = sqlite3.connect("chinook.db")
    my_cursor = con.cursor()

def show_list():
    # for data in my_cursor.execute("SELECT * FROM customers WHERE country = 'France'"):
    #     print(data)

    result = my_cursor.execute("SELECT * FROM genres")
    customers_Germany = result.fetchall()
    print(customers_Germany)
    for moshtari in customers_Germany:
        print(moshtari)

def add_new():
    new_genre_name = input("ENter a name for your new genre")
    my_cursor.execute(f"INSERT INTO genres(GenreId, Name) VALUES ({new_genre_name})")
    con.commit()

def edit():
    new_city = input("Enter the city")
    new_country = input("Enter the name of the country")
    my_cursor.execute(f"UPDATE customers SET Country = '{new_country}', City = '{new_city}' WHERE firstName = 'Helena' AND CustomerId = 6 ")
    con.commit()

def remove():
    gener_name = input("ENter the name for remove")
    my_cursor.execute(f"DELETE FROM artists WHERE Name ='{gener_name}'")
    con.commit()

load_database()
while True:
    show_menu()
    choice = int(input())

    if choice == 1:
        show_list()
    if choice == 2:
        add_new()
    if choice == 3:
        edit()
    if choice == 4:
        remove()
