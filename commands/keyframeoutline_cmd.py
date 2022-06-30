from maya import cmds
sl_objs=cmds.ls(sl=1)
if len(sl_objs):
	find_curves=cmds.findKeyframe(sl_objs[-1],curve=True)
	if find_curves is None:
		cmds.inViewMessage(amg='have no animated curves on {}'.format(sl_objs[-1]), pos='midCenter',backColor=0x8B5353,fade=True,fadeInTime=0.2,fadeOutTime=0.2)
	else:
		if cmds.window('keyFrameOutlineWindow',q=1,exists=1):
			cmds.deleteUI('keyFrameOutlineWindow',window=1)
		cmds.window('keyFrameOutlineWindow', width=1080, height=800)
		cmds.scrollLayout('scrolllayout',borderVisible=1,width=850,bgc=[0.25,0.33,0.3])
		cmds.rowLayout('rowlayout',numberOfColumns=len(find_curves),width=830*len(find_curves))
		for find_curve in find_curves:
			cmds.columnLayout()
			cmds.text(label=find_curve+' outline',width=820,height=20,bgc=[0.5,0.45,0.5])
			cmds.keyframeOutliner('myOutliner', animCurve=find_curve,statusBarMessage=find_curve+' outline',width=820,height=800)
			cmds.setParent('..')
		cmds.showWindow('keyFrameOutlineWindow')
        print('keyFrameOutlineWindow')
else:
	cmds.inViewMessage(amg='please select an object with animated curves!', pos='midCenter',backColor=0x7B5353,fade=True,fadeInTime=0.2,fadeOutTime=0.2)
