from tkinter import *
import random
import tkinter.messagebox

class Number_Guessing:
    def __init__(self,root):
        self.root=root
        self.root.title("Number Guessing")
        self.root.geometry("500x350")
        self.root.iconbitmap("logo1064.ico")
        self.root.resizable(0,0)


        answer=StringVar()
        


        def on_enter1(e):
            but_guess['background']="black"
            but_guess['foreground']="cyan"
  
        def on_leave1(e):
            but_guess['background']="SystemButtonFace"
            but_guess['foreground']="SystemButtonText"

        def on_enter2(e):
            but_change['background']="black"
            but_change['foreground']="cyan"
  
        def on_leave2(e):
            but_change['background']="SystemButtonFace"
            but_change['foreground']="SystemButtonText"

        def on_enter3(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"
  
        def on_leave3(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"





        
        def change():
            global actual_number
            but_guess.config(state="normal")
            number=random.randint(2,101)
            start_number=number-1
            actual_number=number+5
            end_number=number+10
            lab_hint.config(text=f"The number is between range {start_number} to {end_number}")
            #print(actual_number)

            #print(number,start_number,end_number,actual_guess_number)

        def clear():
            lab_hint.config(text="Please Select Change Number to start")
            answer.set("")
            but_guess.config(state="disable")

        

        def guess():
            try:

                ans=answer.get()
                if(len(ans)!=0):

                    if(ans==str(actual_number)):
                        tkinter.messagebox._show("Correct","Your Guess is correct")
                        change()
                        answer.set("")
                    else:
                        tkinter.messagebox._show("Wrong","Your Guess is wrong")
                else:
                    tkinter.messagebox.showerror("Error","Please write guess")
            except:
                tkinter.messagebox.showerror("Error","Please Select Change Number to start")











#==================frame=============================#
        
        mainframe=Frame(self.root,width=500,height=350,relief="ridge",bd=3,bg="black")
        mainframe.place(x=0,y=0)


        lab_number=Label(mainframe,text="Please Enter Number",font=('times new roman',16),bg="black",fg="white")
        lab_number.place(x=170,y=10)

        ent_number=Entry(mainframe,width=37,font=('times new roman',14),relief="ridge",bd=4,justify="center",textvariable=answer)
        ent_number.place(x=70,y=50)

        lab_hint=Label(mainframe,text="Please Select Change Number to start",font=('times new roman',14),bg="black",fg="white")
        lab_hint.place(x=100,y=100)

        but_guess=Button(mainframe,width=16,text="Guess",font=('times new roman',14),cursor="hand2",command=guess)
        but_guess.place(x=20,y=190)
        but_guess.bind("<Enter>",on_enter1)
        but_guess.bind("<Leave>",on_leave1)

        but_change=Button(mainframe,width=16,text="Change Numbers",font=('times new roman',14),cursor="hand2",command=change)
        but_change.place(x=300,y=190)
        but_change.bind("<Enter>",on_enter2)
        but_change.bind("<Leave>",on_leave2)


        but_clear=Button(mainframe,width=16,text="Clear",font=('times new roman',14),cursor="hand2",command=clear)
        but_clear.place(x=150,y=250)
        but_clear.bind("<Enter>",on_enter3)
        but_clear.bind("<Leave>",on_leave3)




if __name__ == "__main__":
    root=Tk()
    Number_Guessing(root)
    root.mainloop()