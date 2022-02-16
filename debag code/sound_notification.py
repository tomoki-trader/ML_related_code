#set the first code
import winsound
def play_sound(self,etype, value, tb,Hz=700,long=1000, tb_offset=None):
    self.showtraceback((etype, value, tb), tb_offset=tb_offset)
    return winsound.Beep(Hz,long)

get_ipython().set_custom_exc((Exception,),play_sound)

#set the last code
for i in range(1):#5回繰り返す
    winsound.Beep(500,900)