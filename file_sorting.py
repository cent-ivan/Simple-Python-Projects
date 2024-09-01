import os 
import shutil
import time

filename = {
    "jpg":"Pictures", #filename type : folder to put in
    "png":"Pictures",

    "mp3":"Musics",
    "mp4":"Videos",

    "txt":"Documents",
    "pdf":"Documents",
    "docx":"Word Files",
    "pptx":"Powerpoints"
}


def create_folder():
    for folder in filename.values():
        if folder in os.listdir(): 
            continue
        else:
            path  =  os.getcwd() + f"\\{folder}" #gets the current word directory and adds the folder name
            os.mkdir(path)
    print("All folders created")
    main()


def add_file(key):
    dst =  os.getcwd() + f"\\{filename[key]}" #get the target path of where the file will move
    for content in os.listdir():
        split_content = content.split(".") #turns into list, divides the filename and extension

        if split_content[-1] == key: #checks the extension if it is in the right directory
            file  = ".".join(split_content)
            src  =  os.getcwd() + f"\\{file}" #gets the file to be moved
            shutil.move(src, dst)

    

def main(): #controls the flow of the program
    start_time  =  time.time()
    for key in filename:
        if filename[key] not in os.listdir():
            create_folder()
        else:   
            add_file(key)

    end_time = time.time()
    print(end_time -  start_time) #calculate run time

#user entered path here
path = input("Enter path: ")

if path == "":
    print("No entered path")
else:
    os.chdir(path) #changed the path
    main()







# source = r"C:/Users/user/Desktop/TestFolder/Revert Virus.png" 
# dst = r"C:/Users/user/Desktop/folder"


#shutil.copy(source, dst, follow_symlinks= True) <- Copy data and mode bits  a file between folders
#shutil.copy2(source, dst) <- Copy data and metadata
#shutil.move(source, dst) <- Moves/cut file between folders

# for i, j in enumerate(os.scandir()): <- if you also want to get file and directory properties such as file size and modification date.
#      print(i, j) 