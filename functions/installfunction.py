from maya import cmds as cmds
from maya import mel as mel
import os
from OBWindow import OBWindow
from OBWindow2 import OBWindow2
from functions import mirroracross
from functions import reversalbothside
from functions import onesidetootherside
from functions import getcmdlines as gcls
from Globals import CurrentPath,zjhmenu,setupPath
def ZJHInstall():
	mainWindow_py=mel.eval("$tempMelVar=$gMainWindow")
	mainWindowMenuList=cmds.window(mainWindow_py,q=1,menuArray=1)
	subWin_command_line=gcls.Getcmdlines(CurrentPath+"/commands/subWin_command.py")
	subWin2_command_line=gcls.Getcmdlines(CurrentPath+"/commands/subWin2_command.py")
	keyframeoutline_cmd_line=gcls.Getcmdlines(CurrentPath+"/commands/keyframeoutline_cmd.py")
	apply_cmd_line=gcls.Getcmdlines(CurrentPath+"/commands/applymirror_direct_cmd.py")
	applysymmetry_cmd_line=gcls.Getcmdlines(CurrentPath+"/commands/applysymmetry_direct_cmd.py")
	advautomirror_cmd_line=gcls.Getcmdlines(CurrentPath+"/commands/advautomirror_cmd.py")
	uninstall_cmd_line=gcls.Getcmdlines(CurrentPath+"/commands/uninstallfunction_cmd.py")
	if zjhmenu not in mainWindowMenuList:
		cmds.menu(zjhmenu,p=mainWindow_py,tearOff=1)
		cmds.menuItem(d=1)
		cmds.menuItem('mirror animation',c=apply_cmd_line,stp='python')
		cmds.menuItem(ob=1,c=subWin_command_line)
		cmds.menuItem('symmetry animation',c=applysymmetry_cmd_line,stp='python')
		cmds.menuItem(ob=1,c=subWin2_command_line)
		cmds.menuItem('ADV AutoMirrorAcrossYZ',c=advautomirror_cmd_line,stp='python')
		cmds.menuItem(d=1)
		cmds.menuItem('open keyFrameOutlines',c=keyframeoutline_cmd_line,stp='python')
		cmds.menuItem(d=1)
		cmds.menuItem('Uninstall',c=uninstall_cmd_line,stp='python')
		cmds.menuItem(d=1)
		cmds.menuItem('usage note')
		cmds.inViewMessage(amg='{} is been installed succeefully!'.format(zjhmenu), pos='midCenter',backColor=0x5B8373,fade=True,fadeInTime=0.5,fadeOutTime=0.2)
def Uninstall():
    result=cmds.promptDialog(title='Uninstall {}'.format(zjhmenu)
                        ,message='You will abandon {}! Yes or No'.format(zjhmenu)
                        ,button=['Yes', 'Cancel']
                        ,defaultButton='Yes'
                        ,cancelButton='Cancel'
                        ,dismissString='Cancel')
    if result=='Yes':
        cmds.deleteUI(zjhmenu)
        with open(CurrentPath+'/functions/userSetuptoscripts.py','r') as f:
    		setup_contents=[line.format(CurrentPath) for line in f.readlines()]
        with open(setupPath+"/userSetup.py",'r') as f_r:
        	old_lines=f_r.readlines()
        with open(setupPath+"/userSetup.py",'w') as f_w:
        	for line in old_lines:
        		if line in setup_contents:
        			continue
    			f_w.write(line)
	cmds.unloadPlugin('zjhIP2Code')
    cmds.unloadPlugin('zjhIP2Series')
    plugPath="C:/Users/{}/Documents/maya/2018/plug-ins".format(os.environ['USERNAME'])
    os.remove(plugPath+'/zjhIP2Series.mll')
    os.remove(plugPath+'/zjhIP2Code.mll')