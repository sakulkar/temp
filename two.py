##!/usr/bin/python
#
#from gnuradio import gr;
#from gnuradio.wxgui import fftsink2;
##import wx;
#
#class my_graph(gr.top_block):
#        def __init__(self):
#                gr.top_block.__init__(self)
#
#                #build flow graph
#                #create sinusoidal source with a sample rate
#                # of 48000s/s and frequency of 350 
#                #amplitude of 0.1
#                src = gr.sig_source_f(48000,gr.GR_SIN_WAVE,350,0.1)
#
#                #create a destination sink 
#                sink = fftsink2.fft_sink_f(self, title="fft", fft_size=512, sample_rate=48000);
#
#                #connect each of the sources to the sink
#                self.connect(src,(sink,0))
#    
#if __name__ == '__main__':
#    fg = my_graph()
#    try:
#        fg.run()
#    except KeyboardInterrupt:
#        pass
#    
#   