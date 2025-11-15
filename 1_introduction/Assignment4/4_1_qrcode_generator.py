# making qrcode of name and mobile number
import qrcode

name = input("Please enter your name: ")
mobile_number = input("Please enter your mibilenumber: ")

img = qrcode.make(name + mobile_number)
img.save("name and mobile_qrcode.png")

