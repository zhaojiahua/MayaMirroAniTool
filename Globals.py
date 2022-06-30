import sys
import os
import socket
from functions import getip
hostname=socket.gethostname()
hostIP=socket.gethostbyname(hostname)
CurrentPath=sys.path[0]
setupPath="C:/Users/{}/Documents/maya/2018/scripts".format(os.environ['USERNAME'])
zjhmenu="MirrorAniTool"