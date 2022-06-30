from maya import cmds
def Across_yz(objs):
	for obj in objs:
		find_curves=cmds.findKeyframe(obj,curve=True)
		if find_curves is None:
			cmds.inViewMessage(amg='have no animated curves on {},please set the keyframe!'.format(obj), pos='midCenter',backColor=0x8B5353,fade=True,fadeInTime=0.2,fadeOutTime=0.2)
		else:
			tx_values=cmds.keyframe(obj,q=1,attribute='translateX',valueChange=1)
			tx_intangent_types=cmds.keyTangent(obj,q=1,attribute='translateX',inTangentType=1)
			tx_intangents=cmds.keyTangent(obj,q=1,attribute='translateX',inAngle=1)
			tx_intangent_weights=cmds.keyTangent(obj,q=1,attribute='translateX',inWeight=1)
			tx_outtangent_types=cmds.keyTangent(obj,q=1,attribute='translateX',outTangentType=1)
			tx_outtangents=cmds.keyTangent(obj,q=1,attribute='translateX',outAngle=1)
			tx_outtangent_weights=cmds.keyTangent(obj,q=1,attribute='translateX',outWeight=1)
			
			ry_values=cmds.keyframe(obj,q=1,attribute='rotateY',valueChange=1)
			ry_intangent_types=cmds.keyTangent(obj,q=1,attribute='rotateY',inTangentType=1)
			ry_intangents=cmds.keyTangent(obj,q=1,attribute='rotateY',inAngle=1)
			ry_intangent_weights=cmds.keyTangent(obj,q=1,attribute='rotateY',inWeight=1)
			ry_outtangent_types=cmds.keyTangent(obj,q=1,attribute='rotateY',outTangentType=1)
			ry_outtangents=cmds.keyTangent(obj,q=1,attribute='rotateY',outAngle=1)
			ry_outtangent_weights=cmds.keyTangent(obj,q=1,attribute='rotateY',outWeight=1)
			
			rz_values=cmds.keyframe(obj,q=1,attribute='rotateZ',valueChange=1)
			rz_intangent_types=cmds.keyTangent(obj,q=1,attribute='rotateZ',inTangentType=1)
			rz_intangents=cmds.keyTangent(obj,q=1,attribute='rotateZ',inAngle=1)
			rz_intangent_weights=cmds.keyTangent(obj,q=1,attribute='rotateZ',inWeight=1)
			rz_outtangent_types=cmds.keyTangent(obj,q=1,attribute='rotateZ',outTangentType=1)
			rz_outtangents=cmds.keyTangent(obj,q=1,attribute='rotateZ',outAngle=1)
			rz_outtangent_weights=cmds.keyTangent(obj,q=1,attribute='rotateZ',outWeight=1)
			if tx_values is None:
				cmds.inViewMessage(amg='have no animated curves on {}_tx,please set the keyframe!'.format(obj), pos='midCenter',backColor=0x8B5353,fade=True,fadeInTime=0.2,fadeOutTime=0.2)
			else:
				tmp_i=0
				for tmp_i in range(len(tx_values)):
					tx_value=tx_values[tmp_i]*-1
					tx_intangent_type=tx_intangent_types[tmp_i]
					tx_intangent=tx_intangents[tmp_i]*-1
					tx_intangent_weight=tx_intangent_weights[tmp_i]
					tx_outtangent_type=tx_outtangent_types[tmp_i]
					tx_outtangent=tx_outtangents[tmp_i]*-1
					tx_outtangent_weight=tx_outtangent_weights[tmp_i]
					cmds.keyframe(obj,edit=1,attribute='translateX',index=(tmp_i,tmp_i),valueChange=tx_value)
					cmds.keyTangent(obj,edit=1,attribute='translateX',index=(tmp_i,tmp_i)
											,inTangentType=tx_intangent_type
											,inAngle=tx_intangent
											,inWeight=tx_intangent_weight
											,outTangentType=tx_outtangent_type
											,outAngle=tx_outtangent
											,outWeight=tx_outtangent_weight)
			if ry_values is None:
				cmds.inViewMessage(amg='have no animated curves on {}_ry,please set the keyframe!'.format(obj), pos='midCenter',backColor=0x8B5353,fade=True,fadeInTime=0.2,fadeOutTime=0.2)
			else:
				tmp_i=0
				for tmp_i in range(len(ry_values)):
					ry_value=ry_values[tmp_i]*-1
					ry_intangent_type=ry_intangent_types[tmp_i]
					ry_intangent=ry_intangents[tmp_i]*-1
					ry_intangent_weight=ry_intangent_weights[tmp_i]
					ry_outtangent_type=ry_outtangent_types[tmp_i]
					ry_outtangent=ry_outtangents[tmp_i]*-1
					ry_outtangent_weight=ry_outtangent_weights[tmp_i]
					cmds.keyframe(obj,edit=1,attribute='rotateY',index=(tmp_i,tmp_i),valueChange=ry_value)
					cmds.keyTangent(obj,edit=1,attribute='rotateY',index=(tmp_i,tmp_i)
											,inTangentType=ry_intangent_type
											,inAngle=ry_intangent
											,inWeight=ry_intangent_weight
											,outTangentType=ry_outtangent_type
											,outAngle=ry_outtangent
											,outWeight=ry_outtangent_weight)
			if rz_values is None:
				cmds.inViewMessage(amg='have no animated curves on {}_rz,please set the keyframe!'.format(obj), pos='midCenter',backColor=0x8B5353,fade=True,fadeInTime=0.2,fadeOutTime=0.2)
			else:
				tmp_i=0
				for tmp_i in range(len(rz_values)):
					rz_value=rz_values[tmp_i]*-1
					rz_intangent_type=rz_intangent_types[tmp_i]
					rz_intangent=rz_intangents[tmp_i]*-1
					rz_intangent_weight=rz_intangent_weights[tmp_i]
					rz_outtangent_type=rz_outtangent_types[tmp_i]
					rz_outtangent=rz_outtangents[tmp_i]*-1
					rz_outtangent_weight=rz_outtangent_weights[tmp_i]
					cmds.keyframe(obj,edit=1,attribute='rotateZ',index=(tmp_i,tmp_i),valueChange=rz_value)
					cmds.keyTangent(obj,edit=1,attribute='rotateZ',index=(tmp_i,tmp_i)
											,inTangentType=rz_intangent_type
											,inAngle=rz_intangent
											,inWeight=rz_intangent_weight
											,outTangentType=rz_outtangent_type
											,outAngle=rz_outtangent
											,outWeight=rz_outtangent_weight)
