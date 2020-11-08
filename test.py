import wx
 
 
class Main(wx.Frame):
 
    def __init__(self, parent, id, title):
        """ レイアウトの作成 """
 
        wx.Frame.__init__(self, parent, id, title)
        self.panel = wx.Panel(self, wx.ID_ANY)
 
        self.v_layout = wx.BoxSizer(wx.VERTICAL)
 
        button = wx.Button(self.panel, wx.ID_ANY, "文字を追加")
        button.Bind(wx.EVT_BUTTON, self.add_text)
 
        self.v_layout.Add(button)
        self.panel.SetSizer(self.v_layout)
 
        self.Show(True)
 
    def add_text(self, event):
        text = wx.StaticText(self.panel, wx.ID_ANY, "追加した文字")
        self.v_layout.Add(text, proportion=0)
        self.v_layout.Layout()
 
 
def main():
    app = wx.App()
    Main(None, wx.ID_ANY, "タイトル")
    app.MainLoop()
 
if __name__ == "__main__":
    main()
