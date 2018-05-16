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
    '''returns a dictionary with randomly selected organs'''
    org={}
    org['track1']=random.choice(['Acoustic Grand Piano',
            'String Ensemble 1',
            'Synth Strings 1',
            'Pad 2 (warm)'])
    org['melodyTrack']=random.choice(['Harmonica',
            'Distortion Guitar',
            'Trumpet'])
    org['bassTrack']=random.choice(['Synth Bass 1','Electric Bass (finger)'])
    org['kickTrack']=random.choice(['Synth Drum'])
    org['snareTrack']=random.choice(['Taiko Drum '])
    for key,value in org.items():
        print('organs:')
        print(key+':'+value)
    return org

organOptions=setTheOrgans()


theKey=chooseKey()
tempo=random.choice([180,200,220,240])
print("key: "+theKey)
print("tempo: "+str(tempo))
track1 = Track(organOptions['track1'],tempo)
kickTrack=Track(organOptions['kickTrack'],tempo)
snareTrack=Track(organOptions['snareTrack'],tempo)
bassTrack=Track(organOptions['bassTrack'],tempo)
melodyTrack=Track(organOptions['melodyTrack'],tempo)
duration=8
duration2=4

def getTheTime():
    '''returns current time and date'''
    curTime=str(datetime.datetime.now())
    return curTime


def createProgression():
    '''returns a random progression from predefined chords'''
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
    '''adds chords to the chord track'''
    volumeOfChords=80
    chord1=RomanChord(progression['progression'][0],4,1,theKey,progression['flavor'][0],volumeOfChords)
    chord2=RomanChord(progression['progression'][1],4,1,theKey,progression['flavor'][1],volumeOfChords)
    chord3=RomanChord(progression['progression'][2],4,1,theKey,progression['flavor'][2],volumeOfChords)
    chord4=RomanChord(progression['progression'][3],4,1,theKey,progression['flavor'][3],volumeOfChords)
    totalBarschords=0
    for i in range(0,16):
        for t1 in range(0,2):
            track1.addChord(chord1)
            notes1=chord1.getNotes()
            totalBarschords+=1
            print("bar "+str(totalBarschords)+" "+chord1.getNumeral())
            for n in notes1:
                print("chord 1:"+n.name)
        for t2 in range(0,2):
            track1.addChord(chord2)
            notes2=chord2.getNotes()
            totalBarschords+=1
            print("bar "+str(totalBarschords)+" "+chord2.getNumeral())
            for n in notes2:
                print("chord 2:"+n.name)
        for t3 in range(0,2):
            track1.addChord(chord3)
            notes3=chord3.getNotes()
            totalBarschords+=1
            print("bar "+str(totalBarschords)+" "+chord3.getNumeral())
            for n in notes3:
                print("chord 3:"+n.name)
        for t4 in range(0,2):
            track1.addChord(chord4)
            notes4=chord4.getNotes()
            totalBarschords+=1
            print("bar "+str(totalBarschords)+" "+chord4.getNumeral())
            for n in notes4:
                print("chord 4:"+n.name)
    assert totalBarschords==128

def makeDrumPatterns():
    pattern={}
    pattern["kick_verse"]=[]
    pattern["kick_chorus"]=[]
    pattern["snare_verse"]=[]
    pattern["snare_chorus"]=[]
    print("pattern created empty")
    for j in range(0,8):
        pattern["kick_verse"].append(random.choice(range(0,4)))
        pattern["snare_verse"].append(random.choice(range(0,4)))
    for u in range(0,16):
        pattern["kick_chorus"].append(random.choice(range(0,4)))
        pattern["snare_chorus"].append(random.choice(range(0,4)))
    return pattern

def makeDrumsBarVerse(drumGeneralVolume,pattern,totalBarsDrums):
    bars=0
    for i in range(0,8):
        volumeKick=drumGeneralVolume
        volumeSnare=drumGeneralVolume
        if pattern["kick_verse"][i]==0 and i!=0:
            volumeKick=0
        if pattern["snare_verse"][i]==0:
            volumeSnare=0
        noteKick=Note(theKey,3,0.5,volumeKick)
        noteSnare=Note(theKey,3,0.5,volumeSnare)
        empty=Note(theKey,3,0.5,0)
        kickTrack.addNote(noteKick)
        kickTrack.addNote(empty)
        snareTrack.addNote(empty)
        snareTrack.addNote(noteSnare)
        bars+=1
        print("drum bar "+str(totalBarsDrums)+"----------")
        print("kick:"+noteKick.name+" "+str(volumeKick))
        print("snare:"+noteSnare.name+" "+str(volumeSnare))
        print("bars from verse"+str(bars))
    return bars

