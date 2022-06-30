def zjhEncodeIP(hostIP):
    IPint=[int(item) for item in hostIP.split('.')]
    pairint=zip(IPint,[18,28,18,28])
    encodeint=[str(item[0]*item[1]) for item in pairint]
    encodestr=''
    for item in encodeint:
        while len(item)<6:
            item='0'+item
        encodestr+=item
    return encodestr
def zjhDecodeIP(encodestr):
    encodelist=[encodestr[:len(encodestr)/2],encodestr[len(encodestr)/2:]]
    decodelist=[]
    for item in encodelist:
        decodelist.append(item[:len(item)/2])
        decodelist.append(item[len(item)/2:])
    pairint=zip(decodelist,[18,28,18,28])
    decodeintlist=[]
    for item in pairint:
        decodeintlist.append(int(item[0])/item[1])
    return decodeintlist