def Across_xz(objs):
	for obj in objs:
		find_curves=cmds.findKeyframe(obj,curve=True)
		if find_curves is None:
			cmds.inViewMessage(amg='have no animated curves on {},please set the keyframe!'.format(obj), pos='midCenter',backColor=0x8B5353,fade=True,fadeInTime=0.2,fadeOutTime=0.2)
		else:
			ty_values=cmds.keyframe(obj,q=1,attribute='translateY',valueChange=1)
			ty_intangent_types=cmds.keyTangent(obj,q=1,attribute='translateY',inTangentType=1)
			ty_intangents=cmds.keyTangent(obj,q=1,attribute='translateY',inAngle=1)
			ty_intangent_weights=cmds.keyTangent(obj,q=1,attribute='translateY',inWeight=1)
			ty_outtangent_types=cmds.keyTangent(obj,q=1,attribute='translateY',outTangentType=1)
			ty_outtangents=cmds.keyTangent(obj,q=1,attribute='translateY',outAngle=1)
			ty_outtangent_weights=cmds.keyTangent(obj,q=1,attribute='translateY',outWeight=1)
			
			rx_values=cmds.keyframe(obj,q=1,attribute='rotateX',valueChange=1)
			rx_intangent_types=cmds.keyTangent(obj,q=1,attribute='rotateX',inTangentType=1)
			rx_intangents=cmds.keyTangent(obj,q=1,attribute='rotateX',inAngle=1)
			rx_intangent_weights=cmds.keyTangent(obj,q=1,attribute='rotateX',inWeight=1)
			rx_outtangent_types=cmds.keyTangent(obj,q=1,attribute='rotateX',outTangentType=1)
			rx_outtangents=cmds.keyTangent(obj,q=1,attribute='rotateX',outAngle=1)
			rx_outtangent_weights=cmds.keyTangent(obj,q=1,attribute='rotateX',outWeight=1)
			
			rz_values=cmds.keyframe(obj,q=1,attribute='rotateZ',valueChange=1)
			rz_intangent_types=cmds.keyTangent(obj,q=1,attribute='rotateZ',inTangentType=1)
			rz_intangents=cmds.keyTangent(obj,q=1,attribute='rotateZ',inAngle=1)
			rz_intangent_weights=cmds.keyTangent(obj,q=1,attribute='rotateZ',inWeight=1)
			rz_outtangent_types=cmds.keyTangent(obj,q=1,attribute='rotateZ',outTangentType=1)
			rz_outtangents=cmds.keyTangent(obj,q=1,attribute='rotateZ',outAngle=1)
			rz_outtangent_weights=cmds.keyTangent(obj,q=1,attribute='rotateZ',outWeight=1)
			if ty_values is None:
				cmds.inViewMessage(amg='have no animated curves on {}_ty,please set the keyframe!'.format(obj), pos='midCenter',backColor=0x8B5353,fade=True,fadeInTime=0.2,fadeOutTime=0.2)
			else:
				tmp_i=0
				for tmp_i in range(len(ty_values)):
					ty_value=ty_values[tmp_i]*-1
					ty_intangent_type=ty_intangent_types[tmp_i]
					ty_intangent=ty_intangents[tmp_i]*-1
					ty_intangent_weight=ty_intangent_weights[tmp_i]
					ty_outtangent_type=ty_outtangent_types[tmp_i]
					ty_outtangent=ty_outtangents[tmp_i]*-1
					ty_outtangent_weight=ty_outtangent_weights[tmp_i]
					cmds.keyframe(obj,edit=1,attribute='translateY',index=(tmp_i,tmp_i),valueChange=ty_value)
					cmds.keyTangent(obj,edit=1,attribute='translateY',index=(tmp_i,tmp_i)
											,inTangentType=ty_intangent_type
											,inAngle=ty_intangent
											,inWeight=ty_intangent_weight
											,outTangentType=ty_outtangent_type
											,outAngle=ty_outtangent
											,outWeight=ty_outtangent_weight)
			if rx_values is None:
				cmds.inViewMessage(amg='have no animated curves on {}_rx,please set the keyframe!'.format(obj), pos='midCenter',backColor=0x8B5353,fade=True,fadeInTime=0.2,fadeOutTime=0.2)
			else:
				tmp_i=0
				for tmp_i in range(len(rx_values)):
					rx_value=rx_values[tmp_i]*-1
					rx_intangent_type=rx_intangent_types[tmp_i]
					rx_intangent=rx_intangents[tmp_i]*-1
					rx_intangent_weight=rx_intangent_weights[tmp_i]
					rx_outtangent_type=rx_outtangent_types[tmp_i]
					rx_outtangent=rx_outtangents[tmp_i]*-1
					rx_outtangent_weight=rx_outtangent_weights[tmp_i]
					cmds.keyframe(obj,edit=1,attribute='rotateX',index=(tmp_i,tmp_i),valueChange=rx_value)
					cmds.keyTangent(obj,edit=1,attribute='rotateX',index=(tmp_i,tmp_i)
											,inTangentType=rx_intangent_type
											,inAngle=rx_intangent
											,inWeight=rx_intangent_weight
											,outTangentType=rx_outtangent_type
											,outAngle=rx_outtangent
											,outWeight=rx_outtangent_weight)
			if rz_values is None:
				cmds.inViewMessage(amg='have no animated curves on {}_rz,please set the keyframe!'.format(obj), pos='midCenter',backColor=0x8B5353,fade=True,fadeInTime=0.2,fadeOutTime=0.2)
			else:
				tmp_i=0
				for tmp_i in range(len(rz_values)):
					rz_value=rz_values[tmp_i]*-1
					rz_intangent_type=rz_intangent_types[tmp_i]
					rz_intangent=rz_intangents[tmp_i]*-1
					rz_intangent_weight=rz_intangent_weights[tmp_i]
					rz_outtangent_type=rz_outtangent_types[tmp_i]
					rz_outtangent=rz_outtangents[tmp_i]*-1
					rz_outtangent_weight=rz_outtangent_weights[tmp_i]
					cmds.keyframe(obj,edit=1,attribute='rotateZ',index=(tmp_i,tmp_i),valueChange=rz_value)
					cmds.keyTangent(obj,edit=1,attribute='rotateZ',index=(tmp_i,tmp_i)
											,inTangentType=rz_intangent_type
											,inAngle=rz_intangent
											,inWeight=rz_intangent_weight
											,outTangentType=rz_outtangent_type
											,outAngle=rz_outtangent
											,outWeight=rz_outtangent_weight)
