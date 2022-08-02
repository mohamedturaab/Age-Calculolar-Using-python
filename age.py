from tkinter import *
from datetime import  date
root=Tk()
root.geometry("700x500")
root.title(" Age Calculater | Developed By Eng IQ😍😍")

def calculeteage():
    today = date.today()
    birthDate=date(int(yearEntry.get()), int(MothEntry.get()), int(dayEntry.get()))
    age = today.year - birthDate.year - ((today.month , today.today) < (birthDate.month , birthDate.day))
    Label(text=f"{namevalue.get()} Your Age {age}").grid(row=6, column=1)


Label(text="Name").grid(row=1,column=0)
Label(text =ANCHOR)
Label(text="Year").grid(row=2,column=0)
Label(text="Moth").grid(row=3,column=0)
Label(text="Day").grid(row=4,column=0)

namevalue= StringVar()
yearvalue= StringVar()
Mothvalue= StringVar()
dayvalue= StringVar()

nameEntry = Entry(root,textvariabl=namevalue)
yearEntry= Entry(root,textvariable=yearvalue)
MothEntry= Entry(root,textvariable=Mothvalue)
dayEntry= Entry(root,textvariable=dayvalue)

nameEntry.grid(row=1,column=1,padx=10,pady=10)
yearEntry.grid(row=2,column=1,padx=10,pady=10)
MothEntry.grid(row=3,column=1,padx=10,pady=10)
dayEntry.grid(row=4,column=1,padx=10,pady=10)

Button(text="Calculate Age ",command=calculeteage,bg='#002233',fg='white',font='arial 10').grid(row=5,column=1)
root.mainloop()