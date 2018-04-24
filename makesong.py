from EasyMIDI import EasyMIDI,Track,Note,Chord,RomanChord 
import random
import datetime

easyMIDI = EasyMIDI()
track1 = Track("acoustic grand piano")
drumsTrack=Track("Synth Drum")
duration=4

def getTheTime():
    curTime=str(datetime.datetime.now())
    return curTime

def createProgression():
    progression=[]
    flavor=[]
    dictChordsFlavor={}
    options=[['I','VI'],['II','IV'],['I','VI*'],['V*','III','VII-*']]
    print(len(options))
    for i in range(0,4):
        progression.append(random.choice(options[i]))
        flavor.append(majorOrMinor())
    
    dictChordsFlavor['progression']=progression
    dictChordsFlavor['flavor']=flavor
    print(dictChordsFlavor)
    return dictChordsFlavor


def addProgression(progression):
    for i in range(0,duration):
        print(progression['progression'][0])
        track1.addChord(RomanChord(progression['progression'][0],4,1,'C',progression['flavor'][0],100))
        track1.addChord(RomanChord(progression['progression'][1],4,1,'C',progression['flavor'][1],100))
        track1.addChord(RomanChord(progression['progression'][2],4,1,'C',progression['flavor'][2],100))
        track1.addChord(RomanChord(progression['progression'][3],4,1,'C',progression['flavor'][3],100))

def addPercussion(progression):
    for i in range(0,duration*16):
        volume=100
        has=random.choice(range(0,4))
        if has==0 :
            volume=0
        note=Note('C',2,0.25,volume)
        drumsTrack.addNotes (note)

def addBass(progression):
    #bass
    pass

def makeMelody(progression):
    #make melody based on chord progression
    pass

def majorOrMinor():
    ch=random.choice(range(0,2))
    return ch

def exportFile():
    easyMIDI.addTrack(track1)
    easyMIDI.addTrack(drumsTrack)
    name=getTheTime()
    easyMIDI.writeMIDI(name+".mid")

def makeSong():
    progression=createProgression()
    addProgression(progression)
    addPercussion(progression)
    addBass(progression)
    makeMelody(progression)
    exportFile()

makeSong()    


