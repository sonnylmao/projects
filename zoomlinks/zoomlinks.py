#ver 1.0 edited: 28/3/21
import webbrowser
from tkinter import * 
from tkinter import font

#tkinter setup
root = Tk()
root.title("Zoom Links GUI")
root.geometry("500x500")

## defining functions for zoom links ## 
#maths
def mathspure():
    webbrowser.open('https://www.google.com') #insert zoom link here
def mathsmech():
    webbrowser.open('https://www.google.com') #insert zoom link here
def mathsstats():
    webbrowser.open('https://www.google.com') #insert zoom link here

#physics
def physicsA():
    webbrowser.open('https://www.google.com') #insert zoom link here
def physicsB():
    webbrowser.open('https://www.google.com') #insert zoom link here

#compsci
def cstheory():
    webbrowser.open('https://www.google.com') #insert zoom link here
def csproblsolving():
    webbrowser.open('https://www.google.com') #insert zoom link here
    
## text declaration ##
'''
Text1 = Text(root, "hellO")
Text1.grid(row=0,column=2)
'''

myFont = font.Font(family='Arial', size=15, weight='bold')
## button declaration ##
#maths 
ButtonTextPure = Button(root, text="Maths", state=DISABLED, font=myFont, fg="black", width=9)
ButtonTextPure.grid(row=0,column=0,padx=5)
ButtonPure = Button(root, text="Pure", fg="#FFFFFF", bg="#000000", command=mathspure, height=2, width=15) #pure
ButtonPure.grid(row=1,column=0,padx=5,pady=1)
ButtonPure = Button(root, text="Mechanics", fg="#FFFFFF", bg="#000000", command=mathsmech, height=2, width=15) #mech
ButtonPure.grid(row=2,column=0,padx=5,pady=1)
ButtonPure = Button(root, text="Statistics", fg="#FFFFFF", bg="#000000", command=mathsstats, height=2, width=15) #stats
ButtonPure.grid(row=3,column=0,padx=5,pady=1)

#physics
ButtonTextPure = Button(root, text="Physics", state=DISABLED, font=myFont, fg="black", width=9)
ButtonTextPure.grid(row=0,column=1,padx=5)
ButtonPure = Button(root, text="Dr _____", fg="#5585F9", bg="#4BDBCF", command=physicsA, height=2, width=15) #teacher1
ButtonPure.grid(row=1,column=1,padx=5,pady=1)
ButtonPure = Button(root, text="Mr _____", fg="#5585F9", bg="#4BDBCF", command=physicsB, height=2, width=15) #teacher2
ButtonPure.grid(row=2,column=1,padx=5,pady=1)

#comp sci
ButtonTextPure = Button(root, text="Comp Sci", state=DISABLED, font=myFont, fg="black", width=9)
ButtonTextPure.grid(row=0,column=2,padx=5)
ButtonPure = Button(root, text="Theory", fg="#5585F9", bg="#4BDBCF", command=cstheory, height=2, width=15) #theory
ButtonPure.grid(row=1,column=2,padx=5,pady=1)
ButtonPure = Button(root, text="Problem Solving", fg="#5585F9", bg="#4BDBCF", command=csproblsolving, height=2, width=15) #pracitcal/problem solving
ButtonPure.grid(row=2,column=2,padx=5,pady=1)
root.mainloop()
