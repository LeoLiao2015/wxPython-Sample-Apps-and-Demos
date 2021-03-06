#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports----------------------------------------------------------------------

#--wxPython Imports.
import wx


#- wxPython Demo --------------------------------------------------------------
__wxPyOnlineDocs__ = 'https://wxpython.org/Phoenix/docs/html/wx.ProgressDialog.html'
__wxPyDemoPanel__ = 'TestPanel'

overview = """\
<html><body>
<center><h2>wx.ProgressDialog</h2></center>
This class represents a dialog that shows a short message and a progress bar.
Optionally, it can display an ABORT button
<p>
This dialog indicates the progress of some event that takes a while to
accomplish, usually, such as file copy progress, download progress, and so on.
The display is <b>completely</b> under control of the program; you must update
the dialog from within the program creating it.
<p>
When the dialog closes, you must check to see if the user aborted the process
or not, and act accordingly -- that is, if the PD_CAN_ABORT style flag is set.
If not then you may progress blissfully onward.
</body></html>
"""


class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        self.log = log
        wx.Panel.__init__(self, parent, -1)

        b = wx.Button(self, -1, "Create and Show a ProgressDialog", (50, 50))
        self.Bind(wx.EVT_BUTTON, self.OnButton, b)


    def OnButton(self, event):
        max = 80

        dlg = wx.ProgressDialog("Progress dialog example",
                                "An informative message",
                                maximum=max,
                                parent=self,
                                style=0
                                    | wx.PD_APP_MODAL
                                    | wx.PD_CAN_ABORT
                                    ## | wx.PD_CAN_SKIP
                                    ## | wx.PD_ELAPSED_TIME
                                    | wx.PD_ESTIMATED_TIME
                                    | wx.PD_REMAINING_TIME
                                    ## | wx.PD_AUTO_HIDE
                                    )

        keepGoing = True
        count = 0

        while keepGoing and count < max:
            count += 1
            wx.MilliSleep(250)
            wx.Yield()

            if count >= max / 2:
                (keepGoing, skip) = dlg.Update(count, "Half-time!")
            else:
                (keepGoing, skip) = dlg.Update(count)


        dlg.Destroy()


#- wxPy Demo -----------------------------------------------------------------


def runTest(frame, nb, log):
    win = TestPanel(nb, log)
    return win


#- __main__ Demo --------------------------------------------------------------


class printLog:
    def __init__(self):
        pass

    def write(self, txt):
        print('%s' % txt)

    def WriteText(self, txt):
        print('%s' % txt)


class TestFrame(wx.Frame):
    def __init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString,
                 pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.DEFAULT_FRAME_STYLE, name='frame'):
        wx.Frame.__init__(self, parent, id, title, pos, size, style, name)

        log = printLog()

        panel = TestPanel(self, log)
        self.Bind(wx.EVT_CLOSE, self.OnDestroy)


    def OnDestroy(self, event):
        self.Destroy()


class TestApp(wx.App):
    def OnInit(self):
        gMainWin = TestFrame(None)
        gMainWin.SetTitle('Test Demo')
        gMainWin.Show()

        return True


#- __main__ -------------------------------------------------------------------


if __name__ == '__main__':
    import sys
    print('Python %s.%s.%s %s' % sys.version_info[0:4])
    print('wxPython %s' % wx.version())
    gApp = TestApp(redirect=False,
            filename=None,
            useBestVisual=False,
            clearSigInt=True)

    gApp.MainLoop()
