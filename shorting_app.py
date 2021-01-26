from tkinter import*
from tkinter import ttk,filedialog,messagebox
import os,shutil
class Shorting_App:
    def __init__(self,root):
        self.root = root
        self.root.title("Shorting Application | Developed By Mohammad Forhad")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg ="white")
        self.logo_icon = PhotoImage(file="images/folder.png")
        title = Label(self.root,text="File Shorting Application ", font = ("impact",40),bg="#023548",fg="white",anchor="w").place(x=0,y=0,relwidth = 1)


        #=========Section 1================
        self.var_foldername = StringVar()
        lbl_select_folder = Label(self.root,text ="Select Folder",font=("times new roman",25),bg="white").place(x=50,y=100)
        txt_folder_name = Entry(self.root,textvariable=self.var_foldername,font=("times new roman",15),state="readonly",bg="lightyellow").place(x=250,y=100,height=42,width=600)
        btn_browse = Button(self.root,command=self.browse_function,text="BROWSE",bd=4,relief=RAISED,font=("times new roman",15,"bold"),bg="green",fg="white",activebackground="green",cursor="hand2",activeforeground="white").place(x=900,y=95,height=45,width="150")
        hr = Label(self.root,bg="lightgray").place(x=50,y=160,height=2,width=1250)

        #===============================section2===============================
        #=============================All Extentions==================
        self.image_extentions = ["Image Extentions",".png",".jpg",".jpeg",".jfif"]
        self.audio_extentions = ["Audio Extentions",".amr",".mp3"]
        self.video_extentions = ["Video Extentions",".mp4",".avi",".mpeg4",".mkv",".3gp"]
        self.doc_extentions = ["Document Extentions",".doc",".xlsx",".ppt",".pdf",".pptx",".xls",".zip",".rar",".csv",".psd",".ai",".docx",".txt"]
        

        self.folders = {
                    "videos":self.video_extentions,
                    "audios":self.audio_extentions,
                    "images":self.image_extentions,
                    "documents":self.doc_extentions,
                }


        lbl_support_ext = Label(self.root,text ="Various Supported Extentions: ",font=("times new roman",25),bg="white").place(x=50,y=170)
        self.image_box = ttk.Combobox(self.root,values=self.image_extentions,font=("times new roman",15),state="readonly",justify=CENTER)
        self.image_box.place(x=60,y=230,width=270,height=35)
        self.image_box.current(0)



        self.video_box = ttk.Combobox(self.root,values=self.video_extentions,font=("times new roman",15),state="readonly",justify=CENTER)
        self.video_box.place(x=360,y=230,width=270,height=35)
        self.video_box.current(0)


        self.audio_box = ttk.Combobox(self.root,values=self.audio_extentions,font=("times new roman",15),state="readonly",justify=CENTER)
        self.audio_box.place(x=700,y=230,width=270,height=35)
        self.audio_box.current(0)

        self.doc_box = ttk.Combobox(self.root,values=self.doc_extentions,font=("times new roman",15),state="readonly",justify=CENTER)
        self.doc_box.place(x=1010,y=230,width=270,height=35)
        self.doc_box.current(0)

        #===============================section3===============================
        #=============================All ImageIcons==================
        self.image_icon = PhotoImage(file="images/photos.png")
        self.audio_icon = PhotoImage(file="images/audio.png")
        self.video_icon = PhotoImage(file="images/videos.png")
        self.document_icon = PhotoImage(file="images/document.png")
        self.other_icon = PhotoImage(file="images/others.png")


        Frame1 = Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Frame1.place(x=50,y=300,width=1250,height=300)

        self.lbl_total_files = Label(Frame1,text="Total Files : ",font=("times new roman",20),bg="white")
        self.lbl_total_files.place(x=10,y=10)


        self.lbl_total_image = Label(Frame1,bd=3,relief=RAISED,compound=TOP,font=("times new roman",20,"bold"),image = self.image_icon,bg="#087587",fg="white")
        #(,image = self.image_icon) eta hobe oporer lainer total images er pore comma diya 
        self.lbl_total_image.place(x=20,y=60,width=230,height=200)

        self.lbl_total_audio = Label(Frame1,bd=3,relief=RAISED,compound=TOP,font=("times new roman",20,"bold"),image= self.audio_icon,bg="#008Ea4",fg="white")
        #(image= self.audio_icon, eta hobe oporer lainer total audios er pore comma diya)
        self.lbl_total_audio.place(x=260,y=60,width=230,height=200)

        self.lbl_total_video = Label(Frame1,bd=3,relief=RAISED,compound=TOP,font=("times new roman",20,"bold"),image=self.video_icon,bg="#DF002A",fg="white")
        #(image=self.video_icon, eta hobe oporer lainer total videos er pore comma diya)
        self.lbl_total_video.place(x=500,y=60,width=230,height=200)

        self.lbl_total_document = Label(Frame1,bd=3,relief=RAISED,compound=TOP,font=("times new roman",20,"bold"),image=self.document_icon,bg="#008Ea4",fg="white")
        #(image=self.video_icon, eta hobe oporer lainer total videos er pore comma diya)
        self.lbl_total_document.place(x=740,y=60,width=230,height=200)

        self.lbl_total_other = Label(Frame1,bd=3,relief=RAISED,compound=TOP,font=("times new roman",20,"bold"),image=self.other_icon,bg="gray",fg="white")
        #(image=self.video_icon, eta hobe oporer lainer total videos er pore comma diya)
        self.lbl_total_other.place(x=980,y=60,width=230,height=200)

        #===============================section4===============================
        lbl_status = Label(self.root,text ="STATUS",font=("times new roman",20),bg="white").place(x=50,y=620)
        self.lbl_st_total = Label(self.root,text ="",font=("times new roman",18),bg="white",fg="green")
        self.lbl_st_total.place(x=300,y=620)

        self.lbl_st_moved = Label(self.root,text ="",font=("times new roman",18),bg="white",fg="blue")
        self.lbl_st_moved.place(x=500,y=620)

        self.lbl_st_left = Label(self.root,text ="",font=("times new roman",18),bg="white",fg="orange")
        self.lbl_st_left.place(x=700,y=620)


        #===================Buttons===============
        self.btn_clear = Button(self.root,command=self.clear,text="CLEAR",font=("times new roman",15,"bold"),bg="#607d8b",fg="white",activebackground="#607d8b",cursor="hand2",activeforeground="white")
        self.btn_clear.place(x=880,y=610,height=50,width="180")

        self.btn_start = Button(self.root,state=NORMAL,command=self.start_function,text="START",font=("times new roman",15,"bold"),bg="#ff5722",fg="white",activebackground="#ff5722",cursor="hand2",activeforeground="white")
        self.btn_start.place(x=1100,y=610,height=50,width="180")

    def Total_count(self):
        images = 0
        audios = 0
        videos = 0
        documents = 0
        others = 0
        self.count = 0
        cmbine_list =[]
        for i in self.all_files:
            if os.path.isfile(os.path.join(self.directry,i)) == True:
                self.count+=1
                ext = "."+i.split(".")[-1]
                for folder_name in self.folders.items():
                    #print(folder_name)
                    for x in folder_name[1]:
                        cmbine_list.append(x)
                    if ext.lower() in folder_name[1] and folder_name[0] == "images":
                        images+=1
                    if ext.lower() in folder_name[1] and folder_name[0] == "audios":
                        audios+=1
                    if ext.lower() in folder_name[1] and folder_name[0] == "videos":
                        videos+=1
                    if ext.lower() in folder_name[1] and folder_name[0] == "documents":
                        documents+=1
