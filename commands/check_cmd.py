from functions import paywindow as pwind
from maya import cmds
pwind.paywin.InstallPlug()
cmds.deleteUI(pwind.paywin.win_name)