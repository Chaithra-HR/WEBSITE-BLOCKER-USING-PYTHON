from tkinter import * 
root = Tk() 
root.geometry('500x300') 
root.resizable(0,0) 
root.title("Website Blocker") 
Label(root, text ='Website Blocker' ,font ='arial 20 bold').pack() 
host_path ='C:\Windows\System32\drivers\etc\hosts' 
host ='C:\Windows\System32\drivers\etc\host' 
ip_address = '127.0.0.1' 
Label(root, text ='Enter Website :' , font ='arial 13 bold').place(x=5 ,y=60) 
Websites = Text(root,font = 'arial 10',height='2', width = '40') 
Websites.place(x= 140,y = 60) 
def remove():
    website_lists = Websites.get(1.0,END)
    Website = list(website_lists.split(","))
    with open (host_path , 'r+') as host_file:
        file_content = host_file.read()
        for web in Website:             
            if web in file_content:                 
                h=open ("host","r")                 
                k=open("hosts","w") 
                k.write("") 
                k.close()                 
                for l in h:                      
                    f=open ("hosts","a") 
                    f.write(l) 
                    f.close() 
                    Label(root, text = '   unblocked         ' , font = 'arial 12 bold').place(x=190,y=200)                
                    pass 
def Blocker(): 
    website_lists = Websites.get(1.0,END)     
    Website = list(website_lists.split(","))     
    with open (host_path , 'r+') as host_file: 
        file_content = host_file.read()         
        for web in Website: 
            if web in file_content: 
                Label(root, text = 'Already Blocked' , font = 'arial 12 bold').place(x=195,y=200)                 
                pass             
            else: 
                host_file.write(ip_address + " " + web + '\n') 
                Label(root, text = "    Blocked           ", font = 'arial 12 bold').place(x=198,y =200)

unblock = Button(root, text = 'unblock',font = 'arial 12 bold',pady = 5,command = remove ,width = 6, bg = 'royal blue1', activebackground = 'sky blue') 
unblock.place(x = 250, y = 150) 
block = Button(root, text = 'Block',font = 'arial 12 bold',pady = 5,command = Blocker ,width = 6, bg = 'royal blue1', activebackground = 'sky blue')
block.place(x = 180, y = 150) 
root.mainloop() 
