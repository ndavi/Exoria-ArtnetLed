from artnetServer.ArtNetServer import ArtNetServer

def newArtNetToOSCData(data):
    print(data.framedata)
    pass


artNetReceiver = ArtNetServer()
artNetReceiver.run(newArtNetToOSCData)
