import wx
import random

class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='Guess the number')
        
        self.input = 0
        self.secret_number = 0
        self.new_game()

        #set control container panel
        self.my_panel = wx.Panel(self)
        self.my_menu = wx.Menu()
        
        #configure layout
        self.my_sizer = wx.BoxSizer(wx.VERTICAL)
                
        #add text box
        self.text_control = wx.TextCtrl(self.my_panel, pos=(5,5), style=wx.TE_RIGHT)
        self.my_sizer.Add(self.text_control, proportion=2, flag=wx.ALL | wx.EXPAND, border=5)
        self.Bind(wx.EVT_TEXT_ENTER, self.input_guess, self.text_control)
        
        #add clear button
        newgame_btn = wx.Button(self.my_panel, label='New Game')
        self.my_sizer.Add(newgame_btn, proportion=0, flag=wx.ALL | wx.CENTER , border=5)
        self.Bind(wx.EVT_BUTTON, self.on_newgame, newgame_btn)
        
        #add input button
        input_btn = wx.Button(self.my_panel, label='Enter')
        self.my_sizer.Add(input_btn, proportion=0, flag=wx.ALL | wx.CENTER , border=5)
        self.Bind(wx.EVT_BUTTON, self.input_guess, input_btn)
        
        #set sizer
        self.my_panel.SetSizer(self.my_sizer)
        
        self.Show()
        
    def on_newgame(self, event):
        pass
        
    def input_guess(self, event):
        value = self.text_control.GetValue()
    
        self.input = int(value)
        print(f'Guess was {self.input}')
        self.comapre()

    def comapre(self):
        if self.input == self.secret_number:
            print("Correct")
        elif self.input < self.secret_number:
            print("Secret number is higher")
        else:
            print("Secret number is lower")

    def new_game(self):
        self.secret_number = random.randrange(100)

app = wx.App()
frame = MyFrame()
app.MainLoop()