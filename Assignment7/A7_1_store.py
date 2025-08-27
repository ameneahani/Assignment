import qrcode
PRODUCTS = [] # یه لیست خیلی بزرگه که قراره همه کالا ها توش ثبت بشه


def read_form_database():
    f= open("database.txt","r")
    for line in f:
        result = line.split(",")
        my_dict = {"code": result[0], "name": result[1], "price": result[2], "count": result[3]}
        PRODUCTS.append(my_dict) #اطلاعات از توی فایل خونده میشه وبه صورت دبکشنری درمیاد و در لیستی از دیکشتری ها ذخیره میشه
    f.close()

def write_to_database():
    f = open("database.txt","w")
    for line in PRODUCTS:
        f.write(line['code']+',')
        f.write(line['name']+',')
        f.write(line['price']+',')
        f.write(line['count'])
    f.close()

def show_menu():
    print("1-Add")
    print("2- Edit")
    print("3- remove")
    print("4-search")
    print("5- show")
    print("6- Buy")
    print("7- QRcode")
    print("8- Exit") # تابعش در خود پایتون هست


def add():
    code = input("enter code:")
    name = input("enter name:")
    price = input("enter price: ")
    count = input("enter count:")
    new_product = {'code': code, 'name': name, 'price': price, 'count': count + '\n'} #\n به این دلیل است که در فایل نوشتاری برود خط جدید
    PRODUCTS.append(new_product)

def edit():
    code = input("please enter code: ")
    print("Choose one number: ")
    in_choice = int(input("1-Name\t 2- Price\t 3- Count : "))
    new = input("Enter new Name\ count \ Price :")
    for product in PRODUCTS:
        if product['code'] == code:
            if in_choice == 1:
                product['name'] = new
            elif in_choice == 2:
                product['count'] = new
            elif in_choice == 3:
                product['price'] = new
            else:
                print("incorrect number. Try again")
                break
            print("Information update successfully")
            break
    else:
        print("The code not found")


def remove():
    code = input("Enter the code: ")
    i = 0
    for product in PRODUCTS:
        if product['code'] == code:
            PRODUCTS.pop(i)
            print("Update successfully")
            break
        i += 1
    else:
        print("The code not found")

def search():
    user_input = input("Enter code or name :")
    for product in PRODUCTS:
        if product["code"] == user_input or product["name"] == user_input:
            print(product["code"],"\t",product["name"],"\t",product["price"])
            break
    else:
        print("not found")


def show_list():
    print("code\tname\tprice\tcount")
    for product in PRODUCTS:
        print(product["code"],"\t",product["name"],"\t",product["price"])
        

def buy():
    code = 0
    basket = []
    while code != 'end':
        code = input("Enter the code or type end: ")
        if code != 'end':
            for product in PRODUCTS:
                if product['code'] == code:
                    count = int(input("Enter count of the product: "))
                    product['count']=int(product['count'])
                    if product['count'] >= count:
                        product['count'] = str(product['count'] - count) + '\n'
                        my_dict = {'name':product['name'], 'price':product['price'], 'count':count}
                        basket.append(my_dict)
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
        print(product['name'],'\t', product['price'],'\t', product['count'], '\t', count*int(product['price']))
        total_price = total_price + count*int(product['price'])
    print("Total price : ", total_price)
    

def make_qrcode():
    code = input("Enter the code that you want to make Qr-code for it: ")
    for product in PRODUCTS:
        if product['code'] == code:
            img = qrcode.make('code:'+ product['code']+ 'name:'+ product['name'] +'price:'+ product['price'] +'count:'+ product['count'])
            img.save(product['code']+ '.png')
            print("The Qrcode maked successfully")
            break
    else:
        print("The code not found!")

print("welcome to this store")
print("Loading...")
print("Data loaded.")
read_form_database()

while True:
    show_menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        add()
    elif choice == 2:
        edit()
    elif choice == 3:
        remove()
    elif choice == 4:
        search()
    elif choice == 5:
        show_list()
    elif choice == 6:
        buy()
    elif choice == 7:
        make_qrcode()
    elif choice == 8:
        write_to_database()
        exit(0)
    else:
        print("Enter correct choice: ")


