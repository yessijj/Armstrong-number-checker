from tkinter import*
from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter import messagebox
import tkinter as tk


def num_length(num:int) -> int:
    res = 0
    while num > 0:
        res += 1
        num //= 10
    return res


def is_armstrong(num: str) -> str:
    try:
        num = int(num)
        length = num_length(num)
        # creating copy so that we can check result with original number
        copy = num
        arm = 0
        arm_in_string_form = ''
        while copy > 0:
            rem = copy % 10
            arm += rem ** length
            arm_in_string_form = f'{rem}^{length} + ' + arm_in_string_form
            copy //= 10

        if num == 0:
            text1 = '0^0' + ' = ' + str(arm)
        else:
            text1 = arm_in_string_form[:-3] + ' = ' + str(arm)

        if arm == num:
            text1 += f' and {arm} = {num}.'
            text2 = f'Therefore {num} is an armstrong number.'
            valid_num()
        else:
            text1 += f' and {arm} != {num}.'
            text2 = f'Therefore {num} is not an armstrong number!'
            not_valid_num()
        return text1 + '\n' + text2

    except:
        return 'Invalid input!'






w = Tk()




w.geometry("400x400+500+200")
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
w.overrideredirect(1)

s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", foreground='blue', background='white')
progress = Progressbar(w, style="red.Horizontal.TProgressbar", orient=HORIZONTAL   , length=800, mode='determinate', )


def valid_num():
    MsgBox = tk.messagebox.askquestion('Congratulations!!!', 'The given number is Armstrong Number',
                                       icon='info')


def not_valid_num():
    MsgBox = tk.messagebox.askquestion('Sorry!!!', 'The given number is not Armstrong Number',
                                       icon='error')


def new_win():

 root=Tk()



 root.geometry("400x400+500+200")
 root.resizable(0,0)
 root.title("ARMSTRONG NUMBERS CHECKER")
 root.overrideredirect(1)

 Label(root, font="Times 12 " , text="ENTER 3 DIGIT NUMBERS" ,fg=a).pack(fill=X , ipadx=10, pady=30, padx=10)

 scvalue = StringVar()
 scvalue.set("")
 screen= Entry(root, textvar=scvalue, font="Times 15 " , bd=6)
 screen.pack(fill=X , ipadx=30, pady=20,  padx=50 )



 f = Frame(root, bg="grey").pack()
 b1 = Button(root, width=10, height=2, text='CHECK',  border=0, fg=a, bg='white' , font="Times 10 " ,command=lambda:is_armstrong(scvalue.get()))
 b1.place(x=100, y=200)

 def ExitApplication():
     MsgBox = tk.messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application',
                                          icon='warning')
     if MsgBox == 'yes':
         root.destroy()
     else:
         tk.messagebox.showinfo('Return', 'You will now return to the application screen')

 b2 = Button(root, width=10, height=2, text='EXIT', border=0, fg=a, bg='white', font="Times 10 ", command=ExitApplication)
 b2.place(x=230, y=200)



 root.mainloop()



def bar():
    l4 = Label(w, text='Loading...', fg='white', bg=a)
    lst4 = ('Calibri (Body)', 10)
    l4.config(font=lst4)
    l4.place(x=18, y=350)

    import time
    r = 0
    for i in range(100):
        progress['value'] = r
        w.update_idletasks()
        time.sleep(0.03)
        r = r + 1

    w.destroy()
    new_win()

progress.place(x=-10, y=380)

a = '#249794'
Frame(w, width=427, height=385, bg=a).place(x=0, y=0)  # 249794
b1 = Button(w, width=10, height=1, text='Get Started', command=bar, border=0, fg=a, bg='white' , font="Times 10 ")
b1.place(x=170, y=300)



l1=Label(w,text='ARMSTRONG',fg='white',bg=a)
lst1=('Calibri (Body)',18,'bold')
l1.config(font=lst1)
l1.place(x=20,y=80)

l2=Label(w,text='NUMBER',fg='white',bg=a)
lst2=('Calibri (Body)',18)
l2.config(font=lst2)
l2.place(x=180,y=82)

l3=Label(w,text='CHECKER',fg='white',bg=a)
lst3=('Calibri (Body)',17)
l3.config(font=lst3)
l3.place(x=20,y=110)



w.mainloop()
