from sys import *
from cli import *

param= str(sys.argv[1:])
param=param[2:6]
print("")
print("fiok kod: ",param)

tr=cli(param)
tr=tr.replace("ef", "== VOICE ===") 
tr=tr.replace("cs1","=== WIFI ===") 
tr=tr.replace("cs2","WIFI_CONTROL") 
tr=tr.replace("af41","=VIDEOCONF=")
tr=tr.replace("af42","= CITRIX  =")
tr=tr.replace("af13","=NYOMTATAS=")
tr=tr.replace("af21","=== ATM ===")
tr=tr.replace("af43","== VIDUX ==")

tr=tr.replace("Tu100","TK-ASRA")
tr=tr.replace("Tu300","DC-ASRA") 
tr=tr.replace("Tu200","TK-ASRB")
tr=tr.replace("Tu400","DC-ASRB") 

print(tr) 

