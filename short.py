import os,shutil
folders = {
    "videos":[".mp4",".mkv"],
    "audios":[".wav",".mp3"],
    "images":[".jpg",".jpeg",".png"],
    "documents":[".doc",".docx",".xlsx",".xls",".pdf",".zip",".rar"],
    "software":[".exe"]
}
# print(folders)
# for folder_name in folders:
#     print(folder_name,folders[folder_name])
def rename_folder():
    for folder in os.listdir(directry):
        if os.path.isdir(os.path.join(directry,folder)) == True:
            os.rename(os.path.join(directry,folder),os.path.join(directry,folder.lower()))

def create_move(ext,file_name):
    find = False
    for folder_name in folders:
        if "."+ext in folders[folder_name]:
            if folder_name not in os.listdir(directry):
                os.mkdir(os.path.join(directry,folder_name))
            shutil.move(os.path.join(directry,file_name),os.path.join(directry,folder_name))
            find = True
            break 
    if find!= True:
        if other_name not in os.listdir(directry):
            os.mkdir(os.path.join(directry,other_name))
        shutil.move(os.path.join(directry,file_name),os.path.join(directry,other_name))


directry = input("Enter The Location : ")
other_name = input("Enter The Folder name for Unknown Files : ")
rename_folder()
all_files = os.listdir(directry)
length = len(all_files)
count = 1
# print(all_files)
for i in all_files:
    if os.path.isfile(os.path.join(directry,i)) == True:
        create_move(i.split(".")[-1],i)
    print(f"Total Files: {length} | Done: {count} | Left: {length-count}")
    count+=1
