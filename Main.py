from tkinter import *
import Data 
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

# City
City = Entry(Window,width=25,font=("Arial",17),fg="Black",bd=10,justify="center")
City.place(x=540 - City.winfo_reqwidth()//2,y=28)

#Button

def GetCity():
    CityName = City.get()
   
    WeatherData = list(Data.CollectWeatherInfo(City=CityName))
    print(WeatherData)

    WeatherLabel = Label(Window,text=WeatherData[0],font=("Arial",45),bg="#c0c0c0",width=100,justify="center")
    WeatherLabel.place(x=540 - WeatherLabel.winfo_reqwidth()//2,y=100)

    TempLabel = Label(Window,text=WeatherData[1],font=("Arial",30),bg="#c0c0c0",width=15,justify="center")
    TempLabel.place(x=540 - TempLabel.winfo_reqwidth()//2,y=180)

    MinTempLabel = Label(Window,text=WeatherData[2],font=("Arial",20),bg="#c0c0c0",width=15,justify="center")
    MinTempLabel.place(x=540 - MinTempLabel.winfo_reqwidth()//2 - 350,y=550)

    HumidityLabel = Label(Window,text=WeatherData[4],font=("Arial",20),bg="#c0c0c0",width=15,justify="center")
    HumidityLabel.place(x=540 - HumidityLabel.winfo_reqwidth()//2,y=550) 

    MaxTempLabel = Label(Window,text=WeatherData[3],font=("Arial",20),bg="#c0c0c0",width=15,justify="center")
    MaxTempLabel.place(x=540 - MaxTempLabel.winfo_reqwidth()//2 + 350,y=550)
    

SearchButton = Button(Window,text="Search",padx=10,font=("Arial",17),command=GetCity)
SearchButton.place(x=540 + City.winfo_reqwidth()//2 + 25,y=28)

TodaysWeatherLabel = Label(Window,text="Todays Weather",font=("Arial",45),bg="#c0c0c0")
TodaysWeatherLabel.place(x=540 - TodaysWeatherLabel.winfo_reqwidth()//2,y=100)

TodaysTempLabel = Label(Window,text="--.--",font=("Arial",30),bg="#c0c0c0")
TodaysTempLabel.place(x=540 - TodaysTempLabel.winfo_reqwidth()//2,y=180)

MinTempLabel = Label(Window,text="Min Temp",font=("Arial",20),bg="#c0c0c0")
MinTempLabel.place(x=540 - MinTempLabel.winfo_reqwidth()//2 - 350,y=500) 

HumidityLabel = Label(Window,text="Humidity",font=("Arial",20),bg="#c0c0c0")
HumidityLabel.place(x=540 - HumidityLabel.winfo_reqwidth()//2,y=500) 

MaxTempLabel = Label(Window,text="Max Temp",font=("Arial",20),bg="#c0c0c0")
MaxTempLabel.place(x=540 - MaxTempLabel.winfo_reqwidth()//2 + 350,y=500) 

TodaysMinTempLabel = Label(Window,text="--.--",font=("Arial",20),bg="#c0c0c0")
TodaysMinTempLabel.place(x=540 - TodaysMinTempLabel.winfo_reqwidth()//2 - 350,y=550)

TodaysHumidityLabel = Label(Window,text="--.--",font=("Arial",20),bg="#c0c0c0")
TodaysHumidityLabel.place(x=540 - TodaysHumidityLabel.winfo_reqwidth()//2,y=550) 

TodaysMaxTempLabel = Label(Window,text="--.--",font=("Arial",20),bg="#c0c0c0")
TodaysMaxTempLabel.place(x=540 - TodaysMaxTempLabel.winfo_reqwidth()//2 + 350,y=550)


Window.mainloop()