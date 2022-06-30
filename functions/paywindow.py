from maya import cmds
import os
from Globals import CurrentPath,setupPath,hostIP
from functions import getcmdlines as gcls
from functions import installfunction as istf
class PayWindow:
    def __init__(self):
        self.win_name="pay_window"
        self.win_backColor=[0.25,0.28,0.25]
        self.win_widthHeight=[345,540]
        self.text=None
        self.check_cmd_line=gcls.Getcmdlines(CurrentPath+'/commands/check_cmd.py')
        self.close_cmd_line=gcls.Getcmdlines(CurrentPath+'/commands/closepay_cmd.py')
    def CreateWin(self):
        if cmds.window(self.win_name,q=1,ex=1):
            cmds.deleteUI(self.win_name)
        cmds.window(self.win_name,title=self.win_name,widthHeight=self.win_widthHeight,backgroundColor=self.win_backColor)
        cmds.scrollLayout(hst=16,vst=16,borderVisible=1,bgc=[0.21,0.24,0.23],childResizable=2)
        cmds.image(image=CurrentPath+'/images/payimage/gongzhonghao.jpg')
        cmds.rowLayout(rowAttach=[[1,'both',12],[2,'both',12]],columnAttach=[[1,'left',10],[2,'both',2]],numberOfColumns=2)
        cmds.text(label='serial number:')
        cmds.textField(text=cmds.zjhIP2Series(hostIP),editable=0,font='fixedWidthFont',w=190,ann="It's about your PC IP")
        cmds.setParent("..")
        cmds.rowLayout(rowAttach=[[1,'both',15],[2,'both',15]],columnAttach=[[1,'left',10],[2,'both',10]],numberOfColumns=2)
        cmds.button(label="OK",w=115,h=30,bgc=[0.24,0.28,0.28],c=self.check_cmd_line)
        cmds.button(label='Close',w=115,h=30,bgc=[0.24,0.28,0.28],c=self.close_cmd_line)
    def ShowWin(self):
        cmds.showWindow(self.win_name)
    def InstallPlug(self):
        auth_code=cmds.zjhIP2Code(hostIP)
        if self.text != auth_code:
            while self.text != auth_code:
                cmds.inViewMessage(amg="please enter the valid code", pos='midCenter',backColor=0xB55353,fade=True,fadeInTime=0.5,fadeOutTime=0.2)
                result=cmds.promptDialog(title='Check_auth_code'
                            ,message='Enter a valid verification code please!'
                            ,button=['OK', 'Cancel']
                            ,defaultButton='OK'
                            ,cancelButton='Cancel'
                            ,dismissString='Cancel')
                if result == 'OK':
                    self.text = cmds.promptDialog(query=True, text=True)
                else:
                    cmds.unloadPlugin('zjhIP2Code')
                    cmds.unloadPlugin('zjhIP2Series')
                    plugPath="C:/Users/{}/Documents/maya/2018/plug-ins".format(os.environ['USERNAME'])
                    try:
                        os.remove(plugPath+'/zjhIP2Series.mll')
                        os.remove(plugPath+'/zjhIP2Code.mll')
                    finally:
                        break
        if self.text==auth_code:
            istf.ZJHInstall()
            with open(CurrentPath+'/functions/userSetuptoscripts.py','r') as f:
                setup_contents=f.read()
            with open(setupPath+'/userSetup.py','a+') as f:
                f.write(setup_contents.format(CurrentPath))
paywin=PayWindow()