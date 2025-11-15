#Instagram new followers finder
import instaloader
import getpass

f = open("followers.txt","r")
old_followers = []
for old_follower in f:
    old_followers.append(old_follower)
f.close()

L = instaloader.Instaloader()
username = input("Enter username: ")
password = getpass.getpass("Enter password: ")
L.login(username, password)
print("You can login sucessfully!")

profile = instaloader.Profile.from_username(L.context, "am_ne.ahani")

new_followers = []
for follower in profile.get_followers():
    new_followers.append(follower)

for follower in new_followers:
    if follower in old_followers:
        print(follower)
f = open("followes.txt","w")
for follower in new_followers:
    f.write(follower,"\n")
f.close()



