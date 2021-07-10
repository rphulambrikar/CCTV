import tkinter as tk
import tkinter.font as font
from incoming_outgoing import incoming_outgoing
from moving import distract
from rectangle import rectangle_noise
from recording import recording
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Smart cctv")
window.iconphoto(False, tk.PhotoImage(file='icon.png'))
window.configure(bg = "gray")
window.geometry('1080x760')


frame1 = tk.Frame(window)

label_title = tk.Label(frame1, text="Smart CCTV Monitoring", bg="Blue")
label_font = font.Font(size=35, weight='bold',family='Helvetica')
label_title['font'] = label_font
label_title.grid(pady=(10,10), column=2)


btn1_image = Image.open('icons/lamp.png')
btn1_image = btn1_image.resize((50,50), Image.ANTIALIAS)
btn1_image = ImageTk.PhotoImage(btn1_image)

btn2_image = Image.open('icons/rectangle-of-cutted-line-geometrical-shape.png')
btn2_image = btn2_image.resize((50,50), Image.ANTIALIAS)
btn2_image = ImageTk.PhotoImage(btn2_image)

btn5_image = Image.open('icons/exit.png')
btn5_image = btn5_image.resize((80,80), Image.ANTIALIAS)
btn5_image = ImageTk.PhotoImage(btn5_image)

btn3_image = Image.open('icons/security-camera.png')
btn3_image = btn3_image.resize((50,50), Image.ANTIALIAS)
btn3_image = ImageTk.PhotoImage(btn3_image)

btn6_image = Image.open('icons/incognito.png')
btn6_image = btn6_image.resize((50,50), Image.ANTIALIAS)
btn6_image = ImageTk.PhotoImage(btn6_image)

btn4_image = Image.open('icons/recording.png')
btn4_image = btn4_image.resize((50,50), Image.ANTIALIAS)
btn4_image = ImageTk.PhotoImage(btn4_image)

# --------------- Button -------------------#
btn_font = font.Font(size=25)
btn1 = tk.Button(frame1, text='Monitor', height=90, width=180, bg='gray', fg='black', image=btn1_image, compound='left')
btn1['font'] = btn_font


btn2 = tk.Button(frame1, text='Rectangle', height=90, width=180, fg='green', bg='cyan', command=rectangle_noise, compound='left', image=btn2_image)
btn2['font'] = btn_font
btn2.grid(row=3, pady=(20,10), column=2)

btn_font = font.Font(size=25)
btn3 = tk.Button(frame1, text='Noise', height=90, width=180, fg='green',bg='cyan', command=distract, image=btn3_image, compound='left')
btn3['font'] = btn_font
btn3.grid(row=1, pady=(20,10),column=2)

btn4 = tk.Button(frame1, text='Record', height=90, width=180,fg='green', bg='cyan', command=recording, image=btn4_image, compound='left')
btn4['font'] = btn_font
btn4.grid(row=2, pady=(20,10), column=2)


btn6 = tk.Button(frame1, text='In/Out', height=90, width=180,fg='green', bg='cyan', command=incoming_outgoing, image=btn6_image, compound='left')
btn6['font'] = btn_font
btn6.grid(row=4, pady=(20,10), column=2)

btn5 = tk.Button(frame1, height=90, width=180, bg='gray',fg='black', command=window.quit, image=btn5_image)
btn5['font'] = btn_font
btn5.grid(row=5, pady=(20,10), column=2)

frame1.pack()
window.mainloop()