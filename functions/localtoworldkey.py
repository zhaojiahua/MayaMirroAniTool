def LocalToWorldKey(ctrs):
    for ctr in ctrs:
        ctr_dup=cmds.circle(n=ctr+'_dup',nr=(1,0,0),ch=0)
        cmds.parent(ctr_dup,ctr)
        cmds.xform(t=(0,0,0),ro=(0,0,0))
        cmds.parent(ctr_dup,w=1)
        cmds.makeIdentity(ctr_dup,a=1,t=0)
        parent_constraint=cmds.parentConstraint(ctr,ctr_dup,mo=1)
        key_frames=sorted(list(set(cmds.keyframe(ctr,q=1))))
        ctr_dup_values=[]
        for frame in key_frames:
            cmds.currentTime(frame)
            translation=cmds.xform(ctr_dup,q=1,t=1)
            rotation=cmds.xform(ctr_dup,q=1,ro=1)
            ctr_dup_values.append([translation,rotation])
        cmds.delete(parent_constraint)
        key_values=zip(key_frames,ctr_dup_values)
        for item in key_values:
            cmds.currentTime(item[0])
            cmds.xform(ctr_dup,t=item[1][0])
            cmds.setKeyframe(ctr_dup,at='translate')
            cmds.xform(ctr_dup,ro=item[1][1])
            cmds.setKeyframe(ctr_dup,at='rotate')
