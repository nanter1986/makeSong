from EasyMIDI import * 
import random
import datetime
from pprint import * 

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
    for i in range(0,duration2):
        print(progression['progression'][0])
        for t1 in range(0,4):
            track1.addChord(chord1)
            notes1=chord1.getNotes()
            print(chord1.getNumeral())
            for n in notes1:
                print("chord 1:"+n.name)
        for t2 in range(0,4):
            track1.addChord(chord2)
            notes2=chord2.getNotes()
            print(chord2.getNumeral())
            for n in notes2:
                print("chord 2:"+n.name)
        for t3 in range(0,4):
            track1.addChord(chord3)
            notes3=chord3.getNotes()
            print(chord3.getNumeral())
            for n in notes3:
                print("chord 3:"+n.name)
        for t4 in range(0,4):
            track1.addChord(chord4)
            notes4=chord4.getNotes()
            print(chord4.getNumeral())
            for n in notes4:
                print("chord 4:"+n.name)

def addPercussion(progression):
    #creates drum pattern based on parameter,and adds ut to drum track
    pattern=[]
    pattern2=[]
    print("pattern created empty")
    #create the repeating pattern
    for j in range(0,16):
        pattern.append(random.choice(range(0,4)))
    print(pattern)
    for u in range(0,32):
        pattern2.append(random.choice(range(0,4)))
    print(pattern2)
    #add the repeating pattern
    for i in range(0,2):
        for i in range(0,duration2):
            for x in pattern:
                volume=100
                if x==0:
                    volume=0
                note=Note(theKey,2,0.25,volume)
                drumsTrack.addNotes(note)
        for i in range(0,duration2):
            for y in pattern2:
                volume=100
                if y==0:
                    volume=0
                note=Note(theKey,2,0.125,volume)
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

def verseSeq():
    #make the basic sequence of notes used for verse lines,preferes smooth transitions
    theSeq=[]
    result=2
    for i in range(0,15):
        options=[0,-1,+1]
        choice=random.choice(options)
        result=result+choice
        if result<0:
            result=0
        elif result>6:
            result=6
        theSeq.append(result)
    pprint(theSeq)
    return theSeq

def chorusSeq():
    theSeq=[]
    result=2
    for i in range(0,31):
        options=[0,-1,+1]
        choice=random.choice(options)
        result=result+choice
        if result<0:
            result=0
        elif result>6:
            result=6
        theSeq.append(result)
    pprint(theSeq)
    return theSeq

def makeMelodyPattern(scales,progression):
    #creates melody pattern based on parameter,and adds ut to melody track,verse
    sequenceVerse=verseSeq()
    sequenceChorus=chorusSeq()
    pattern=[]
    for ch in progression["progression"]:
        print("--------------next round -verse----------")
        for i in range(0,15):
            chord1=RomanChord(ch,4,4,theKey,progression['flavor'][0],100)
            if i==0:
                volume=100
                nnn=random.choice(chord1.getNotes())
                pprint(nnn.name)
                note=Note(nnn.name,5,0.5,volume)
                print(note.name)
                pattern.append(note)
            else:
                volume=random.choice([0,100,100])
                #pattern.append(random.choice(scales))
                note=Note(scales[sequenceVerse[i]],5,0.25,volume)
                print(note.name)
                pattern.append(note)
    print("--------------------------end of verse----------------")
    
    for ch in progression["progression"]:
        print("--------------next round chorus----------")
        for i in range(0,31):
            chord1=RomanChord(ch,4,4,theKey,progression['flavor'][0],100)
            if i==0:
                volume=100
                nnn=random.choice(chord1.getNotes())
                pprint(nnn.name)
                note=Note(nnn.name,5,0.25,volume)
                print(note.name)
                pattern.append(note)
            else:
                volume=random.choice([0,100])
                #pattern.append(random.choice(scales))
                note=Note(scales[sequenceChorus[i]],5,0.125,volume)
                print(note.name)
                pattern.append(note)
    print("--------------------------end of verse----------------")
    return pattern


def makeMelody(progression):
    #add chorus and verse to melody track
    theory=MusicTheory()
    scales=theory.getMajorScales()[theKey]
    print(scales)
    pattern1=makeMelodyPattern(scales,progression)
    for times in range(0,2):
        for j in pattern1:
            print(j.name)
            melodyTrack.addNotes(j)

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


