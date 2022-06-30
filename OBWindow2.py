from maya import cmds
from Globals import CurrentPath
from functions import onesidetootherside as os2os
from functions import reversalbothside as rvebs
from functions import getcmdlines as gcls
class OBWindow2:
    def __init__(self):
        self.win_name="symmetry_animation_option"
        self.win_backColor=[0.2,0.2,0.25]
        self.win_widthHeight=[620,320]
        self.radiocollection1=None
        self.radiocollection2=None
        self.rb1=None
        self.rb2=None
        self.rb3=None
        self.rb4=None
        self.rb5=None
        self.reset_cmd_line=gcls.Getcmdlines(CurrentPath+'/commands/resetseting2.py')
        self.saveset_cmd_line=gcls.Getcmdlines(CurrentPath+'/commands/saveseting2.py')
        self.help_cmd_line=gcls.Getcmdlines(CurrentPath+'/commands/helpmenu_cmd.py')
        self.close_cmd_line=gcls.Getcmdlines(CurrentPath+'/commands/close_cmd2.py')
        self.apply_cmd_line=gcls.Getcmdlines(CurrentPath+'/commands/applysymmetry_cmd.py')
        self.select_rbs=None
    def CreateWin(self):
        if cmds.window(self.win_name,q=1,ex=1):
            cmds.deleteUI(self.win_name)
        cmds.window(self.win_name,title=self.win_name,widthHeight=self.win_widthHeight,backgroundColor=self.win_backColor,mb=1)
        cmds.menu("Edit")
        cmds.menuItem("Save Setting",c=self.saveset_cmd_line)
        cmds.menuItem("Reset Setting",c=self.reset_cmd_line)
        cmds.menuItem(d=1)
        cmds.menuItem("As Tool")
        cmds.menuItem("As Action")
        cmds.menu("Help",hm=1)
        cmds.menuItem("Help on Symmetry animation Option",c=self.help_cmd_line)

        cmds.scrollLayout(hst=16,vst=16,borderVisible=1,bgc=[0.21,0.21,0.25],childResizable=1)
        cmds.rowLayout(columnAttach=[[1,'left',100],[2,'both',20],[3,'right',20]],numberOfColumns=4,h=50,w=330,bgc=[0.26,0.22,0.25])
        cmds.text(label='Symmetry Direction :',al='center')
        self.radiocollection1=cmds.radioCollection(gl=1)
        self.rb1=cmds.radioButton(label='LtoR',collection=self.radiocollection1)
        self.rb2=cmds.radioButton(label='RtoL',collection=self.radiocollection1)
        self.rb3=cmds.radioButton(label='Both',collection=self.radiocollection1)
        cmds.setParent("..")
        cmds.rowLayout(columnAttach=[[1,'left',120],[2,'both',20],[3,'right',20]],numberOfColumns=2,h=50,w=330,bgc=[0.24,0.22,0.24])
        cmds.text(label='        Local Axis :',al='center')
        cmds.columnLayout()
        self.radiocollection2=cmds.radioCollection(gl=1)
        self.rb4=cmds.radioButton(label='opposite',collection=self.radiocollection2)
        self.rb5=cmds.radioButton(label='same',collection=self.radiocollection2)
        cmds.setParent("..")
        cmds.setParent("..")
        cmds.rowLayout(rowAttach=[[1,'top',80],[2,'top',80],[3,'top',80]],columnAttach=[[1,'left',10],[2,'both',30]],numberOfColumns=3)
        cmds.button(label='Symmetry',w=130,bgc=[0.24,0.24,0.3],c=self.apply_cmd_line)
        cmds.button(label='Apply',w=130,bgc=[0.24,0.24,0.3],c=self.apply_cmd_line)
        cmds.button(label='Close',w=130,bgc=[0.24,0.24,0.3],c=self.close_cmd_line)
        self.SetRadio([self.rb3,self.rb4])
    def Symmertry(self,direction,axissame,objs):
        if axissame=='opposite':
            axissame_index=0
        else:
            axissame_index=1
        if direction=='Both':
            rvebs.ReversalBothside(objs,axissame_index)
        else:
            os2os.OnesideToOtherside(objs,direction,axissame_index)
    def SetRadio(self,set_rbs):
        cmds.radioCollection(self.radiocollection1,edit=1,select=set_rbs[0])
        cmds.radioCollection(self.radiocollection2,edit=1,select=set_rbs[1])
    def QueryCollection(self):
        select_radio1=cmds.radioCollection(self.radiocollection1,q=1,select=1)
        select_radio2=cmds.radioCollection(self.radiocollection2,q=1,select=1)
        return select_radio1,select_radio2
    def Applysymmetry_cmd(self):
        objs=cmds.ls(sl=1)
        self.select_rbs=self.QueryCollection()
        direction=cmds.radioButton(self.select_rbs[0],q=1,label=1)
        axissame=cmds.radioButton(self.select_rbs[1],q=1,label=1)
        if objs:
            self.Symmertry(direction,axissame,objs)
            print("Symmertry animated curve successful!")
        else:
            cmds.inViewMessage(amg='please select at least an object with animated curves!', pos='midCenter',backColor=0x7B5353,fade=True,fadeInTime=0.2,fadeOutTime=0.2)
    def ShowWin(self):
        cmds.showWindow(self.win_name)

win2=OBWindow2()