def connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('OBI_WLAN_KENOBI', 'Ithurtswhenip')
        #sta_if.connect('EpusNet2', 'epus1993')
        #sta_if.connect('iPhone von Kilu', 'sousousou')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

def no_debug():
    import esp
    # this can be run from the REPL as well
    esp.osdebug(None)

no_debug()
connect()