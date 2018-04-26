from  tkinter import *
from PIL import Image

def main():
    showGUI()




def showGUI():
    top = Tk()
    top.title("Copic Color Collection")
    L1 = Label(top,text="Color 1").grid(row=0)
    E1 = Entry(top)
    E1.grid(row=0,column=1)

    L2 = Label(top,text="Color 2").grid(row=1)
    E2 = Entry(top)
    E2.grid(row=1,column=1)

    L3 = Label(top,text="Color 3").grid(row=2)
    E3 = Entry(top)
    E3.grid(row=2,column=1)

    L4 = Label(top,text="Color 4").grid(row=3)
    E4 = Entry(top)
    E4.grid(row=3,column=1)

    L5 = Label(top,text="Color 5").grid(row=4)
    E5 = Entry(top)
    E5.grid(row=4,column=1)

    def grabInputs():
        input1 = E1.get()
        input2 = E2.get()
        input3 = E3.get()
        input4 = E4.get()
        input5 = E5.get()
        return [input1,input2,input3,input4,input5]
    
    def showColor():
        givenInputs = grabInputs()
        if(givenInputs[0]):
            img1 = Image.open('../colors/'+givenInputs[0]+'.jpg')
            img1.show()
        if(givenInputs[1]):
            img2 = Image.open('../colors/'+givenInputs[1]+'.jpg')
            img2.show()
        if(givenInputs[2]):
            img3 = Image.open('../colors/'+givenInputs[2]+'.jpg')
            img3.show()
        if(givenInputs[3]):
            img4 = Image.open('../colors/'+givenInputs[3]+'.jpg')
            img4.show()
        if(givenInputs[4]):
            img5 = Image.open('../colors/'+givenInputs[4]+'.jpg')
            img5.show()

    button = Button(top, text="Colorize",command=showColor).grid(row=5, column=1)


    top.mainloop()

main()

