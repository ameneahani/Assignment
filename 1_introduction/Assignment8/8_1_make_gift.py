import os
import imageio

file_list =sorted(os.listdir("image")) # اگر سورت نکنیم فایل ها را رندوم باز میکند
IMAGES = []
for file_name in file_list:
    file_path = "image/" + file_name # مسیر عکس ها 
    image = imageio.imread(file_path) #عکس ها را باز میکند و میخواند و در متغیر ذخیره میکند 
    IMAGES.append(image)
    # print(IMAGES)

imageio.mimsave("output.gif", IMAGES, duration=0.2)