def Across_xy(objs):
	for obj in objs:
		find_curves=cmds.findKeyframe(obj,curve=True)
		if find_curves is None:
			cmds.inViewMessage(amg='have no animated curves on {},please set the keyframe!'.format(obj), pos='midCenter',backColor=0x8B5353,fade=True,fadeInTime=0.2,fadeOutTime=0.2)
		else:
			tz_values=cmds.keyframe(obj,q=1,attribute='translateZ',valueChange=1)
			tz_intangent_types=cmds.keyTangent(obj,q=1,attribute='translateZ',inTangentType=1)
			tz_intangents=cmds.keyTangent(obj,q=1,attribute='translateZ',inAngle=1)
			tz_intangent_weights=cmds.keyTangent(obj,q=1,attribute='translateZ',inWeight=1)
			tz_outtangent_types=cmds.keyTangent(obj,q=1,attribute='translateZ',outTangentType=1)
			tz_outtangents=cmds.keyTangent(obj,q=1,attribute='translateZ',outAngle=1)
			tz_outtangent_weights=cmds.keyTangent(obj,q=1,attribute='translateZ',outWeight=1)
			
			rx_values=cmds.keyframe(obj,q=1,attribute='rotateX',valueChange=1)
			rx_intangent_types=cmds.keyTangent(obj,q=1,attribute='rotateX',inTangentType=1)
			rx_intangents=cmds.keyTangent(obj,q=1,attribute='rotateX',inAngle=1)
			rx_intangent_weights=cmds.keyTangent(obj,q=1,attribute='rotateX',inWeight=1)
			rx_outtangent_types=cmds.keyTangent(obj,q=1,attribute='rotateX',outTangentType=1)
			rx_outtangents=cmds.keyTangent(obj,q=1,attribute='rotateX',outAngle=1)
			rx_outtangent_weights=cmds.keyTangent(obj,q=1,attribute='rotateX',outWeight=1)
			
			ry_values=cmds.keyframe(obj,q=1,attribute='rotateY',valueChange=1)
			ry_intangent_types=cmds.keyTangent(obj,q=1,attribute='rotateY',inTangentType=1)
			ry_intangents=cmds.keyTangent(obj,q=1,attribute='rotateY',inAngle=1)
			ry_intangent_weights=cmds.keyTangent(obj,q=1,attribute='rotateY',inWeight=1)
			ry_outtangent_types=cmds.keyTangent(obj,q=1,attribute='rotateY',outTangentType=1)
			ry_outtangents=cmds.keyTangent(obj,q=1,attribute='rotateY',outAngle=1)
			ry_outtangent_weights=cmds.keyTangent(obj,q=1,attribute='rotateY',outWeight=1)
			if tz_values is None:
				cmds.inViewMessage(amg='have no animated curves on {}_tz,please set the keyframe!'.format(obj), pos='midCenter',backColor=0x8B5353,fade=True,fadeInTime=0.2,fadeOutTime=0.2)
			else:
				tmp_i=0
				for tmp_i in range(len(tz_values)):
					tz_value=tz_values[tmp_i]*-1
					tz_intangent_type=tz_intangent_types[tmp_i]
					tz_intangent=tz_intangents[tmp_i]*-1
					tz_intangent_weight=tz_intangent_weights[tmp_i]
					tz_outtangent_type=tz_outtangent_types[tmp_i]
					tz_outtangent=tz_outtangents[tmp_i]*-1
					tz_outtangent_weight=tz_outtangent_weights[tmp_i]
					cmds.keyframe(obj,edit=1,attribute='translateZ',index=(tmp_i,tmp_i),valueChange=tz_value)
					cmds.keyTangent(obj,edit=1,attribute='translateZ',index=(tmp_i,tmp_i)
											,inTangentType=tz_intangent_type
											,inAngle=tz_intangent
											,inWeight=tz_intangent_weight
											,outTangentType=tz_outtangent_type
											,outAngle=tz_outtangent
											,outWeight=tz_outtangent_weight)
			if rx_values is None:
				cmds.inViewMessage(amg='have no animated curves on {}_rx,please set the keyframe!'.format(obj), pos='midCenter',backColor=0x8B5353,fade=True,fadeInTime=0.2,fadeOutTime=0.2)
			else:
				tmp_i=0
				for tmp_i in range(len(rx_values)):
					rx_value=rx_values[tmp_i]*-1
					rx_intangent_type=rx_intangent_types[tmp_i]
					rx_intangent=rx_intangents[tmp_i]*-1
					rx_intangent_weight=rx_intangent_weights[tmp_i]
					rx_outtangent_type=rx_outtangent_types[tmp_i]
					rx_outtangent=rx_outtangents[tmp_i]*-1
					rx_outtangent_weight=rx_outtangent_weights[tmp_i]
					cmds.keyframe(obj,edit=1,attribute='rotateX',index=(tmp_i,tmp_i),valueChange=rx_value)
					cmds.keyTangent(obj,edit=1,attribute='rotateX',index=(tmp_i,tmp_i)
											,inTangentType=rx_intangent_type
											,inAngle=rx_intangent
											,inWeight=rx_intangent_weight
											,outTangentType=rx_outtangent_type
											,outAngle=rx_outtangent
											,outWeight=rx_outtangent_weight)
			if ry_values is None:
				cmds.inViewMessage(amg='have no animated curves on {}_ry,please set the keyframe!'.format(obj), pos='midCenter',backColor=0x8B5353,fade=True,fadeInTime=0.2,fadeOutTime=0.2)
			else:
				tmp_i=0
				for tmp_i in range(len(ry_values)):
					ry_value=ry_values[tmp_i]*-1
					ry_intangent_type=ry_intangent_types[tmp_i]
					ry_intangent=ry_intangents[tmp_i]*-1
					ry_intangent_weight=ry_intangent_weights[tmp_i]
					ry_outtangent_type=ry_outtangent_types[tmp_i]
					ry_outtangent=ry_outtangents[tmp_i]*-1
					ry_outtangent_weight=ry_outtangent_weights[tmp_i]
					cmds.keyframe(obj,edit=1,attribute='rotateY',index=(tmp_i,tmp_i),valueChange=ry_value)
					cmds.keyTangent(obj,edit=1,attribute='rotateY',index=(tmp_i,tmp_i)
											,inTangentType=ry_intangent_type
											,inAngle=ry_intangent
											,inWeight=ry_intangent_weight
											,outTangentType=ry_outtangent_type
											,outAngle=ry_outtangent
											,outWeight=ry_outtangent_weight)
def AcrossXY(objs,localAxis='XYZ'):
	if localAxis=='XYZ' or localAxis=='YXZ':
		Across_xy(objs)
	elif localAxis=='XZY' or localAxis=='ZXY':
		Across_xz(objs)
	else:
		Across_yz(objs)
def AcrossXZ(objs,localAxis='XYZ'):
	if localAxis=='XYZ' or localAxis=='ZYX':
		Across_xz(objs)
	elif localAxis=='XZY' or localAxis=='YZX':
		Across_xy(objs)
	else:
		Across_yz(objs)
def AcrossYZ(objs,localAxis='XYZ'):
	if localAxis=='XYZ' or localAxis=='XZY':
		Across_yz(objs)
	elif localAxis=='YXZ' or localAxis=='YZX':
		Across_xz(objs)
	else:
		Across_xy(objs)