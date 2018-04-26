from EasyMIDI import * 
import random
import datetime

easyMIDI = EasyMIDI()

def chooseKey():
    keys=['C','D','E','F','G','A','B']
    key=random.choice(keys)
    return key

theKey=chooseKey()
print(theKey)
track1 = Track("acoustic grand piano")
drumsTrack=Track("Synth Drum")
bassTrack=Track("Synth Bass 1")
melodyTrack=Track("Distortion Guitar")
duration=8
duration2=4

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
        flavor.append(majorOrMinor(progression))
    
    dictChordsFlavor['progression']=progression
    dictChordsFlavor['flavor']=flavor
    print(dictChordsFlavor)
    return dictChordsFlavor


def addProgression(progression):
    for i in range(0,duration):
        print(progression['progression'][0])
        track1.addChord(RomanChord(progression['progression'][0],4,1,theKey,progression['flavor'][0],100))
        track1.addChord(RomanChord(progression['progression'][1],4,1,theKey,progression['flavor'][1],100))
        track1.addChord(RomanChord(progression['progression'][2],4,1,theKey,progression['flavor'][2],100))
        track1.addChord(RomanChord(progression['progression'][3],4,1,theKey,progression['flavor'][3],100))

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
            note=Note(theKey,2,0.25,volume)
            drumsTrack.addNotes(note)

def addBass(progression):
    theory=MusicTheory()
    scales=theory.getMajorScales()[theKey]
    print(scales)
    pattern=[]
    for i in range(0,16):
        if i==0:
            volume=100
            note=Note(scales[0],3,0.25,volume)
        elif i==14:    
            volume=100
            note=Note(scales[0],5,0.25,volume)
        else:
            volume=random.choice([0,100])
            #pattern.append(random.choice(scales))
            note=Note(scales[0],5,0.25,volume)
        pattern.append(note)
    print("bass:")
    #print(pattern)
    for j in range(0,duration):
        for n in pattern:
            print(n.name)
            bassTrack.addNotes(n)

def makeMelodyPattern(scales):
    pattern=[]
    for i in range(0,15):
        if i==0:
            volume=100
            note=Note(scales[0],5,0.5,volume)
        elif i==14:    
            volume=100
            note=Note(scales[6],5,0.25,volume)
        else:
            volume=random.choice([0,100])
            #pattern.append(random.choice(scales))
            note=Note(random.choice(scales),5,0.25,volume)
        pattern.append(note)
    #print("melody:")
    #print(pattern)
    return pattern
    

def makeMelody(progression):
    #make melody based on chord progression
    theory=MusicTheory()
    scales=theory.getMajorScales()[theKey]
    print(scales)
    pattern1=makeMelodyPattern(scales)
    pattern2=makeMelodyPattern(scales)
    for j in range(0,duration2):
        print("pattern1:")
        for x in pattern1:
            print(x.name)
            melodyTrack.addNotes(x)
    for j2 in range(0,duration2):
        print("pattern1:")
        for x2 in pattern2:
            print(x2.name)
            melodyTrack.addNotes(x2)

def majorOrMinor(pattern):
    for i in pattern:
        if pattern[i] in
    ch=random.choice(range(0,2))
    return ch

def exportFile():
    easyMIDI.addTrack(track1)
    easyMIDI.addTrack(drumsTrack)
    easyMIDI.addTrack(bassTrack)
    easyMIDI.addTrack(melodyTrack)
    name=getTheTime()
    easyMIDI.writeMIDI("songs/"+name+".mid")

def makeSong():
    progression=createProgression()
    addProgression(progression)
    addPercussion(progression)
    addBass(progression)
    makeMelody(progression)
    exportFile()

makeSong()    


