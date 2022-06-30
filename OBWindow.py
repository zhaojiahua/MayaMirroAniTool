from maya import cmds
from Globals import CurrentPath
from functions import mirroracross as mar
from functions import getcmdlines as gcls
class OBWindow:
    def __init__(self):
        self.win_name="mirror_animation_option"
        self.win_backColor=[0.2,0.2,0.25]
        self.win_widthHeight=[620,530]
        self.radiocollection1=None
        self.radiocollection2=None
        self.radiocollection3=None
        self.rb1=None
        self.rb2=None
        self.rb3=None
        self.rb4=None
        self.rb5=None
        self.rb6=None
        self.rb7=None
        self.rb8=None
        self.rb9=None
        self.rb10=None
        self.rb11=None
        self.reset_cmd_line=gcls.Getcmdlines(CurrentPath+'/commands/resetseting.py')
        self.saveset_cmd_line=gcls.Getcmdlines(CurrentPath+'/commands/saveseting.py')
        self.help_cmd_line=gcls.Getcmdlines(CurrentPath+'/commands/helpmenu_cmd.py')
        self.close_cmd_line=gcls.Getcmdlines(CurrentPath+'/commands/close_cmd.py')
        self.apply_cmd_line=gcls.Getcmdlines(CurrentPath+'/commands/applymirror_cmd.py')
        self.select_rbs=[]
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
        cmds.menuItem("Help on Mirror animation Option",c=self.help_cmd_line)

        cmds.scrollLayout(hst=16,vst=16,borderVisible=1,bgc=[0.21,0.21,0.24])
        cmds.columnLayout(columnAttach=("both",10),rowSpacing=20,columnWidth=560,h=280)
        cmds.rowLayout(columnAttach=[[1,'left',100],[2,'both',20],[3,'right',20]],numberOfColumns=4,h=50,bgc=[0.22,0.22,0.25])
        cmds.text(label='Mirror across :',al='center')
        self.radiocollection1=cmds.radioCollection(gl=1)
        self.rb1=cmds.radioButton(label='XY',collection=self.radiocollection1)
        self.rb2=cmds.radioButton(label='YZ',collection=self.radiocollection1)
        self.rb3=cmds.radioButton(label='XZ',collection=self.radiocollection1)
        cmds.setParent("..")
        cmds.rowLayout(columnAttach=[[1,'left',120],[2,'both',20]],numberOfColumns=3,h=50,bgc=[0.22,0.22,0.25])
        cmds.text(label='Direction :')
        cmds.columnLayout()
        self.radiocollection2=cmds.radioCollection(gl=1)
        self.rb4=cmds.radioButton(label='Stay at Local',collection=self.radiocollection2)
        self.rb5=cmds.radioButton(label='mirror across world',collection=self.radiocollection2)
        cmds.setParent("..")
        cmds.setParent("..")
        cmds.rowLayout(columnAttach=[[1,'left',70],[2,'both',30]],rat=[[1,'top',55],[2,'top',10]],numberOfColumns=2,h=200,bgc=[0.25,0.23,0.27])
        cmds.text(label='Local Axis Direction :',al='center')
        cmds.columnLayout()
        self.radiocollection3=cmds.radioCollection(gl=1)
        self.rb6=cmds.radioButton(label='XYZ',collection=self.radiocollection3)
        self.rb7=cmds.radioButton(label='XZY',collection=self.radiocollection3)
        self.rb8=cmds.radioButton(label='YXZ',collection=self.radiocollection3)
        self.rb9=cmds.radioButton(label='YZX',collection=self.radiocollection3)
        self.rb10=cmds.radioButton(label='ZXY',collection=self.radiocollection3)
        self.rb11=cmds.radioButton(label='ZYX',collection=self.radiocollection3)
        cmds.setParent("..")
        cmds.setParent("..")
        cmds.setParent("..")
        cmds.columnLayout(columnAttach=("both",10),rowSpacing=10,columnWidth=500,h=100)
        cmds.rowLayout(rowAttach=[[1,'top',60],[2,'top',60],[3,'top',60]],columnAttach=[[1,'left',10],[2,'both',30]],numberOfColumns=3)
        cmds.button(label='Mirror',w=130,bgc=[0.24,0.24,0.3],c=self.apply_cmd_line)
        cmds.button(label='Apply',w=130,bgc=[0.24,0.24,0.3],c=self.apply_cmd_line)
        cmds.button(label='Close',w=130,bgc=[0.24,0.24,0.3],c=self.close_cmd_line)
        self.select_rbs=[self.rb2,self.rb4,self.rb6]
        self.SetRadio(self.rb2,self.rb4,self.rb6)
    def Across(self,plan,localaxis,objs):
        if plan=='XY':
            mar.AcrossXY(objs,localaxis)
        elif plan=='YZ':
            mar.AcrossYZ(objs,localaxis)
        else:
            mar.AcrossXZ(objs,localaxis)
    def SetRadio(self,set_rb1,set_rb2,set_rb6):
        cmds.radioCollection(self.radiocollection1,edit=1,select=set_rb1)
        cmds.radioCollection(self.radiocollection2,edit=1,select=set_rb2)
        cmds.radioCollection(self.radiocollection3,edit=1,select=set_rb6)
    def QueryCollection(self):
        select_radio1=cmds.radioCollection(self.radiocollection1,q=1,select=1)
        select_radio2=cmds.radioCollection(self.radiocollection2,q=1,select=1)
        select_radio3=cmds.radioCollection(self.radiocollection3,q=1,select=1)
        return [select_radio1,select_radio2,select_radio3]
    def Applymirro_cmd(self):
        objs=cmds.ls(sl=1)
        self.select_rbs=self.QueryCollection()
        plan=cmds.radioButton(self.select_rbs[0],q=1,label=1)
        localaxis=cmds.radioButton(self.select_rbs[2],q=1,label=1)
        if objs:
            self.Across(plan,localaxis,objs)
            print("mirror animated curve successful!")
        else:
            cmds.inViewMessage(amg='please select at least an object with animated curves!', pos='midCenter',backColor=0x7B5353,fade=True,fadeInTime=0.2,fadeOutTime=0.2)
    def ShowWin(self):
        cmds.showWindow(self.win_name)

win=OBWindow()