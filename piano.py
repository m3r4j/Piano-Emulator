from tkinter import *
from PIL import Image, ImageTk
import playsound
import threading


# Initialize the screen
root = Tk()

# Set the title to "Piano-Emulator"
root.title('Piano-Emulator')

# Create the window size
root.geometry('689x400')

# Make the window unresizable
root.resizable(0,0)

# Set the icon to a "piano" icon
root.iconbitmap('icons/pianoicon.ico')


# Add the piano image onto the screen
piano_img = Image.open('images/piano.png')
piano_img = piano_img.resize((200, 200), Image.ANTIALIAS)
piano_img = ImageTk.PhotoImage(piano_img)

# Create the piano label
piano_label = Label(root, image=piano_img)
piano_label.pack()
counter_label = Label(root, text='0', font=(None, 30))
counter_label.place(x=90, y=70)


# Create a function that can play a sound
def playpiano(sound_num):
	global counter_label

	counter_label.place_forget()
	counter_label = Label(root, text=sound_num, font=(None, 30))
	counter_label.place(x=90, y=70)
	
	playsound.playsound(f'audio/Piano{sound_num}.mp3')

# Create a thread so the GUI doesn't glitch out by "playsound" library
def playbutton(sound_num):
	global t 
	
	t = threading.Thread(target=playpiano, args=(sound_num,))
	t.setDaemon(True)
	t.start()



# Add 23 buttons
Button(root, bg='black', pady=73, padx=10, command=lambda: playbutton(1)).place(x=0, y=230)
Button(root, bg='white', pady=73, padx=10, command=lambda: playbutton(2)).place(x=30, y=230)
Button(root, bg='black', pady=73, padx=10, command=lambda: playbutton(3)).place(x=60, y=230)
Button(root, bg='white', pady=73, padx=10, command=lambda: playbutton(4)).place(x=90, y=230)
Button(root, bg='black', pady=73, padx=10, command=lambda: playbutton(5)).place(x=120, y=230)
Button(root, bg='white', pady=73, padx=10, command=lambda: playbutton(6)).place(x=150, y=230)
Button(root, bg='black', pady=73, padx=10, command=lambda: playbutton(7)).place(x=180, y=230)
Button(root, bg='white', pady=73, padx=10, command=lambda: playbutton(8)).place(x=210, y=230)
Button(root, bg='black', pady=73, padx=10, command=lambda: playbutton(9)).place(x=240, y=230)
Button(root, bg='white', pady=73, padx=10, command=lambda: playbutton(10)).place(x=270, y=230)
Button(root, bg='black', pady=73, padx=10, command=lambda: playbutton(11)).place(x=300, y=230)
Button(root, bg='white', pady=73, padx=10, command=lambda: playbutton(12)).place(x=330, y=230)
Button(root, bg='black', pady=73, padx=10, command=lambda: playbutton(13)).place(x=360, y=230)
Button(root, bg='white', pady=73, padx=10, command=lambda: playbutton(14)).place(x=390, y=230)
Button(root, bg='black', pady=73, padx=10, command=lambda: playbutton(15)).place(x=420, y=230)
Button(root, bg='white', pady=73, padx=10, command=lambda: playbutton(16)).place(x=450, y=230)
Button(root, bg='black', pady=73, padx=10, command=lambda: playbutton(17)).place(x=480, y=230)
Button(root, bg='white', pady=73, padx=10, command=lambda: playbutton(18)).place(x=510, y=230)
Button(root, bg='black', pady=73, padx=10, command=lambda: playbutton(19)).place(x=540, y=230)
Button(root, bg='white', pady=73, padx=10, command=lambda: playbutton(20)).place(x=570, y=230)
Button(root, bg='black', pady=73, padx=10, command=lambda: playbutton(21)).place(x=600, y=230)
Button(root, bg='white', pady=73, padx=10, command=lambda: playbutton(22)).place(x=630, y=230)
Button(root, bg='black', pady=73, padx=10, command=lambda: playbutton(23)).place(x=660, y=230)



# Run the mainloop
root.mainloop()