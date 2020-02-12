import os
def image_captured():
    path = 'C:\\Users\\Katlic\\Documents\\LCO_Bootcamp\\LCO_class_assign_prac\\PracticeFolder'
    img_Extension = ['.png', '.jpg', '.jpeg']
#     os.chdir(path)
    list_of_images = []
    for file in os.listdir():
        file_name, file_extention =  os.path.splitext(file)
        if file_extention in img_Extension:
            img = file_name + file_extention
            list_of_images.append(img)
    return list_of_images


image_captured()