from media import Media
from actor import Actor
class Series(Media):
    def __init__(self, n, di, I, u, du, c, episode):
        super().__init__( n, di, I, u, du, c)
        self.episode = episode

    def showinfo(self):
        casts = self.casts[0].name + "," + self.casts[1].name
        row = [type(self).__name__, self.name, self.director, self.IMDB, self.duration, casts, self.episode]
        col_width = 17
        for item in row:
            print(f"{item:<{col_width}}", end="")
        print()
    
    def edit(self):
        choice = int(input("1- name, 2- director, 3- IMDB, 4- url, 5- duration, 6- casts 7- episod \n enter choice : "))
        correct_choice = True
        if choice == 1:
            new_name = input("Enter new name: ")
            self.name = new_name
        elif choice == 2:
            new_director = input("Enter new director : ")
            self.director = new_director
        elif choice == 3:
            new_IMDB = input("Enter new IMDB : ")
            self.IMDB = new_IMDB
        elif choice == 4:
            new_url = input("Enter new url : ")
            self.url = new_url
        elif choice == 5:
            new_duration = input("Enter new duration: ")
            self.duration = new_duration
        elif choice == 6:
            new_cast_1 = input("Enter new first cast: ")
            new_cast_2 = input("Enter new second cast: ")
            self.casts = [Actor(new_cast_1), Actor(new_cast_2)]
        elif choice == 7:
            new_episode = input("Enter new episod: ")
            self.episode = new_episode
        else:
            correct_choice = False
            print("Invalid input")
        if correct_choice:
            print("data edit successfully")

    