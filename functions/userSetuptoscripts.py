#################forzjh#################
#zjh
import sys #zjh
from maya import cmds #zjh
plug_path="{}" #zjh
sys.path.insert(0,plug_path) #zjh
from functions import installfunction as istf #zjh
cmds.evalDeferred('istf.ZJHInstall()') #zjh
#zjh
##################forzjh################