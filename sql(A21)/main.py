import qrcode
import sqlite3

class Store:
    def __init__(self):
        self.load_database()
        self.load_database()
        self.start()

    def load_database(self):
        print("welcome to this store")
        print("Loading...")
        self.conection = sqlite3.connect("database.db")
        self.my_cursor = self.conection.cursor()
        query = "SELECT * FROM products"
        result = self.my_cursor.execute(query)
        self.products = result.fetchall()
        print("Data loaded.")

    def refresh(self):
        self.load_database()

    def start(self):
        while True:
            self.show_menu()
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.add()
            elif choice == 2:
                self.edit()
            elif choice == 3:
                self.remove()
            elif choice == 4:
                self.search()
            elif choice == 5:
                self.show_list()
            elif choice == 6:
                self.buy()
            elif choice == 7:
                self.make_qrcode()
            elif choice == 8:
                exit(0)
            else:
                print("Enter correct choice: ")

    @staticmethod
    def show_menu():
        print("1-Add")
        print("2- Edit")
        print("3- remove")
        print("4-search")
        print("5- show")
        print("6- Buy")
        print("7- QRcode")
        print("8- Exit") # تابعش در خود پایتون هست

    def add(self):
        code = input("enter code:")
        name = input("enter name:")
        price = input("enter price: ")
        count = input("enter count:")
        quary = f"INSERT INTO products('code','name', 'price', 'count') VALUES({code}, '{name}', {price}, {count})"
        self.my_cursor.execute(quary)
        self.conection.commit()
        self.refresh()

    def edit(self):
        code = input("please enter code: ")
        print("Choose one number: ")
        in_choice = int(input("1-Name\t 2- Price\t 3- Count : "))
        new = input("Enter new Name\ count \ Price :")
        
        if in_choice == 1:
            column = 'name'
        elif in_choice == 2:
            column = 'count'
        elif in_choice == 3:
            column = 'price'
        else:
            print("incorrect number. Try again")
        quary = f"UPDATE products SET '{column}' = '{new}' WHERE code = {code}"
        self.my_cursor.execute(quary)
        self.conection.commit()
        self.refresh()
        print("Information update successfully")

    def remove(self):
        code = input("Enter the code: ")
        quary = f"DELETE FROM products WHERE code = '{code}'"
        self.my_cursor.execute(quary)
        self.conection.commit()
        self.refresh()

    def search(self):
        user_input = int(input("Enter code or name :"))
        for product in self.products:
            if product[0] == user_input or product[1] == user_input:
                print("code\tname\tprice\tcount")
                print(f"{product[0]}\t{product[1]}\t{product[2]}\t{product[3]}")
                break

    def show_list(self):
        print("code\tname\tprice\tcount")
        for product in self.products:
            for member in product:
                print(member,end="\t")
            print()

    def buy(self):
        code = 0
        basket = []
        while code != 'end':
            code = input("Enter the code or type end: ")
            if code != 'end':
                for product in self.products:
                    if product[0] == int(code):
                        count = int(input("Enter count of the product: "))
                        if product[3] >= count:
                            quary = f"UPDATE products SET count = {product[3]-count} WHERE code = {int(code)}"
                            self.my_cursor.execute(quary)
                            self.conection.commit()
                            basket.append(product)
                            print("Successfully added to the basket")
                            break
                        else:
                            print("the number that you want isnt exist")
                            break
                else:
                    print("the code not found!")
        total_price = 0
        for product in basket:
            print("name\t price\t count \t total")
            print(product[1],'\t', product[2],'\t', count, '\t', count*int(product[2]))
            total_price = total_price + count*int(product[2])
        print("Total price : ", total_price)
        self.refresh()

    def make_qrcode(self):
        input_code = int(input("Enter the code that you want to make Qr-code for it: "))
        for product in self.products:
            if product[0] == input_code:
                text = f"code: {product[0]} name: {product[1]} price: {product[2]} count: {product[3]}"
                img = qrcode.make(text)
                img.save(str(product[0])+ '.png')
                print("The Qrcode maked successfully")
                break
        else:
            print("The code not found!")

app = Store()
