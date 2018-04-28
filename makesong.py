from EasyMIDI import * 
import random
import datetime

easyMIDI = EasyMIDI()

def chooseKey():
    #returns a random key
    keys=['C','D','E','F','G','A','B']
    key=random.choice(keys)
    #key='C'
    return key


def setTheOrgans():
    #returns a dictionary with randomly selected organs
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
    #returns current time and date
    curTime=str(datetime.datetime.now())
    return curTime


def createProgression():
    #returns a random progression from predefined chords
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
    #adds chords to the chord track
    chord1=RomanChord(progression['progression'][0],4,1,theKey,progression['flavor'][0],100)
    chord2=RomanChord(progression['progression'][1],4,1,theKey,progression['flavor'][1],100)
    chord3=RomanChord(progression['progression'][2],4,1,theKey,progression['flavor'][2],100)
    chord4=RomanChord(progression['progression'][3],4,1,theKey,progression['flavor'][3],100)
    for i in range(0,2*duration):
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
    #creates drum pattern based on parameter,and adds ut to drum track
    pattern=[]
    print("pattern created empty")
    #create the repeating pattern
    for j in range(0,16):
        pattern.append(random.choice(range(0,4)))
    print(pattern)
    #add the repeating pattern
    for i in range(0,2*duration):
        for x in pattern:
            volume=100
            if x==0:
                volume=0
            note=Note(theKey,2,0.25,volume)
            drumsTrack.addNotes(note)

def addBass(progression):
    #creates bass pattern based on parameter,and adds ut to bass track
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
    for j in range(0,2*duration):
        for n in pattern:
            #print(n.name)
            bassTrack.addNotes(n)

def makeMelodyPattern(scales):
    #creates melody pattern based on parameter,and adds ut to melody track,verse
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
    #creates melody pattern based on parameter,and adds ut to melody track,chorus
    pattern=[]
    for i in range(0,30):
        if i==0:
            volume=100
            note=Note(scales[0],6,0.25,volume)
        elif i==7:
            volume=100
            note=Note(scales[1],6,0.25,volume)
        elif i==13:    
            volume=100
            note=Note(scales[6],6,0.125,volume)
        else:
            volume=random.choice([0,100])
            #pattern.append(random.choice(scales))
            note=Note(random.choice(scales),6,0.125,volume)
        pattern.append(note)
    #print("melody:")
    #print(pattern)
    return pattern

def makeMelody(progression):
    #add chorus and verse to melody track
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
    #decides if chord comes from major or minor key
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
    #adds all tracks to file and exports it,name based on date
    easyMIDI.addTrack(track1)
    easyMIDI.addTrack(drumsTrack)
    easyMIDI.addTrack(bassTrack)
    easyMIDI.addTrack(melodyTrack)
    name=getTheTime()
    #easyMIDI.writeMIDI("songs/"+name+".mid")
    easyMIDI.writeMIDI("../../storage/downloads/"+name+".mid")

def makeSong():
    #main function,delegates to other functions
    progression=createProgression()
    addProgression(progression)
    addPercussion(progression)
    addBass(progression)
    makeMelody(progression)
    exportFile()

makeSong()    


