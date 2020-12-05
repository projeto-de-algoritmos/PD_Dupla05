import tkinter as tk
import glob
import time

root = tk.Tk()
root.title("Sprites Pair Sequence")
root.geometry("400x400")
lst = tk.Listbox(root)
lab = tk.Label(root, text="hello")

i = 1
def showimg(e):
    global i, root
    #print("ok")
    while True:
        try:
            global root, lst, lab
            n = lst.curselection()
            fname = lst.get(n)
            img = tk.PhotoImage(file=fname, format = "gif -index " + str(i))
            lab.configure(image=img)
            lab.image = img
            i+=1
            time.sleep(0.15)
            root.update()
        except:
            i = 0    
    print(fname)        

def screen(arr): 
    global root, lst, lab
    print("entrou")
    lst.pack(side="right", fill=tk.Y, expand=1)
    #namelist = [i for i in glob.glob("img/character/*.gif")]
    #print (namelist)
    namelist = arr
    gifs =[]


    for fname in namelist:
        gifs.append(fname)
        lst.insert(tk.END, fname)



    lst.bind("<<ListboxSelect>>", showimg)
    img = tk.PhotoImage(file=gifs[0])
    lab = tk.Label(root, text="hello", image=img)
    lab.pack(side="left")

    root.mainloop()