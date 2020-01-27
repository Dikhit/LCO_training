import requests as rq

def image_downloader(url,file_path, file_name):
    try:
        data = rq.get(url)
        file_name = file_name+".jpg"

        with open(file_name, "wb") as file:
            file.write(data)
    except:
        return "Something went wrong!!"
def main():
    url = input("Enter the url : ")
    file_name = input("Enter the file name to save as : ")

    image_downloader(url,'images/',file_name)

if __name__ == '__main__' : main()

