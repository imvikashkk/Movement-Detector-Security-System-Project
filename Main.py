import tkinter as tk
import tkinter.font as font
from PIL import Image, ImageTk
from Backend import backend
from Open import open

window = tk.Tk()
window.title("Movement Detection")
window.iconphoto(False, tk.PhotoImage(file='mn.png'))
window.geometry('1080x760')

frame1 = tk.Frame(window)
label_title = tk.Label(frame1, text="VRV THE MAKERS")
label_font = font.Font(size=35, weight='bold',family='Helvetica')
label_title['font'] = label_font
label_title.grid(pady=(10,10), column=2)

icon = Image.open('icons/spy.png')
icon = icon.resize((150,150))
icon = ImageTk.PhotoImage(icon)
label_icon = tk.Label(frame1, image=icon)
label_icon.grid(row=1, pady=(5,10), column=2)

icon = Image.open('icons/spy.png')
icon = icon.resize((150,150) )
icon = ImageTk.PhotoImage(icon)
label_icon = tk.Label(frame1, image=icon)
label_icon.grid(row=1, pady=(5,10), column=2)

btn1_image = Image.open('icons/lamp.png')
btn1_image = btn1_image.resize((50,50))
btn1_image = ImageTk.PhotoImage(btn1_image)


btnQuit_image = Image.open('icons/exit.png')
btnQuit_image = btnQuit_image.resize((50,50) )
btnQuit_image = ImageTk.PhotoImage(btnQuit_image)

btn3_image = Image.open('icons/recording.png')
btn3_image = btn3_image.resize((50,50) )
btn3_image = ImageTk.PhotoImage(btn3_image)



################ BUTTON ################

btn_font = font.Font(size=25)
btn1 = tk.Button(frame1, text='Saved', height=90, width=180, fg='green',command=open, image=btn3_image, compound='left')
btn1['font'] = btn_font
btn1.grid(row=4, pady=(20,10),column=1)

btnQuit = tk.Button(frame1, text='Exit', height=90, width=180, fg='red', command=window.quit, image=btnQuit_image)
btnQuit['font'] = btn_font
btnQuit.grid(row=4, pady=(20,10), column=3)

btn_font = font.Font(size=25)
btn3 = tk.Button(frame1, text='Monitor', height=90, width=300,command=backend, fg='green', image=btn1_image, compound='left')
btn3['font'] = btn_font
btn3.grid(row=5, pady=(20,10), column=2)

frame1.pack()
window.mainloop()

