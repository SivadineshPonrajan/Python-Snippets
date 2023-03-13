# -*- coding: utf-8 -*-
import wx
import wikipedia
import wolframalpha
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")


#espeak.synth("Welcome")
speak.Speak("Welcome")

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(500, 105),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
             wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="Virtual-X")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label="Hello, I am a Digital Assistant. How can I help you?")
        my_sizer.Add(lbl, 0, wx.ALL, 10)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(500,40))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 5, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()



    def OnEnter(self, event):
        input = self.txt.GetValue()
        input = input.lower()
        x = input
        if input.startswith(":"):
            #wolframalpha
            input = input.split('.')

            input = '.'.join(input[1:])
            print (input)
            print (" ")
            print (" ")
            app_id = "6293QU-J72L9374W6"
            client = wolframalpha.Client(app_id)
            res = client.query(input)
            answer = next(res.results).text
            #espeak.synth(answer)
            speak.Speak("Here you go")
            print (answer)
        elif input.startswith("."):
            speak.Speak("Here you go")
            print ("My creator is Mr.Sivadinesh - An engineering Student")
        else:
            #wikipedia
            input = x.split(' ')
            input = ' '.join(input[2:])
            #espeak.synth("Searched for"+input)
            speak.Speak("Here you go")
            print(wikipedia.summary(input))


if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
