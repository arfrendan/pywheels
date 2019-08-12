from escpos.printer import Usb
import six
import sys
class ChUsb (Usb):
    def __init__(self, *args, **kwargs):
        super(ChUsb,self).__init__(*args,**kwargs)
        self.charcode('WPC1252')
    def text(self,txt):
        txt = txt.encode('gb2312').decode('l1')
        if txt:
            if self.codepage:
                self._raw(txt.encode(self.codepage))
            else:
                self._raw(txt.encode())
                
    def reset(self):
        self.set(align = u'left',width = 1,height = 1,text_type = 'NORMAL' )
    def textln(self,txt):
        #self.set(width = 1,height = 1)
        if txt:
            self.text(txt)
            self.text("\n")
    
p2 = ChUsb(0x8866,0x0100,timeout=0, in_ep=0x81, out_ep=0x02)