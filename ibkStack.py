import nuke

def ibkStack():
    master = nuke.selectedNode()
    mscreent = master['screen_type'].getValue()
    mscreent = int(mscreent)
    msize = master.knob('Size').getValue()
    moff = master.knob('off').getValue()
    mmult = master.knob('mult').getValue()
    mpatch = master.knob('multi').getValue()
    
    slave = nuke.createNode('IBKColourV3')
    slave.knob('Size').setValue(msize)
    slave['screen_type'].setValue(mscreent)
    slave.knob('off').setValue(moff)
    slave.knob('mult').setValue(mmult)
    slave.knob('erode').setValue('0')
    mpatch = mpatch*2
    slave.knob('multi').setValue(mpatch)
