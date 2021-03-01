import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("(Interface) Pycalc Alpha v1.6  ©2020 Samcq50")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_358=tk.Button(root)
        GButton_358["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=48)
        GButton_358["font"] = ft
        GButton_358["fg"] = "#000000"
        GButton_358["justify"] = "center"
        GButton_358["text"] = "+"
        GButton_358.place(x=530,y=100,width=70,height=70)
        GButton_358["command"] = self.GButton_358_command

        GButton_692=tk.Button(root)
        GButton_692["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=48)
        GButton_692["font"] = ft
        GButton_692["fg"] = "#000000"
        GButton_692["justify"] = "center"
        GButton_692["text"] = "-"
        GButton_692.place(x=530,y=180,width=70,height=70)
        GButton_692["command"] = self.GButton_692_command

        GButton_459=tk.Button(root)
        GButton_459["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=48)
        GButton_459["font"] = ft
        GButton_459["fg"] = "#000000"
        GButton_459["justify"] = "center"
        GButton_459["text"] = "x"
        GButton_459.place(x=530,y=260,width=70,height=70)
        GButton_459["command"] = self.GButton_459_command

        GButton_210=tk.Button(root)
        GButton_210["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=48)
        GButton_210["font"] = ft
        GButton_210["fg"] = "#000000"
        GButton_210["justify"] = "center"
        GButton_210["text"] = "="
        GButton_210.place(x=530,y=420,width=70,height=70)
        GButton_210["command"] = self.GButton_210_command

        GButton_791=tk.Button(root)
        GButton_791["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=48)
        GButton_791["font"] = ft
        GButton_791["fg"] = "#000000"
        GButton_791["justify"] = "center"
        GButton_791["text"] = "M"
        GButton_791.place(x=450,y=100,width=70,height=70)
        GButton_791["command"] = self.GButton_791_command

        GButton_730=tk.Button(root)
        GButton_730["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=48)
        GButton_730["font"] = ft
        GButton_730["fg"] = "#000000"
        GButton_730["justify"] = "center"
        GButton_730["text"] = "π"
        GButton_730.place(x=450,y=180,width=70,height=70)
        GButton_730["command"] = self.GButton_730_command

        GButton_147=tk.Button(root)
        GButton_147["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=28)
        GButton_147["font"] = ft
        GButton_147["fg"] = "#000000"
        GButton_147["justify"] = "center"
        GButton_147["text"] = "X_2"
        GButton_147.place(x=450,y=260,width=70,height=70)
        GButton_147["command"] = self.GButton_147_command

        GButton_376=tk.Button(root)
        GButton_376["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=28)
        GButton_376["font"] = ft
        GButton_376["fg"] = "#000000"
        GButton_376["justify"] = "center"
        GButton_376["text"] = "X_3"
        GButton_376.place(x=450,y=340,width=70,height=70)
        GButton_376["command"] = self.GButton_376_command

        GButton_699=tk.Button(root)
        GButton_699["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=26)
        GButton_699["font"] = ft
        GButton_699["fg"] = "#000000"
        GButton_699["justify"] = "center"
        GButton_699["text"] = "X_N"
        GButton_699.place(x=450,y=420,width=70,height=70)
        GButton_699["command"] = self.GButton_699_command

        GButton_429=tk.Button(root)
        GButton_429["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_429["font"] = ft
        GButton_429["fg"] = "#000000"
        GButton_429["justify"] = "center"
        GButton_429["text"] = "Shell version"
        GButton_429.place(x=360,y=0,width=80,height=20)
        GButton_429["command"] = self.GButton_429_command

        GButton_585=tk.Button(root)
        GButton_585["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_585["font"] = ft
        GButton_585["fg"] = "#000000"
        GButton_585["justify"] = "center"
        GButton_585["text"] = "About Pycalc"
        GButton_585.place(x=180,y=0,width=90,height=20)
        GButton_585["command"] = self.GButton_585_command

        GButton_764=tk.Button(root)
        GButton_764["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_764["font"] = ft
        GButton_764["fg"] = "#000000"
        GButton_764["justify"] = "center"
        GButton_764["text"] = "De-jam (reset)"
        GButton_764.place(x=80,y=0,width=90,height=20)
        GButton_764["command"] = self.GButton_764_command

        GButton_956=tk.Button(root)
        GButton_956["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_956["font"] = ft
        GButton_956["fg"] = "#000000"
        GButton_956["justify"] = "center"
        GButton_956["text"] = "Log/History"
        GButton_956.place(x=0,y=0,width=70,height=20)
        GButton_956["command"] = self.GButton_956_command

        GButton_688=tk.Button(root)
        GButton_688["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_688["font"] = ft
        GButton_688["fg"] = "#000000"
        GButton_688["justify"] = "center"
        GButton_688["text"] = "Scientific"
        GButton_688.place(x=280,y=0,width=70,height=20)
        GButton_688["command"] = self.GButton_688_command

        GButton_811=tk.Button(root)
        GButton_811["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=48)
        GButton_811["font"] = ft
        GButton_811["fg"] = "#000000"
        GButton_811["justify"] = "center"
        GButton_811["text"] = "/"
        GButton_811.place(x=530,y=340,width=70,height=70)
        GButton_811["command"] = self.GButton_811_command

        GButton_232=tk.Button(root)
        GButton_232["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_232["font"] = ft
        GButton_232["fg"] = "#000000"
        GButton_232["justify"] = "center"
        GButton_232["text"] = "Website"
        GButton_232.place(x=450,y=0,width=70,height=20)
        GButton_232["command"] = self.GButton_232_command

        GButton_235=tk.Button(root)
        GButton_235["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_235["font"] = ft
        GButton_235["fg"] = "#000000"
        GButton_235["justify"] = "center"
        GButton_235["text"] = "Help"
        GButton_235.place(x=530,y=0,width=70,height=20)
        GButton_235["command"] = self.GButton_235_command

        GButton_207=tk.Button(root)
        GButton_207["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=48)
        GButton_207["font"] = ft
        GButton_207["fg"] = "#000000"
        GButton_207["justify"] = "center"
        GButton_207["text"] = "9"
        GButton_207.place(x=340,y=180,width=70,height=70)
        GButton_207["command"] = self.GButton_207_command

        GButton_346=tk.Button(root)
        GButton_346["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=48)
        GButton_346["font"] = ft
        GButton_346["fg"] = "#000000"
        GButton_346["justify"] = "center"
        GButton_346["text"] = "8"
        GButton_346.place(x=260,y=180,width=70,height=70)
        GButton_346["command"] = self.GButton_346_command

        GButton_805=tk.Button(root)
        GButton_805["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=48)
        GButton_805["font"] = ft
        GButton_805["fg"] = "#000000"
        GButton_805["justify"] = "center"
        GButton_805["text"] = "7"
        GButton_805.place(x=180,y=180,width=70,height=70)
        GButton_805["command"] = self.GButton_805_command

        GButton_876=tk.Button(root)
        GButton_876["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=48)
        GButton_876["font"] = ft
        GButton_876["fg"] = "#000000"
        GButton_876["justify"] = "center"
        GButton_876["text"] = "6"
        GButton_876.place(x=340,y=260,width=70,height=70)
        GButton_876["command"] = self.GButton_876_command

        GButton_350=tk.Button(root)
        GButton_350["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=48)
        GButton_350["font"] = ft
        GButton_350["fg"] = "#000000"
        GButton_350["justify"] = "center"
        GButton_350["text"] = "5"
        GButton_350.place(x=260,y=260,width=70,height=70)
        GButton_350["command"] = self.GButton_350_command

        GButton_28=tk.Button(root)
        GButton_28["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=48)
        GButton_28["font"] = ft
        GButton_28["fg"] = "#000000"
        GButton_28["justify"] = "center"
        GButton_28["text"] = "4"
        GButton_28.place(x=180,y=260,width=70,height=70)
        GButton_28["command"] = self.GButton_28_command

        GButton_466=tk.Button(root)
        GButton_466["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=48)
        GButton_466["font"] = ft
        GButton_466["fg"] = "#000000"
        GButton_466["justify"] = "center"
        GButton_466["text"] = "3"
        GButton_466.place(x=340,y=340,width=70,height=70)
        GButton_466["command"] = self.GButton_466_command

        GButton_375=tk.Button(root)
        GButton_375["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=48)
        GButton_375["font"] = ft
        GButton_375["fg"] = "#000000"
        GButton_375["justify"] = "center"
        GButton_375["text"] = "2"
        GButton_375.place(x=260,y=340,width=70,height=70)
        GButton_375["command"] = self.GButton_375_command

        GButton_121=tk.Button(root)
        GButton_121["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=48)
        GButton_121["font"] = ft
        GButton_121["fg"] = "#000000"
        GButton_121["justify"] = "center"
        GButton_121["text"] = "1"
        GButton_121.place(x=180,y=340,width=70,height=70)
        GButton_121["command"] = self.GButton_121_command

        GButton_483=tk.Button(root)
        GButton_483["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=48)
        GButton_483["font"] = ft
        GButton_483["fg"] = "#000000"
        GButton_483["justify"] = "center"
        GButton_483["text"] = "0"
        GButton_483.place(x=260,y=420,width=70,height=70)
        GButton_483["command"] = self.GButton_483_command

        GButton_412=tk.Button(root)
        GButton_412["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=48)
        GButton_412["font"] = ft
        GButton_412["fg"] = "#000000"
        GButton_412["justify"] = "center"
        GButton_412["text"] = "C"
        GButton_412.place(x=180,y=100,width=230,height=70)
        GButton_412["command"] = self.GButton_412_command

        GButton_739=tk.Button(root)
        GButton_739["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=48)
        GButton_739["font"] = ft
        GButton_739["fg"] = "#000000"
        GButton_739["justify"] = "center"
        GButton_739["text"] = "."
        GButton_739.place(x=340,y=420,width=70,height=70)
        GButton_739["command"] = self.GButton_739_command

        GButton_615=tk.Button(root)
        GButton_615["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=28)
        GButton_615["font"] = ft
        GButton_615["fg"] = "#000000"
        GButton_615["justify"] = "center"
        GButton_615["text"] = "MR"
        GButton_615.place(x=0,y=420,width=70,height=70)
        GButton_615["command"] = self.GButton_615_command

        GButton_760=tk.Button(root)
        GButton_760["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=28)
        GButton_760["font"] = ft
        GButton_760["fg"] = "#000000"
        GButton_760["justify"] = "center"
        GButton_760["text"] = "MC"
        GButton_760.place(x=0,y=340,width=70,height=70)
        GButton_760["command"] = self.GButton_760_command

        GButton_998=tk.Button(root)
        GButton_998["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=33)
        GButton_998["font"] = ft
        GButton_998["fg"] = "#000000"
        GButton_998["justify"] = "center"
        GButton_998["text"] = "+/-"
        GButton_998.place(x=0,y=100,width=70,height=230)
        GButton_998["command"] = self.GButton_998_command

        GButton_158=tk.Button(root)
        GButton_158["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_158["font"] = ft
        GButton_158["fg"] = "#000000"
        GButton_158["justify"] = "center"
        GButton_158["text"] = ""
        GButton_158.place(x=180,y=420,width=70,height=70)
        GButton_158["command"] = self.GButton_158_command

        GListBox_458=tk.Listbox(root)
        GListBox_458["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_458["font"] = ft
        GListBox_458["fg"] = "#333333"
        GListBox_458["justify"] = "center"
        GListBox_458.place(x=10,y=30,width=500,height=60)
        GListBox_458["listvariable"] = "y"

        GButton_875=tk.Button(root)
        GButton_875["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=28)
        GButton_875["font"] = ft
        GButton_875["fg"] = "#000000"
        GButton_875["justify"] = "center"
        GButton_875["text"] = "DEL"
        GButton_875.place(x=530,y=30,width=70,height=70)
        GButton_875["command"] = self.GButton_875_command

    def GButton_358_command(self):
        print("command")


    def GButton_692_command(self):
        print("command")


    def GButton_459_command(self):
        print("command")


    def GButton_210_command(self):
        print("command")


    def GButton_791_command(self):
        print("command")


    def GButton_730_command(self):
        print("command")


    def GButton_147_command(self):
        print("command")


    def GButton_376_command(self):
        print("command")


    def GButton_699_command(self):
        print("command")


    def GButton_429_command(self):
        print("command")


    def GButton_585_command(self):
        print("command")


    def GButton_764_command(self):
        print("command")


    def GButton_956_command(self):
        print("command")


    def GButton_688_command(self):
        print("command")


    def GButton_811_command(self):
        print("command")


    def GButton_232_command(self):
        print("command")


    def GButton_235_command(self):
        print("command")


    def GButton_207_command(self):
        print("command")


    def GButton_346_command(self):
        print("command")


    def GButton_805_command(self):
        print("command")


    def GButton_876_command(self):
        print("command")


    def GButton_350_command(self):
        print("command")


    def GButton_28_command(self):
        print("command")


    def GButton_466_command(self):
        print("command")


    def GButton_375_command(self):
        print("command")


    def GButton_121_command(self):
        print("command")


    def GButton_483_command(self):
        print("command")


    def GButton_412_command(self):
        print("command")


    def GButton_739_command(self):
        print("command")


    def GButton_615_command(self):
        print("command")


    def GButton_760_command(self):
        print("command")


    def GButton_998_command(self):
        print("command")


    def GButton_158_command(self):
        print("command")


    def GButton_875_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
