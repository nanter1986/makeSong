from EasyMIDI import * 
import random
import datetime

easyMIDI = EasyMIDI()

def chooseKey():
    keys=['C','D','E','F','G','A','B']
    key=random.choice(keys)
    #key='C'
    return key


def setTheOrgans():
    org={}
    org['track1']=random.choice(['Acoustic Grand Piano',
            'String Ensemble 1',
            'Synth Strings 1',
            'Pad 2 (warm)'])
    org['melodyTrack']=random.choice(['Harmonica',
            'Distortion Guitar',
            'Trumpet'])
    org['bassTrack']=random.choice(['Synth Bass 1','Electric Bass (finger)']) 
    org['drumsTrack']=random.choice(['Synth Drum'])
    for key,value in org.items():
        print('organs:')
        print(key+':'+value)
    return org

organOptions=setTheOrgans()


theKey=chooseKey()
tempo=random.choice([120,140,160,180])
print("key: "+theKey)
print("tempo: "+str(tempo))
track1 = Track(organOptions['track1'],tempo)
drumsTrack=Track(organOptions['drumsTrack'],tempo)
bassTrack=Track(organOptions['bassTrack'],tempo)
melodyTrack=Track(organOptions['melodyTrack'],tempo)
duration=8
duration2=4

def getTheTime():
    curTime=str(datetime.datetime.now())
    return curTime


def createProgression():
    progression=[]
    flavor=[]
    dictChordsFlavor={}
    options=[['I','VI'],['II','IV'],['I','VI'],['V','III','VII']]
    print(len(options))
    for i in range(0,4):
        chord=random.choice(options[i])
        progression.append(chord)
        flavor.append(majorOrMinor(chord))

    dictChordsFlavor['progression']=progression
    dictChordsFlavor['flavor']=flavor
    print(dictChordsFlavor)
    return dictChordsFlavor


def addProgression(progression):
    chord1=RomanChord(progression['progression'][0],4,1,theKey,progression['flavor'][0],100)
    chord2=RomanChord(progression['progression'][1],4,1,theKey,progression['flavor'][1],100)
    chord3=RomanChord(progression['progression'][2],4,1,theKey,progression['flavor'][2],100)
    chord4=RomanChord(progression['progression'][3],4,1,theKey,progression['flavor'][3],100)
    for i in range(0,duration):
        print(progression['progression'][0])
        track1.addChord(chord1)
        track1.addChord(chord2)
        track1.addChord(chord3)
        track1.addChord(chord4)
    notes1=chord1.getNotes()
    notes2=chord2.getNotes()
    notes3=chord3.getNotes()
    notes4=chord4.getNotes()
    for n in notes1:
        print("chord 1:"+n.name)
    for n in notes2:
        print("chord 2:"+n.name)
    for n in notes3:
        print("chord 3:"+n.name)
    for n in notes4:
        print("chord 4:"+n.name)

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
            note=Note(scales[0],3,0.25,volume)
        else:
            volume=random.choice([0,100])
            #pattern.append(random.choice(scales))
            note=Note(scales[0],3,0.25,volume)
        pattern.append(note)
    print("bass:")
    #print(pattern)
    for j in range(0,duration):
        for n in pattern:
            #print(n.name)
            bassTrack.addNotes(n)

def makeMelodyPattern(scales):
    pattern=[]
    for i in range(0,14):
        if i==0:
            volume=100
            note=Note(scales[0],5,0.5,volume)
        elif i==7:
            volume=100
            note=Note(scales[1],5,0.5,volume)
        elif i==13:    
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

def makeChorusPattern(scales):
    pattern=[]
    for i in range(0,14):
        if i==0:
            volume=100
            note=Note(scales[0],6,0.5,volume)
        elif i==7:
            volume=100
            note=Note(scales[1],6,0.5,volume)
        elif i==13:    
            volume=100
            note=Note(scales[6],6,0.25,volume)
        else:
            volume=random.choice([0,100])
            #pattern.append(random.choice(scales))
            note=Note(random.choice(scales),6,0.25,volume)
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
    pattern2=makeChorusPattern(scales)
    for times in range(0,2):
        for j in range(0,duration2):
            print("pattern1:")
            for x in pattern1:
                print(x.name)
                melodyTrack.addNotes(x)
        for j2 in range(0,duration2):
            print("chorus:")
            for x2 in pattern2:
                print(x2.name)
                melodyTrack.addNotes(x2)

def majorOrMinor(pattern):
    '''ch=0
    if pattern=='I':
        ch=1
    elif pattern=='IV':
        ch=1
    elif pattern=='V':
        ch=1
    print("chord "+pattern+" is "+str(ch))'''
    ch=1
    return ch

def exportFile():
    easyMIDI.addTrack(track1)
    easyMIDI.addTrack(drumsTrack)
    easyMIDI.addTrack(bassTrack)
    easyMIDI.addTrack(melodyTrack)
    name=getTheTime()
    #easyMIDI.writeMIDI("songs/"+name+".mid")
    easyMIDI.writeMIDI("../../storage/downloads/"+name+".mid")

def makeSong():
    progression=createProgression()
    addProgression(progression)
    addPercussion(progression)
    addBass(progression)
    makeMelody(progression)
    exportFile()

makeSong()    


