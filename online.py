#!/usr/bin/env python

from gnuradio import gr
from gnuradio.wxgui import stdgui2,fftsink2,scopesink2
import wx

class gnuradioGUI(stdgui2.std_top_block):
    def __init__(self,frame,panel,vbox,argv):
        stdgui2.std_top_block.__init__(self,frame,panel,vbox,argv)
        
        fft = fftsink2.fft_sink_f(panel, title="FFT display", fft_size=512, sample_rate=100000)
        vbox.Add(fft.win,4,wx.EXPAND)
        

        scope = scopesink2.scope_sink_f(panel, title="Oscilloscope", sample_rate=100000)
        vbox.Add(scope.win,4,wx.EXPAND)
        
        signal = gr.sig_source_f(100000,gr.GR_SIN_WAVE,20000,1000,0)
        throttle = gr.throttle(gr.sizeof_float,100000)
        self.connect(signal,throttle)
        self.connect(throttle,fft)
        self.connect(throttle,scope)

if __name__ == '__main__':
    app = stdgui2.stdapp(gnuradioGUI,"A simple GNU Radio GUI")
    app.MainLoop()
    