def Getcmdlines(path):
    with open(path,'r') as f:
        cmdlines=f.read()
    return cmdlines