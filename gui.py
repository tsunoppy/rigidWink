#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.6 on Wed Nov 25 12:36:09 2020
#

import wx
import wx.grid

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((760, 849))
        
        # Menu Bar
        self.frame_menubar = wx.MenuBar()
        self.Ctrl = wx.Menu()
        item = self.Ctrl.Append(wx.ID_ANY, "&Save as xlsx", "")
        self.Bind(wx.EVT_MENU, self.OnLoad, id=item.GetId())
        item = self.Ctrl.Append(wx.ID_ANY, "&Export as pdf report", "")
        self.Bind(wx.EVT_MENU, self.Export_pdf, id=item.GetId())
        item = self.Ctrl.Append(wx.ID_ANY, "&Import as xls", "")
        self.Bind(wx.EVT_MENU, self.OnImport, id=item.GetId())
        item = self.Ctrl.Append(wx.ID_ANY, "&Load Sample", "")
        self.Bind(wx.EVT_MENU, self.OnSample, id=item.GetId())
        self.Ctrl.AppendSeparator()
        item = self.Ctrl.Append(wx.ID_ANY, "E&xit", "")
        self.Bind(wx.EVT_MENU, self.OnCancel, id=item.GetId())
        self.frame_menubar.Append(self.Ctrl, "&File")
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(wx.ID_ANY, "&About rigidWink", "")
        wxglade_tmp_menu.Append(wx.ID_ANY, "&Reference", "")
        self.frame_menubar.Append(wxglade_tmp_menu, "&About")
        self.SetMenuBar(self.frame_menubar)
        # Menu Bar end
        self.notebook_1 = wx.Notebook(self, wx.ID_ANY)
        self.notebook_1_model = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.grid_model = wx.grid.Grid(self.notebook_1_model, wx.ID_ANY, size=(1, 1))
        self.notebook_1_LOAD = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.grid_load = wx.grid.Grid(self.notebook_1_LOAD, wx.ID_ANY, size=(1, 1))
        self.notebook_1_COMB = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.grid_comb = wx.grid.Grid(self.notebook_1_COMB, wx.ID_ANY, size=(1, 1))
        self.notebook_1_CTLN = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.grid_ctln = wx.grid.Grid(self.notebook_1_CTLN, wx.ID_ANY, size=(1, 1))
        self.panel_result = wx.Panel(self, wx.ID_ANY, style=wx.BORDER_SIMPLE)
        self.text_ctrl_index = wx.TextCtrl(self.panel_result, wx.ID_ANY, "0", style=wx.TE_READONLY)
        self.text_ctrl_total = wx.TextCtrl(self.panel_result, wx.ID_ANY, "", style=wx.TE_READONLY)
        self.text_ctrl_result = wx.TextCtrl(self.panel_result, wx.ID_ANY, "Welcom to rigidWink!", style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.notebook_2 = wx.Notebook(self, wx.ID_ANY)
        self.notebook_2_RESULT = wx.Panel(self.notebook_2, wx.ID_ANY)
        self.panel_stress = wx.Panel(self.notebook_2_RESULT, wx.ID_ANY)
        self.notebook_2_pane_2 = wx.Panel(self.notebook_2, wx.ID_ANY)
        self.panel_model = wx.Panel(self.notebook_2_pane_2, wx.ID_ANY)
        self.notebook_2_Detail = wx.Panel(self.notebook_2, wx.ID_ANY)
        self.text_ctrl_detail = wx.TextCtrl(self.notebook_2_Detail, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.notebook_2_INPUT = wx.Panel(self.notebook_2, wx.ID_ANY)
        self.text_ctrl_input = wx.TextCtrl(self.notebook_2_INPUT, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.button_5 = wx.Button(self, wx.ID_ANY, "View Model")
        self.button_pre = wx.Button(self, wx.ID_ANY, "PREVIOUSE")
        self.button_9 = wx.Button(self, wx.ID_ANY, "NEXT")
        self.button_3 = wx.Button(self, wx.ID_ANY, "Run")
        self.button_4 = wx.Button(self, wx.ID_ANY, "Cancel")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.OnPlot, self.button_5)
        self.Bind(wx.EVT_BUTTON, self.OnPre, self.button_pre)
        self.Bind(wx.EVT_BUTTON, self.OnNext, self.button_9)
        self.Bind(wx.EVT_BUTTON, self.OnExec, self.button_3)
        self.Bind(wx.EVT_BUTTON, self.OnCancel, self.button_4)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("rigidWink")
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(wx.Bitmap("./images/plate.jpg", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.grid_model.CreateGrid(10, 7)
        self.grid_model.SetSelectionMode(wx.grid.Grid.SelectRows)
        self.grid_model.SetColLabelValue(0, "X1,m")
        self.grid_model.SetColLabelValue(1, "X2,m")
        self.grid_model.SetColLabelValue(2, "Y1,m")
        self.grid_model.SetColLabelValue(3, "Y2,m")
        self.grid_model.SetColLabelValue(4, "Dimx")
        self.grid_model.SetColLabelValue(5, "Dimy")
        self.grid_model.SetColLabelValue(6, "kb, kN/m3")
        self.grid_model.SetRowSize(5, 15)
        self.grid_load.CreateGrid(10, 4)
        self.grid_load.SetColLabelValue(0, "CASE")
        self.grid_load.SetColLabelValue(1, "N, kN")
        self.grid_load.SetColLabelValue(2, "Mx, kN.m")
        self.grid_load.SetColLabelValue(3, "My, kN.m")
        self.grid_comb.CreateGrid(10, 9)
        self.grid_comb.SetColLabelValue(0, "Label")
        self.grid_comb.SetColSize(0, 150)
        self.grid_comb.SetColLabelValue(1, "Load1")
        self.grid_comb.SetColLabelValue(2, "")
        self.grid_comb.SetColLabelValue(3, "Load2")
        self.grid_comb.SetColLabelValue(4, "")
        self.grid_comb.SetColLabelValue(5, "Load3")
        self.grid_comb.SetColLabelValue(6, "")
        self.grid_comb.SetColLabelValue(7, "Load4")
        self.grid_comb.SetColLabelValue(8, "")
        self.grid_ctln.CreateGrid(10, 2)
        self.grid_ctln.SetColLabelValue(0, "r, model")
        self.grid_ctln.SetColLabelValue(1, "r, uplift")
        self.notebook_1.SetMinSize((748, 250))
        self.text_ctrl_index.SetMinSize((50, -1))
        self.text_ctrl_total.SetMinSize((50, -1))
        self.notebook_2.SetMinSize((520, 520))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_13 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_12 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_9 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_10 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_11 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(self.grid_model, 1, wx.EXPAND, 0)
        self.notebook_1_model.SetSizer(sizer_3)
        sizer_7.Add(self.grid_load, 1, wx.EXPAND, 0)
        self.notebook_1_LOAD.SetSizer(sizer_7)
        sizer_8.Add(self.grid_comb, 1, wx.EXPAND, 0)
        self.notebook_1_COMB.SetSizer(sizer_8)
        sizer_4.Add(self.grid_ctln, 1, wx.EXPAND, 0)
        self.notebook_1_CTLN.SetSizer(sizer_4)
        self.notebook_1.AddPage(self.notebook_1_model, "MODEL")
        self.notebook_1.AddPage(self.notebook_1_LOAD, "LOAD")
        self.notebook_1.AddPage(self.notebook_1_COMB, "COMB")
        self.notebook_1.AddPage(self.notebook_1_CTLN, "CTLN")
        sizer_1.Add(self.notebook_1, 1, wx.EXPAND, 0)
        sizer_11.Add((100, 20), 0, 0, 0)
        sizer_11.Add(self.text_ctrl_index, 0, 0, 0)
        label_1 = wx.StaticText(self.panel_result, wx.ID_ANY, "/")
        sizer_11.Add(label_1, 0, 0, 0)
        sizer_11.Add(self.text_ctrl_total, 0, 0, 0)
        sizer_6.Add(sizer_11, 0, wx.EXPAND, 0)
        sizer_6.Add(self.text_ctrl_result, 1, wx.EXPAND, 0)
        self.panel_result.SetSizer(sizer_6)
        sizer_2.Add(self.panel_result, 1, wx.ALL | wx.EXPAND, 5)
        sizer_10.Add(self.panel_stress, 1, wx.EXPAND, 0)
        self.notebook_2_RESULT.SetSizer(sizer_10)
        sizer_9.Add(self.panel_model, 1, wx.EXPAND, 0)
        self.notebook_2_pane_2.SetSizer(sizer_9)
        sizer_12.Add(self.text_ctrl_detail, 1, wx.EXPAND, 0)
        self.notebook_2_Detail.SetSizer(sizer_12)
        sizer_13.Add(self.text_ctrl_input, 1, wx.EXPAND, 0)
        self.notebook_2_INPUT.SetSizer(sizer_13)
        self.notebook_2.AddPage(self.notebook_2_RESULT, "RESULT")
        self.notebook_2.AddPage(self.notebook_2_pane_2, "MODEL")
        self.notebook_2.AddPage(self.notebook_2_Detail, "DETAIL")
        self.notebook_2.AddPage(self.notebook_2_INPUT, "INPUT")
        sizer_2.Add(self.notebook_2, 3, wx.EXPAND, 0)
        sizer_1.Add(sizer_2, 5, wx.EXPAND, 0)
        static_line_1 = wx.StaticLine(self, wx.ID_ANY)
        sizer_1.Add(static_line_1, 0, wx.EXPAND, 0)
        sizer_5.Add((10, 20), 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_5.Add(self.button_5, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_5.Add((20, 20), 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_5.Add(self.button_pre, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_5.Add(self.button_9, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_5.Add((200, 20), 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_5.Add(self.button_3, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        sizer_5.Add(self.button_4, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        sizer_1.Add(sizer_5, 0, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        self.Centre()
        # end wxGlade

    def OnLoad(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'OnLoad' not implemented!")
        event.Skip()

    def Export_pdf(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'Export_pdf' not implemented!")
        event.Skip()

    def OnImport(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'OnImport' not implemented!")
        event.Skip()

    def OnSample(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'OnSample' not implemented!")
        event.Skip()

    def OnCancel(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'OnCancel' not implemented!")
        event.Skip()

    def OnPlot(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'OnPlot' not implemented!")
        event.Skip()

    def OnPre(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'OnPre' not implemented!")
        event.Skip()

    def OnNext(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'OnNext' not implemented!")
        event.Skip()

    def OnExec(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'OnExec' not implemented!")
        event.Skip()

# end of class MyFrame

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
