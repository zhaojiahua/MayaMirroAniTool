from functions import paywindow as pwind
from Globals import CurrentPath
from functions import copyfiles
from maya import cmds
import os
def onMayaDroppedPythonFile(obj):
    plugPath="C:/Users/{}/Documents/maya/2018".format(os.environ['USERNAME'])
    try:
        os.mkdir(plugPath+'/plug-ins')
    except:
        pass
    finally:
        oldpath=CurrentPath+'/mayaplugins'
        newpath=plugPath+'/plug-ins'
        copyfiles.CopyFiles(oldpath,newpath)
        cmds.loadPlugin('zjhIP2Code')
        cmds.loadPlugin('zjhIP2Series')
        pwind.paywin.CreateWin()
        pwind.paywin.ShowWin()