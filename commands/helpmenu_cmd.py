from maya import cmds
from Globals import CurrentPath
help_win=cmds.window(title="helps on animation mirror",widthHeight=[930,620])
cmds.scrollLayout(bgc=[0.22,0.28,0.48])
cmds.rowLayout(numberOfColumns=3,columnAttach=[(1,'left',0),(2,'left',0),(3,'left',10)],bgc=[0.22,0.28,0.48])
cmds.text(label="mirror across YZ :")
cmds.image(image=CurrentPath+"/images/img1.png")
cmds.image(image=CurrentPath+"/images/img2.png")
cmds.setParent('..')
cmds.rowLayout(numberOfColumns=3,columnAttach=[(1,'left',0),(2,'left',0),(3,'left',10)],bgc=[0.22,0.28,0.48])
cmds.text(label="mirror across XY :")
cmds.image(image=CurrentPath+"/images/img3.png")
cmds.image(image=CurrentPath+"/images/img4.png")
cmds.setParent('..')
cmds.rowLayout(numberOfColumns=2,columnAttach=[(1,'left',0),(2,'left',150)],bgc=[0.22,0.28,0.48])
cmds.text(label="mirror across XZ :")
cmds.columnLayout()
cmds.image(image=CurrentPath+"/images/img1.png")
cmds.image(image=CurrentPath+"/images/img5.png")
cmds.showWindow()