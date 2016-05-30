#var/lib/mpd/playlists
# python test - raspberry + serialdisplay (arduino) 
# octopusengine.eu

import random, sys, os, time
from time import sleep

from octopusEngineHWlib import *

# 
#-------------------------main test --------------

#sdRQC(2,"raspberry pi test",1)
#sdRQC(4,"IP addres:",1)
#sleep(1)

txt="> ip: "+getIp()
print txt


while True:
  td=getDallTemp()
  tp=getProcTemp()
  print(str(td),str(tp))

  px=str(int(tt/nas))
  py=sy-td*nast
  sdPXYC(px,py,1)

  px=str(int(tt/nas))
  py=sy-tp*nast
  sdPXYC(px,py,3)
  tt=tt+1

  if tt>320*nas: tt=1

