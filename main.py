import song_lister
import song_downloader
import os

def handle_download():
    print("Enter how many songs you want to download from your liked songs?: ")
    number=int(input("press enter if you want to download all, else type number:"))


    if song_downloader.fun2(number) !=-1:
        print("Success")
    else:
        print("fail")


if os.path.getsize('output_links.txt') == 0:
    song_lister.fun1()
else:
    print("Already there files in the queue to download.")
    print("You want to continue with the previous list of yours [press 1]")
    print("or you want to fetch the recent list of yours liked songs [press 2]:")
    num=int(input())
    if(num==1):
        handle_download()
    elif(num==2):
        with open('output_links.txt', 'w') as file:
            pass
        song_lister.fun1()
        handle_download()
