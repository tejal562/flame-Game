from tkinter import *

def check():
    s1=entry1.get().lower()
    s2=entry2.get().upper()
    s1=s1.replace(" "," ")
    s2=s2.replace(" "," ")

    l1=list(s1)
    l2=list(s2)
    l3=l1+l2

    for i in l3:
       if i in l1 and i in l2:
           l1.remove(i)
           l2.remove(i)

    l3=l1+l2
    a=len(l3)
    l=["Friend","lover","Affection","Marriage","Enemy","Sister","Brother"]

    while len(l)>1:
        if a<len(l):
            l.remove(l[a])
        else:
            b=a%len(l)-1   
            l.remove(l[b])
            l=l[b:]+l[:b]

    entry3.insert(END,l[0])

def clear():
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)

    entry1.focus_set()
    
    

              
                 



if __name__=="__main__":
   root=Tk()
   root.geometry("300x150")
   root.title("flames Game")
   root.configure(bg="Orange")



   label1=Label(root,text="Player 1 name : ",fg="Black",bg="light blue")
   label1.grid(row=1,column=0)
   entry1=Entry(root)
   entry1.grid(row=1,column=1)

   label2=Label(root,text="Player 2 name : ",fg="Black",bg="light blue")
   label2.grid(row=2,column=0)
   entry2=Entry(root)
   entry2.grid(row=2,column=1)

   label3=Label(root,text="Relationship status: ",fg="Black",bg="light blue")
   label3.grid(row=4,column=0)
   entry3=Entry(root)
   entry3.grid(row=4,column=1)


   button1=Button(root,text="Check",fg="black",command=check)
   button1.grid(row=3,column=1)

   button2=Button(root,text="Clear",fg="black",command=clear)
   button2.grid(row=5,column=1)
root.mainloop()
