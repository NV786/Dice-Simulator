import random
import tkinter
root = tkinter.Tk()
root.geometry('600x600')
root.configure(bg = 'Blue Violet')
root.resizable(False,False)
root.title('Niyams Rolling Dice Simulator')

#label to print result
label = tkinter.Label(root, text='', font=('Helvetica', 300),fg='white', bg = 'Blue Violet')

#label to introduce
label2 = tkinter.Label(root, text='Welcome to Niyam Verma"s Dice roll Simulator.', font=('Poppins bold', 10, 'bold'))
label2.pack(padx=20, pady=10)
label9 = tkinter.Label(root, text='Click the Roll Dice Button to Roll', font=('Poppins bold', 10, 'bold'))
label9.pack(padx=20, pady=20)
def roll_dice():
    value = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    result=random.choice(value)
    label.configure(text=result)
    label.pack()
    if(result=='\u2680'):
        label3=tkinter.Label(root,text='You rolled a one! Click roll dice to roll again.',font=('Poppins bold',10, 'bold'))
        label3.place(x=150,y=550)
    elif(result=='\u2681'):
        label3=tkinter.Label(root,text='You rolled a two! Click roll dice to roll again.',font=('Poppins bold',10,'bold'))
        label3.place(x=150,y=550)
    elif(result=='\u2682'):
        label3=tkinter.Label(root,text='You rolled a three! Click roll dice to roll again.',font=('Poppins bold',10,'bold'))
        label3.place(x=150,y=550)
    elif(result=='\u2683'):
        label3=tkinter.Label(root,text='You rolled a four! Click roll dice to roll again.',font=('Poppins bold',10,'bold'))
        label3.place(x=150,y=550)
    elif(result=='\u2684'):
        label3=tkinter.Label(root,text='You rolled a five! Click roll dice to roll again.',font=('Poppins bold',10,'bold'))
        label3.place(x=150,y=550)
    elif(result=='\u2685'):
        label3=tkinter.Label(root,text='You rolled a six! Click roll dice to roll again.',font=('Poppins bold',10,'bold'))
        label3.place(x=150,y=550)
        
button = tkinter.Button(root, text='roll dice', foreground='red', command=roll_dice)
button.pack()
root.mainloop()