def makeDrumsBarChorus(drumGeneralVolume,pattern,totalBarsDrums):
    bars=0
    for i in range(0,16):
        volumeKick=drumGeneralVolume
        volumeSnare=drumGeneralVolume
        if pattern["kick_chorus"][i]==0 and i!=0:
            volumeKick=0
        if pattern["snare_chorus"][i]==0:
            volumeSnare=0
        noteKick=Note(theKey,3,0.25,volumeKick)
        noteSnare=Note(theKey,3,0.25,volumeSnare)
        empty=Note(theKey,3,0.25,0)
        kickTrack.addNote(noteKick)
        kickTrack.addNote(empty)
        snareTrack.addNote(empty)
        snareTrack.addNote(noteSnare)
        bars+=0.5
        print("drum bar "+str(totalBarsDrums)+"----------")
        print("kick:"+noteKick.name+" "+str(volumeKick))
        print("snare:"+noteSnare.name+" "+str(volumeSnare))
        print("bars from chorus"+str(bars))
    return bars

def addPercussion(progression):
    '''creates drum pattern based on parameter,and adds ut to drum track,kick and snare go in alternate patterns'''
    drumGeneralVolume=100
    pattern=makeDrumPatterns()
    #create the repeating pattern
    #add the repeating pattern
    totalBarsDrums=0
    for loops in range(0,2):
        for loops in range(0,4):
            totalBarsDrums+=makeDrumsBarVerse(drumGeneralVolume,pattern,totalBarsDrums)
        print("bars so far:"+str(totalBarsDrums))
        for i in range(0,4):
            totalBarsDrums+=makeDrumsBarChorus(drumGeneralVolume,pattern,totalBarsDrums)
        print("bars so far:"+str(totalBarsDrums))
    print(totalBarsDrums)
    assert totalBarsDrums==128

def bassVolumePattern():
    theSeq=[]
    for i in range(0,4):
        options=[0,1]
        choice=random.choice(options)
        theSeq.append(choice)
    print("-------------bass volumes sequence-----------")
    pprint(theSeq)
    return theSeq

def makeChordsFromPattern(progression,volume):
    chord1=RomanChord(progression['progression'][0],4,1,theKey,progression['flavor'][0],volume)
    chord2=RomanChord(progression['progression'][1],4,1,theKey,progression['flavor'][1],volume)
    chord3=RomanChord(progression['progression'][2],4,1,theKey,progression['flavor'][2],volume)
    chord4=RomanChord(progression['progression'][3],4,1,theKey,progression['flavor'][3],volume)
    chords=[chord1,chord2,chord3,chord4]
    return chords

def addBassBar(chordNotes,bassGeneralVolume,bassVolumes):
    pattern=[]
    totalBars=0
    for j in range(0,16):
        for ch in chordNotes:
            for i in range(0,4):
                if i==0:
                    volume=bassGeneralVolume
                    print(ch.getNotes()[0].name)
                    note=Note(ch.getNotes()[0].name,3,0.5,volume)
                    totalBars+=0.5
                else:
                    volume=random.choice([0,bassGeneralVolume])*bassVolumes[i]
                    note=Note(ch.getNotes()[0].name,3,0.5,volume)
                    totalBars+=0.5
                pattern.append(note)
                print("bass note")
                print(str(totalBars)+" "+note.name+" "+str(volume))
    assert totalBars==128
    return pattern

def addBass(progression):
    '''creates bass pattern based on parameter,and adds ut to bass track'''
    bassGeneralVolume=100
    theory=MusicTheory()
    scales=theory.getMajorScales()[theKey]
    bassVolumes=bassVolumePattern()
    print(scales)
    chordNotes=makeChordsFromPattern(progression,bassGeneralVolume)
    pattern=addBassBar(chordNotes,bassGeneralVolume,bassVolumes)
    for n in pattern:
        bassTrack.addNotes(n)

def verseSeq():
    '''make the basic sequence of notes used for verse lines,preferes smooth transitions'''
    theSeq=[]
    result=2
    for i in range(0,7):
        options=[0,-1,+1]
        choice=random.choice(options)
        result=result+choice
        if result<0:
            result=0
        elif result>6:
            result=6
        theSeq.append(result)
    print("-------------verse sequence-----------")
    pprint(theSeq)
    return theSeq


def volumeVerseMaker():
    '''make the basic sequence of volumes for tge verse'''
    theSeq=[]
    for i in range(0,7):
        options=[0,1]
        choice=random.choice(options)
        theSeq.append(choice)
    print("-------------verse volumes-----------")
    pprint(theSeq)
    return theSeq


def melodyPatternVariables(progression):
    v={}
    v["generalMelodyVolume"]=120
    v["sequenceVerse"]=verseSeq()
    v["volumePatternVerse"]=volumeVerseMaker()
    v["sequenceChorus"]=verseSeq()
    v["volumePatternChorus"]=volumeVerseMaker()
    v["patternVerse"]=[]
    v["patternChorus"]=[]
    v["chords"]=makeChordsFromPattern(progression,v["generalMelodyVolume"])
    return v

