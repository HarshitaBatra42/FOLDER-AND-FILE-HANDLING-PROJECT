from pathlib import Path
import os
import shutil
def create_folder():
    try:
        folder_name=input("Enter folder name to create:")
        p=Path(folder_name)
        p.mkdir()  #make directory as it creates a folder
        print("folder created successfully")
    except Exception as e:
        print("sorry an error occured as {err}")



def read_file_folder():
    p=Path("")
    items=list(p.rglob('*'))  #rglob is used to read all files and folders recursively * measn match everything
    for i,v in enumerate(items):  #enumerate is used to get index along with value
        print(f"{i+1} : {v}")


def update_folder():
    try:
        read_file_folder
        old=input("Enter folder name to update:")
        p=Path(old)
        if p.exists() and p.is_dir():
            new=input("Enter new folder name:")
            p.rename(new)
            print("folder updated successfully")
        else:
            print("folder does not exist")
    except Exception as e:
        print(f"sorry an error occured as {e}")


def delete_folder():
    try:
        read_file_folder()
        folder_name=input("Enter folder name to delete:")
        p=Path(folder_name)
        if p.exists() and p.is_dir():
            shutil.rmtree(p) #shutil.rmtree is used to remove directory along with all its contents
            print("folder deleted successfully")
        else:
            print("folder does not exist")
    except Exception as e:
        print(f"sorry an error occured as {e}")


def create_file():
    try:
        read_file_folder()
        file_name=input("Enter file name to create:")
        p=Path(file_name)
        if not p.exists():
            with open(file_name,"w") as fs:
                data=input("Enter data to write in file:")
                fs.write(data)
            print("file created successfully")
        else:
            print("file already exists")
    except Exception as e:
        print(f"sorry an error occured as {e}")

def read_file():
    try:
        read_file_folder()
        file_name=input("Enter file name to read:")
        p=Path(file_name)
        if p.exists() and p.is_file():
            with open(file_name,"r") as fs:
                data=fs.read()
                print("file content is:")
                print(data)
        else:
            print("file does not exist")
    except Exception as e:
        print(f"sorry an error occured as {e}")

def update_file():
    try:
        read_file_folder()
        file_name=input("Enter file name to update:")
        p=Path(file_name)
        if p.exists() and p.is_file():
            print("Options-")
            print("1. Rename the file")
            print("2.For appending data to the file")
            print("3. For overwriting the file content")
            choice=int(input("Enter your choice:"))
            if choice==1:
                new_name=input("Enter new file name:")
                new_p=Path(new_name)
                if not new_p.exists():
                    p.rename(new_name)
                    print("file renamed successfully")
                else:
                    print("file with new name already exists")

            if choice==2:
                with open(file_name,"a") as fs:
                    data=input("Enter data to append to the file:")
                    fs.write(" "+data)
                print("file updated successfully")
            
            if choice==3:
                with open(file_name,"w") as fs:
                    data=input("Enter new data to write in the file:")
                    fs.write(data)
                print("file content overwritten successfully")
    except Exception as e:
        print(f"sorry an error occured as {e}")


def delete_file():
    try:
        read_file_folder()
        name=input("Enter file name to delete with extensions: ")
        p=Path(name)
        if p.exists() and p.is_file():
            p.unlink()  #unlink is used to delete a file
            print("file deleted successfully")
        else:
            print("file does not exist")
    except Exception as e:
        print(f"sorry an error occured as {e}")


print("Options -")
print("1. Create a new file")
print("2. Read files and folder")
print("3. update to a folder")
print("4. Delete a folder")
print("5.Create a file")
print("6.Read a file")
print("7.Update a file")
print("8 Delete a file")

choice=int(input("Enter your choice:"))


if choice==1:
    create_folder()

if choice==2:
    read_file_folder()


if choice==3:
    update_folder()

if choice==4:
    delete_folder()

if choice==5:
    create_file()

if choice==6:
    read_file()

if choice==7:
    update_file()


if choice==8:
    delete_file()