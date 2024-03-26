from tkinter import *

Window = Tk()

# size
# Window.geometry("1080x720")
# Centre Window
WindowWidth = 1080
WindowHeight = 720
ScreenWidth = int((Window.winfo_screenwidth())/2) - int(WindowWidth/2)
ScreenHeigth = int((Window.winfo_screenheight())/2)- int(WindowHeight/2)
# print(ScreenWidth,ScreenHeigth)
Window.geometry(f"{WindowWidth}x{WindowHeight}+{ScreenWidth}+{ScreenHeigth}")
#title
Window.title("Weather")
#logo
logo = PhotoImage(file="img/logo.png")
Window.iconphoto(True,logo)
# background
Window.config(background="#c0c0c0")

Window.mainloop()