# this is for other files only 
        for i in self.all_files:
            if os.path.isfile(os.path.join(self.directry,i)) == True:
                ext = "."+i.split(".")[-1]
                if ext.lower() not in cmbine_list:
                    others+=1

        self.lbl_total_image.config(text="Total Images\n"+str(images))
        self.lbl_total_video.config(text="Total Videos\n"+str(videos))
        self.lbl_total_audio.config(text="Total Audios\n"+str(audios))
        self.lbl_total_document.config(text="Total Documents\n"+str(documents))
        self.lbl_total_other.config(text="Other files\n"+str(others))
        self.lbl_total_files.config(text="Total Files : "+str(self.count))

        #==================this is for others files===============================


        self.lbl_total_image.config(text="Total Images\n"+str(images))
        self.lbl_total_video.config(text="Total Videos\n"+str(videos))
        self.lbl_total_audio.config(text="Total Audios\n"+str(audios))
        self.lbl_total_document.config(text="Total Documents\n"+str(documents))
        self.lbl_total_other.config(text="Other Files\n"+str(others))
        self.lbl_total_files.config(text="Total Files: "+str(self.count))
           


    def browse_function(self):
        op = filedialog.askdirectory(title="SELECT FOLDER FOR SHORTING")
        if op!= None:
            #print(op)
            self.var_foldername.set(str(op))
            self.directry = self.var_foldername.get()
            self.other_name = "others" #input("Enter The Folder name for Unknown Files : ")
            self.rename_folder()
            self.all_files = os.listdir(self.directry)
            length = len(self.all_files)
            count = 1
            self.Total_count()
            self.btn_start.config(state=NORMAL)
            # # print(self.all_files)
            

    def start_function(self):
        if self.var_foldername.get() != "":
            self.btn_clear.config(state=DISABLED)
            c = 0
            for i in self.all_files:
                if os.path.isfile(os.path.join(self.directry,i)) == True:
                    c+=1
                    self.create_move(i.split(".")[-1],i)
                    self.lbl_st_total.config(text="TOTAL: "+str(self.count))
                    self.lbl_st_moved.config(text="MOVED: "+str(c))
                    self.lbl_st_left.config(text="LEFT: "+str(self.count - c))
                     
                    self.lbl_st_total.update()
                    self.lbl_st_moved.update()
                    self.lbl_st_left.update()
                    


            messagebox.showinfo("Success","All Files Has Moved Successfully")
            self.btn_start.config(state=NORMAL)
            self.btn_clear.config(state=NORMAL)
        else:
            messagebox.showerror("Error","Please Select Folder")

    def clear(self):
        self.btn_start.config(state=DISABLED)
        self.var_foldername.set("")
        self.lbl_st_total.config(text="")
        self.lbl_st_moved.config(text="")
        self.lbl_st_left.config(text="")
        self.lbl_total_image.config(text="")
        self.lbl_total_video.config(text="")
        self.lbl_total_audio.config(text="")
        self.lbl_total_document.config(text="")
        self.lbl_total_other.config(text="")
        self.lbl_total_files.config(text="Total Files : ")



        
    def rename_folder(self):
        for folder in os.listdir(self.directry):
            if os.path.isdir(os.path.join(self.directry,folder)) == True:
                os.rename(os.path.join(self.directry,folder),os.path.join(self.directry,folder.lower()))

    def create_move(self,ext,file_name):
        find = False
        for folder_name in self.folders:
            if "."+ext in self.folders[folder_name]:
                if folder_name not in os.listdir(self.directry):
                    os.mkdir(os.path.join(self.directry,folder_name))
                shutil.move(os.path.join(self.directry,file_name),os.path.join(self.directry,folder_name))
                find = True
                break 
        if find!= True:
            if self.other_name not in os.listdir(self.directry):
                os.mkdir(os.path.join(self.directry,self.other_name))
            shutil.move(os.path.join(self.directry,file_name),os.path.join(self.directry,self.other_name))
        



root = Tk()
obj = Shorting_App(root)
root.mainloop()