def doOnFirstNoteOfBarChorus(variablesNeededForMelody,i,j,totalBars,scales):
    volume=variablesNeededForMelody["generalMelodyVolume"]
    nnn=random.choice(variablesNeededForMelody["chords"][j].getNotes())
    note=Note(nnn.name,5,0.5,volume)
    totalBarsChange=0.5
    print("fixed chorus note")
    print(note.name+"-"+str(volume)+" "+str(totalBars))
    variablesNeededForMelody["patternChorus"].append(note)
    return totalBarsChange


def doOnFirstNoteOfBarVerse(variablesNeededForMelody,i,j,totalBars,scales):
    volume=variablesNeededForMelody["generalMelodyVolume"]*variablesNeededForMelody["volumePatternVerse"][i]
    nnn=random.choice(variablesNeededForMelody["chords"][j].getNotes())
    note=Note(nnn.name,4,0.5,volume)
    totalBarsChange=0.5
    print("variable verse note")
    print(note.name+"-"+str(volume)+" "+str(totalBars))
    variablesNeededForMelody["patternVerse"].append(note)
    return totalBarsChange

def doOnOtherNoteOfBarVerse(variablesNeededForMelody,i,j,totalBars,scales):
    volume=variablesNeededForMelody["generalMelodyVolume"]*variablesNeededForMelody["volumePatternVerse"][i]
    totalBarsChange=0.25
    print("fixed verse note")
    note=Note(scales[variablesNeededForMelody["sequenceVerse"][i]],4,0.25,volume)
    print(note.name+"-"+str(volume)+" "+str(totalBars))
    variablesNeededForMelody["patternVerse"].append(note)
    return totalBarsChange

def doOnOtherNoteOfBarChorus(variablesNeededForMelody,i,j,totalBars,scales):
    volume=random.choice([0,variablesNeededForMelody["generalMelodyVolume"]])*variablesNeededForMelody["volumePatternChorus"][i]
    totalBarsChange=0.25
    print("variable chorus note")
    note=Note(scales[variablesNeededForMelody["sequenceChorus"][i]],5,0.25,volume)
    print(note.name+"-"+str(volume)+" "+str(totalBars))
    variablesNeededForMelody["patternChorus"].append(note)
    return totalBarsChange

def makeMelodyPattern(scales,progression):
    '''creates melody pattern based on parameter,and adds ut to melody track,verse'''
    variablesNeededForMelody=melodyPatternVariables(progression)
    totalBars=0
    for verseLength in range(0,2):
        for j in range(0,4):
            print("adding verse------------------")
            for i in range(0,7):
                if i==0:
                    totalBars+=doOnFirstNoteOfBarVerse(variablesNeededForMelody,i,j,totalBars,scales)
                else:
                    totalBars+=doOnOtherNoteOfBarVerse(variablesNeededForMelody,i,j,totalBars,scales)
            for n in variablesNeededForMelody["patternVerse"]:
                print("here are the names verse")
                print(n.name+" "+str(n.volume))
    print("--------------------------end of verse----------------")

    for chorusLength in range(0,2):
        for j in range(0,4):
            print("adding chorus----------------")
            for i in range(0,7):
                if i==0:
                    totalBars+=doOnFirstNoteOfBarChorus(variablesNeededForMelody,i,j,totalBars,scales)
                else:
                    totalBars+=doOnOtherNoteOfBarChorus(variablesNeededForMelody,i,j,totalBars,scales)
            for n in variablesNeededForMelody["patternChorus"]:
                print("here are the names chorus")
                print(n.name+" "+str(n.volume))
        print("--------------------------end of chorus----------------")
    print(totalBars)
    assert totalBars==32
    return variablesNeededForMelody


def makeMelody(progression):
    '''add chorus and verse to melody track'''
    theory=MusicTheory()
    scales=theory.getMajorScales()[theKey]
    print(scales)
    patterns=makeMelodyPattern(scales,progression)
    for times in range(0,4):
        for j in patterns["patternVerse"]:
            melodyTrack.addNotes(j)
        for x in patterns["patternChorus"]:
            melodyTrack.addNotes(x)

def majorOrMinor(pattern):
    '''decides if chord comes from major or minor key'''
    ch=1
    return ch

def exportFile():
    '''adds all tracks to file and exports it,name based on date'''
    easyMIDI.addTrack(track1)
    easyMIDI.addTrack(kickTrack)
    easyMIDI.addTrack(snareTrack)
    easyMIDI.addTrack(bassTrack)
    easyMIDI.addTrack(melodyTrack)
    name=getTheTime()
    #easyMIDI.writeMIDI("songs/"+name+".mid")
    easyMIDI.writeMIDI("../../storage/downloads/"+name+".mid")

def makeSong():
    '''main function,delegates to other functions'''
    progression=createProgression()
    addProgression(progression)
    addPercussion(progression)
    addBass(progression)
    makeMelody(progression)
    exportFile()

makeSong()


