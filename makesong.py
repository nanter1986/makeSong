from EasyMIDI import EasyMIDI,Track,Note,Chord,RomanChord 
import random
import datetime

easyMIDI = EasyMIDI()
theKey=chooseKey()
track1 = Track("acoustic grand piano")
drumsTrack=Track("Synth Drum")
duration=4

def getTheTime():
    curTime=str(datetime.datetime.now())
    return curTime

def chooseKey():
    keys=['C','D','E','F','G','A','B']
    key=random.choice(keys)
    return key

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
    pattern=[]
    print("pattern created empty")
    #create the repeating pattern
    for j in range(0,16):
        pattern.append(random.choice(range(0,4)))
    print(pattern)
    #add the repeating pattern
    for i in range(0,duration):
        for x in pattern:
            volume=100
            if x==0:
                volume=0
            note=Note('C',2,0.25,volume)
            drumsTrack.addNotes(note)

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


