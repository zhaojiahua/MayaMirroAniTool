from maya import cmds
def OnesideToOtherside(ctrs,direction,axissame):
    tempc=tempcr=tempco=None
    axissame=(axissame-0.5)*2
    for ctr in ctrs:
        anicurves_rots=cmds.findKeyframe(ctr,at='rotate',curve=1)
        anicurves_trans=cmds.findKeyframe(ctr,at='translate',curve=1)
        otherAttrs=cmds.listAttr(ctr,k=1)
        if 'translateX' in otherAttrs:
            otherAttrs.remove('translateX')
        if 'translateY' in otherAttrs:
            otherAttrs.remove('translateY')
        if 'translateZ' in otherAttrs:
            otherAttrs.remove('translateZ')
        if 'rotateX' in otherAttrs:
            otherAttrs.remove('rotateX')
        if 'rotateY' in otherAttrs:
            otherAttrs.remove('rotateY')
        if 'rotateZ' in otherAttrs:
            otherAttrs.remove('rotateZ')
        anicurves_others=cmds.findKeyframe(ctr,at=otherAttrs,c=1)
        if anicurves_trans is None:
            anicurves_trans=[]
        else:
            tempc=cmds.duplicate(ctr,n=ctr+'_temp',rc=1,rr=1)[0]
            for anicurves_tran in anicurves_trans:
                cmds.copyKey(anicurves_tran)
                cmds.pasteKey(tempc,option='replaceCompletely')
            #get translate values
            tx_values=cmds.keyframe(ctr,q=1,attribute='translateX',valueChange=1)
            tx_intangent_types=cmds.keyTangent(ctr,q=1,attribute='translateX',inTangentType=1)
            tx_intangents=cmds.keyTangent(ctr,q=1,attribute='translateX',inAngle=1)
            tx_intangent_weights=cmds.keyTangent(ctr,q=1,attribute='translateX',inWeight=1)
            tx_outtangent_types=cmds.keyTangent(ctr,q=1,attribute='translateX',outTangentType=1)
            tx_outtangents=cmds.keyTangent(ctr,q=1,attribute='translateX',outAngle=1)
            tx_outtangent_weights=cmds.keyTangent(ctr,q=1,attribute='translateX',outWeight=1)
            ty_values=cmds.keyframe(ctr,q=1,attribute='translateY',valueChange=1)
            ty_intangent_types=cmds.keyTangent(ctr,q=1,attribute='translateY',inTangentType=1)
            ty_intangents=cmds.keyTangent(ctr,q=1,attribute='translateY',inAngle=1)
            ty_intangent_weights=cmds.keyTangent(ctr,q=1,attribute='translateY',inWeight=1)
            ty_outtangent_types=cmds.keyTangent(ctr,q=1,attribute='translateY',outTangentType=1)
            ty_outtangents=cmds.keyTangent(ctr,q=1,attribute='translateY',outAngle=1)
            ty_outtangent_weights=cmds.keyTangent(ctr,q=1,attribute='translateY',outWeight=1)
            tz_values=cmds.keyframe(ctr,q=1,attribute='translateZ',valueChange=1)
            tz_intangent_types=cmds.keyTangent(ctr,q=1,attribute='translateZ',inTangentType=1)
            tz_intangents=cmds.keyTangent(ctr,q=1,attribute='translateZ',inAngle=1)
            tz_intangent_weights=cmds.keyTangent(ctr,q=1,attribute='translateZ',inWeight=1)
            tz_outtangent_types=cmds.keyTangent(ctr,q=1,attribute='translateZ',outTangentType=1)
            tz_outtangents=cmds.keyTangent(ctr,q=1,attribute='translateZ',outAngle=1)
            tz_outtangent_weights=cmds.keyTangent(ctr,q=1,attribute='translateZ',outWeight=1)
            #set tempc translate values opposite
            tmp_i=0
            for tmp_i in range(len(tx_values)):
                tx_value=tx_values[tmp_i]*-1
                tx_intangent_type=tx_intangent_types[tmp_i]
                tx_intangent=tx_intangents[tmp_i]*-1
                tx_intangent_weight=tx_intangent_weights[tmp_i]
                tx_outtangent_type=tx_outtangent_types[tmp_i]
                tx_outtangent=tx_outtangents[tmp_i]*-1
                tx_outtangent_weight=tx_outtangent_weights[tmp_i]
                cmds.keyframe(tempc,edit=1,attribute='translateX',index=(tmp_i,tmp_i),valueChange=tx_value)
                cmds.keyTangent(tempc,edit=1,attribute='translateX',index=(tmp_i,tmp_i)
                                            ,inTangentType=tx_intangent_type
                                            ,inAngle=tx_intangent
                                            ,inWeight=tx_intangent_weight
                                            ,outTangentType=tx_outtangent_type
                                            ,outAngle=tx_outtangent
                                            ,outWeight=tx_outtangent_weight)
            tmp_i=0
            for tmp_i in range(len(ty_values)):
                ty_value=ty_values[tmp_i]*axissame
                ty_intangent_type=ty_intangent_types[tmp_i]
                ty_intangent=ty_intangents[tmp_i]*axissame
                ty_intangent_weight=ty_intangent_weights[tmp_i]
                ty_outtangent_type=ty_outtangent_types[tmp_i]
                ty_outtangent=ty_outtangents[tmp_i]*axissame
                ty_outtangent_weight=ty_outtangent_weights[tmp_i]
                cmds.keyframe(tempc,edit=1,attribute='translateY',index=(tmp_i,tmp_i),valueChange=ty_value)
                cmds.keyTangent(tempc,edit=1,attribute='translateY',index=(tmp_i,tmp_i)
                                            ,inTangentType=ty_intangent_type
                                            ,inAngle=ty_intangent
                                            ,inWeight=ty_intangent_weight
                                            ,outTangentType=ty_outtangent_type
                                            ,outAngle=ty_outtangent
                                            ,outWeight=ty_outtangent_weight)
            tmp_i=0
            for tmp_i in range(len(tz_values)):
                tz_value=tz_values[tmp_i]*axissame
                tz_intangent_type=tz_intangent_types[tmp_i]
                tz_intangent=tz_intangents[tmp_i]*axissame
                tz_intangent_weight=tz_intangent_weights[tmp_i]
                tz_outtangent_type=tz_outtangent_types[tmp_i]
                tz_outtangent=tz_outtangents[tmp_i]*axissame
                tz_outtangent_weight=tz_outtangent_weights[tmp_i]
                cmds.keyframe(tempc,edit=1,attribute='translateZ',index=(tmp_i,tmp_i),valueChange=tz_value)
                cmds.keyTangent(tempc,edit=1,attribute='translateZ',index=(tmp_i,tmp_i)
                                        ,inTangentType=tz_intangent_type
                                        ,inAngle=tz_intangent
                                        ,inWeight=tz_intangent_weight
                                        ,outTangentType=tz_outtangent_type
                                        ,outAngle=tz_outtangent
                                        ,outWeight=tz_outtangent_weight)
            anicurves_trans=cmds.findKeyframe(tempc,at='translate',curve=1)
        if anicurves_rots is None:
            anicurves_rots=[]
        else:
            tempcr=cmds.duplicate(ctr,n=ctr+'_tempr',rc=1,rr=1)[0]
            for anicurves_rot in anicurves_rots:
                cmds.copyKey(anicurves_rot)
                cmds.pasteKey(tempcr,option='replaceCompletely')
            #get translate values
            rx_values=cmds.keyframe(ctr,q=1,attribute='rotateX',valueChange=1)
            rx_intangent_types=cmds.keyTangent(ctr,q=1,attribute='rotateX',inTangentType=1)
            rx_intangents=cmds.keyTangent(ctr,q=1,attribute='rotateX',inAngle=1)
            rx_intangent_weights=cmds.keyTangent(ctr,q=1,attribute='rotateX',inWeight=1)
            rx_outtangent_types=cmds.keyTangent(ctr,q=1,attribute='rotateX',outTangentType=1)
            rx_outtangents=cmds.keyTangent(ctr,q=1,attribute='rotateX',outAngle=1)
            rx_outtangent_weights=cmds.keyTangent(ctr,q=1,attribute='rotateX',outWeight=1)
            ry_values=cmds.keyframe(ctr,q=1,attribute='rotateY',valueChange=1)
            ry_intangent_types=cmds.keyTangent(ctr,q=1,attribute='rotateY',inTangentType=1)
            ry_intangents=cmds.keyTangent(ctr,q=1,attribute='rotateY',inAngle=1)
            ry_intangent_weights=cmds.keyTangent(ctr,q=1,attribute='rotateY',inWeight=1)
            ry_outtangent_types=cmds.keyTangent(ctr,q=1,attribute='rotateY',outTangentType=1)
            ry_outtangents=cmds.keyTangent(ctr,q=1,attribute='rotateY',outAngle=1)
            ry_outtangent_weights=cmds.keyTangent(ctr,q=1,attribute='rotateY',outWeight=1)
            rz_values=cmds.keyframe(ctr,q=1,attribute='rotateZ',valueChange=1)
            rz_intangent_types=cmds.keyTangent(ctr,q=1,attribute='rotateZ',inTangentType=1)
            rz_intangents=cmds.keyTangent(ctr,q=1,attribute='rotateZ',inAngle=1)
            rz_intangent_weights=cmds.keyTangent(ctr,q=1,attribute='rotateZ',inWeight=1)
            rz_outtangent_types=cmds.keyTangent(ctr,q=1,attribute='rotateZ',outTangentType=1)
            rz_outtangents=cmds.keyTangent(ctr,q=1,attribute='rotateZ',outAngle=1)
            rz_outtangent_weights=cmds.keyTangent(ctr,q=1,attribute='rotateZ',outWeight=1)
            #set tempcr translate values opposite
            tmp_i=0
            for tmp_i in range(len(rx_values)):
                rx_value=rx_values[tmp_i]
                rx_intangent_type=rx_intangent_types[tmp_i]
                rx_intangent=rx_intangents[tmp_i]
                rx_intangent_weight=rx_intangent_weights[tmp_i]
                rx_outtangent_type=rx_outtangent_types[tmp_i]
                rx_outtangent=rx_outtangents[tmp_i]
                rx_outtangent_weight=rx_outtangent_weights[tmp_i]
                cmds.keyframe(tempcr,edit=1,attribute='rotateX',index=(tmp_i,tmp_i),valueChange=rx_value)
                cmds.keyTangent(tempcr,edit=1,attribute='rotateX',index=(tmp_i,tmp_i)
                                            ,inTangentType=rx_intangent_type
                                            ,inAngle=rx_intangent
                                            ,inWeight=rx_intangent_weight
                                            ,outTangentType=rx_outtangent_type
                                            ,outAngle=rx_outtangent
                                            ,outWeight=rx_outtangent_weight)
            tmp_i=0
            for tmp_i in range(len(ry_values)):
                ry_value=ry_values[tmp_i]*-axissame
                ry_intangent_type=ry_intangent_types[tmp_i]
                ry_intangent=ry_intangents[tmp_i]*-axissame
                ry_intangent_weight=ry_intangent_weights[tmp_i]
                ry_outtangent_type=ry_outtangent_types[tmp_i]
                ry_outtangent=ry_outtangents[tmp_i]*-axissame
                ry_outtangent_weight=ry_outtangent_weights[tmp_i]
                cmds.keyframe(tempcr,edit=1,attribute='rotateY',index=(tmp_i,tmp_i),valueChange=ry_value)
                cmds.keyTangent(tempcr,edit=1,attribute='rotateY',index=(tmp_i,tmp_i)
                                            ,inTangentType=ry_intangent_type
                                            ,inAngle=ry_intangent
                                            ,inWeight=ry_intangent_weight
                                            ,outTangentType=ry_outtangent_type
                                            ,outAngle=ry_outtangent
                                            ,outWeight=ry_outtangent_weight)
            tmp_i=0
            for tmp_i in range(len(rz_values)):
                rz_value=rz_values[tmp_i]*-axissame
                rz_intangent_type=rz_intangent_types[tmp_i]
                rz_intangent=rz_intangents[tmp_i]*-axissame
                rz_intangent_weight=rz_intangent_weights[tmp_i]
                rz_outtangent_type=rz_outtangent_types[tmp_i]
                rz_outtangent=rz_outtangents[tmp_i]*-axissame
                rz_outtangent_weight=rz_outtangent_weights[tmp_i]
                cmds.keyframe(tempcr,edit=1,attribute='rotateZ',index=(tmp_i,tmp_i),valueChange=rz_value)
                cmds.keyTangent(tempcr,edit=1,attribute='rotateZ',index=(tmp_i,tmp_i)
                                        ,inTangentType=rz_intangent_type
                                        ,inAngle=rz_intangent
                                        ,inWeight=rz_intangent_weight
                                        ,outTangentType=rz_outtangent_type
                                        ,outAngle=rz_outtangent
                                        ,outWeight=rz_outtangent_weight)
            anicurves_rots=cmds.findKeyframe(tempcr,at='rotate',curve=1)
        if anicurves_others is None:
            anicurves_others=[]
        else:
            tempco=cmds.duplicate(ctr,n=ctr+'_tempo',rc=1,rr=1)[0]
            for anicurves_other in anicurves_others:
                cmds.copyKey(anicurves_other)
                cmds.pasteKey(tempco,option='replaceCompletely')
            anicurves_others=cmds.findKeyframe(tempco,at=otherAttrs,curve=1)
        anicurves=anicurves_rots+anicurves_trans+anicurves_others
        dirs=direction.split('to')
        ctr_otherside=ctr.replace('_{}'.format(dirs[0]),'_{}'.format(dirs[1]))
        old_curves=cmds.findKeyframe(ctr_otherside,curve=1)
        if len(anicurves)==0:
            cmds.inViewMessage(amg='{} has no animated curves'.format(ctr), pos='midCenter',backColor=0x5B8373,fade=True,fadeInTime=0.2,fadeOutTime=0.2)
        else:
            cmds.delete(old_curves)
            for anicurve in anicurves:
                cmds.copyKey(anicurve)
                cmds.pasteKey(ctr_otherside,option='replaceCompletely')
        cmds.delete(tempc,tempcr,tempco)
