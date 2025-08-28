from media import Media
from film import Film
from series import Series
from documentary import Documentary
from clip import Clip
from actor import Actor
MEDIA = []

def read_from_database():
    f= open("database.txt","r")
    for line in f:
        line = line.rstrip('\n')
        result = line.split(",")
        cast_1 = Actor(result[6])
        cast_2 = Actor(result[7])
        casts = [cast_1, cast_2]
        if result[0] == "film":
            my_obj = Film(result[1], result[2], result[3], result[4], result[5], casts)
        elif result[0] == "series":
            my_obj = Series(result[1], result[2], result[3], result[4], result[5], casts, result[8])
        elif result[0] == "documentary":
            my_obj = Documentary(result[1], result[2], result[3], result[4], result[5], casts )
        elif result[0] == "clip":
            my_obj = Clip(result[1], result[2], result[3], result[4], result[5], casts )
        MEDIA.append(my_obj) 
    f.close()

def write_to_database():
    f = open("database.txt","w")
    for line in MEDIA:
        if type(line) == Film:
            f.write("film,")
        elif type(line) == Series:
            f.write("series,")
        elif type(line) == Documentary:
            f.write("documentary,")
        elif type(line) == Clip:
            f.write("clip,")
        f.write(line.name + ",")
        f.write(line.director + ",")
        f.write(line.IMDB + ",")
        f.write(line.duration + ",")
        f.write(line.url + ",")
        f.write(line.casts[0].name +",")
        f.write(line.casts[1].name+",")
        if type(line) == Series:
            f.write(","+ line.episode )
        f.write("\n")
    f.close()


def show_menu():
    print("1- Add")
    print("2- Edit")
    print("3- Remove")
    print("4- Search")
    print("5- Show list")
    print("6- Download")
    print("7- Exit")

def search():
    choice = int(input("1- based on some information of movie 2- Based on the duration of movie \n Enter your choice : "))
    if choice == 1:
        key_word = input("Enter the name or the director : ")
        for media in MEDIA:
            if key_word.lower() in [media.name.lower(), media.director.lower()]:
                print("type \t\t name \t\t director \t IMDB \t\t duration \t casts \t\t episod")
                media.showinfo()
                break
        else:
            print("Not found")
    elif choice == 2:
        found = False
        min_time = int(input("Enter minimum duration of the movei: "))
        max_time = int(input("Enter maximum duration of the movie: "))
        print("type \t\t name \t\t director \t IMDB \t\t duration \t casts \t\t episod")
        for media in MEDIA:
            if min_time <= int(media.duration) <= max_time:
                found = True
                media.showinfo()
        if not found:
            print("Not found")
    else:
        print("Invalid input")
        
print("welcome to this store")
print("Loading...")
read_from_database()
print("Data loaded.")

while True:
    show_menu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        media_type = int(input("Enter type of media:\n 1- Film, 2- series, 3- Documentary, 4- Clip : "))
        if media_type in [1,2,3,4]:
            result = Media.add()
            casts = [Actor(result[5]), Actor(result[6])]
            if media_type == 1:
                media = Film(result[0],result[1],result[2],result[3],result[4],casts)
            elif media_type == 2:
                episode = input("Enter number of episods: ")
                media = Series(result[0],result[1],result[2],result[3],result[4],casts, episode)
            elif media_type == 3:
                media = Documentary(result[0],result[1],result[2],result[3],result[4],casts)
            elif media_type == 4:
                media = Clip(result[0],result[1],result[2],result[3],result[4],casts)
            MEDIA.append(media)
        else :
            print("incorrect number")

    elif choice == 2:
        input_movie = input("Enter the name of film that you want to correct: ")
        for media in MEDIA:
            if input_movie.lower() == media.name.lower():
                media.edit()
                break
        else:
            ("Input not found")
        
    elif choice == 3:
        input_movie = input("Enter the name of film you want to remove : ")
        for media in MEDIA:
            if media.name.lower() == input_movie.lower():
                media.remove(MEDIA)
                print("removed successfully")
                break
        else:
            print("Not found")
    elif choice == 4:
        search()
        
    elif choice == 5:
        print("type \t\t name \t\t director \t IMDB \t\t duration \t casts \t\t episod")
        for media in MEDIA:
            media.showinfo()

    elif choice == 6:
        input_movie = input("Enter the name of film for download : ")
        for media in MEDIA:
            if input_movie.lower() == media.name.lower():
                media.download()
                break
        else:
            print("Not found")
    
    elif choice == 7:
        write_to_database()
        exit(0)
    else:
        print("Enter correct choice: ") 


