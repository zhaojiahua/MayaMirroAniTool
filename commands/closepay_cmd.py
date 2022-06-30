from functions import paywindow as pwind
from maya import cmds
import os
cmds.deleteUI(pwind.paywin.win_name)
cmds.unloadPlugin('zjhIP2Code')
cmds.unloadPlugin('zjhIP2Series')
plugPath="C:/Users/{}/Documents/maya/2018/plug-ins".format(os.environ['USERNAME'])
try:
    os.remove(plugPath+'/zjhIP2Series.mll')
    os.remove(plugPath+'/zjhIP2Code.mll')
finally:
    pass