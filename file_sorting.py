import os
import shutil


filename = {
    "jpg":"Pictures",
    "png":"Pictures",

    "mp3":"Music",
    "mp4":"Videos",

    "txt":"Documents",
    "doc":"Word Files",
    "docx":"Word Files",
    "pptx":"Powerpoint FIles"
}
#main

def addFile(key):
    dst = os.getcwd() + f"\{filename[key]}"

    for content in os.listdir():
        split = content.split(".")  #split until to the filename, gets the filename

        if key == split[-1]:        
            file = ".".join(split)  #completely joins the file name and the extension
            source = os.getcwd() + f"\{file}"  
            shutil.move(source, dst)


def createFolder(key):
    os.mkdir(os.getcwd() + f"\{filename[key]}")
    addFile(key)

#first to execute
def run():
    for key in filename:
        if filename[key] in os.listdir(currentDir):
            addFile(key)            #if the folder exist, calls the add function
        else:
            createFolder(key)       #if the folder does not exist, it calls the create function

        
link_path = input("Enter path: ")
path = link_path.strip('"')

if path == "":
    print("No entered value")
else:
    currentDir = os.chdir(path)
    run()

# source = r"C:/Users/user/Desktop/TestFolder/Revert Virus.png" 
# dst = r"C:/Users/user/Desktop/folder"


# shutil.move(source, dst)
#shutil.copy(source, dst, follow_symlinks= True) <- Copy data and mode bits  a file between folders
#shutil.copy2(source, dst) <- Copy data and metadata
#shutil.move(source, dst) <- Moves/cut file between folders

# for i, j in enumerate(os.scandir()): <- if you also want to get file and directory properties such as file size and modification date.
#      print(i, j) 