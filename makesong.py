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
    org['track1']=random.choice(['Acoustic Grand Piano'])
    org['melodyTrack']=random.choice(['Acoustic Grand Piano'])
    org['bassTrack']=random.choice(['Electric Bass (finger)'])
    org['kickTrack']=random.choice(['Synth Drum'])
    org['snareTrack']=random.choice(['Taiko Drum'])
    for key,value in org.items():
        print('organs:')
        print(key+':'+value)
    return org

organOptions=setTheOrgans()


theKey=chooseKey()
tempo=random.choice([220,240,260,280,300])
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
    progressionChorus=[]
    flavor=[]
    flavorChorus=[]
    dictChordsFlavor={}
    options=[['I','VI'],['I','III','V','VI','VII'],['II','IV'],['V']]
    print(len(options))
    for i in range(0,4):
        chord=random.choice(options[i])
        progression.append(chord)
        flavor.append(majorOrMinor(chord))
    for i in range(0,4):
        chord=random.choice(options[i])
        progressionChorus.append(chord)
        flavorChorus.append(majorOrMinor(chord))

    dictChordsFlavor['progression']=progression
    dictChordsFlavor['progressionChorus']=progressionChorus
    dictChordsFlavor['flavor']=flavor
    dictChordsFlavor['flavorChorus']=flavorChorus
    print(dictChordsFlavor)
    return dictChordsFlavor


def addProgression(progression):
    '''adds chords to the chord track'''
    volumeOfChords=40
    chord1=RomanChord(progression['progression'][0],4,1,theKey,progression['flavor'][0],volumeOfChords)
    chord2=RomanChord(progression['progression'][1],4,1,theKey,progression['flavor'][1],volumeOfChords)
    chord3=RomanChord(progression['progression'][2],4,1,theKey,progression['flavor'][2],volumeOfChords)
    chord4=RomanChord(progression['progression'][3],4,1,theKey,progression['flavor'][3],volumeOfChords)
    chord5=RomanChord(progression['progressionChorus'][0],4,1,theKey,progression['flavorChorus'][0],volumeOfChords)
    chord6=RomanChord(progression['progressionChorus'][1],4,1,theKey,progression['flavorChorus'][1],volumeOfChords)
    chord7=RomanChord(progression['progressionChorus'][2],4,1,theKey,progression['flavorChorus'][2],volumeOfChords)
    chord8=RomanChord(progression['progressionChorus'][3],4,1,theKey,progression['flavorChorus'][3],volumeOfChords)
    allChords=[chord1,chord2,chord3,chord4,chord5,chord6,chord7,chord8]
    for chd in allChords:
        notes=chd.getNotes()
        for n in notes:
            print(n.name)
        print("---------chord end----------1")
    totalBarschords=0
    for vch in range(0,4):
        for i in range(0,4):
            for t1 in range(0,2):
                track1.addChord(chord1)
                notes1=chord1.getNotes()
                totalBarschords+=1
                #print("bar "+str(totalBarschords)+" "+chord1.getNumeral())
                #for n in notes1:
                #    print("chord 1:"+n.name)
            for t2 in range(0,2):
                track1.addChord(chord2)
                notes2=chord2.getNotes()
                totalBarschords+=1
                #print("bar "+str(totalBarschords)+" "+chord2.getNumeral())
                #for n in notes2:
                #    print("chord 2:"+n.name)
            for t3 in range(0,2):
                track1.addChord(chord3)
                notes3=chord3.getNotes()
                totalBarschords+=1
                #print("bar "+str(totalBarschords)+" "+chord3.getNumeral())
                #for n in notes3:
                #    print("chord 3:"+n.name)
            for t4 in range(0,2):
                track1.addChord(chord4)
                notes4=chord4.getNotes()
                totalBarschords+=1
                #print("bar "+str(totalBarschords)+" "+chord4.getNumeral())
                #for n in notes4:
                #    print("chord 4:"+n.name)
        for i in range(0,4):
            for t1 in range(0,2):
                track1.addChord(chord5)
                notes1=chord5.getNotes()
                totalBarschords+=1
                #print("bar "+str(totalBarschords)+" "+chord1.getNumeral())
                #for n in notes1:
                #    print("chord 1:"+n.name)
            for t2 in range(0,2):
                track1.addChord(chord6)
                notes2=chord6.getNotes()
                totalBarschords+=1
                #print("bar "+str(totalBarschords)+" "+chord2.getNumeral())
                #for n in notes2:
                #    print("chord 2:"+n.name)
            for t3 in range(0,2):
                track1.addChord(chord7)
                notes3=chord7.getNotes()
                totalBarschords+=1
                #print("bar "+str(totalBarschords)+" "+chord3.getNumeral())
                #for n in notes3:
                #    print("chord 3:"+n.name)
            for t4 in range(0,2):
                track1.addChord(chord8)
                notes4=chord8.getNotes()
                totalBarschords+=1
                #print("bar "+str(totalBarschords)+" "+chord4.getNumeral())
                #for n in notes4:
                #    print("chord 4:"+n.name)
    print(totalBarschords)
    assert totalBarschords==256


def addPercussion(progression):
    '''creates drum pattern based on parameter,and adds ut to drum track,kick and snare go in alternate patterns'''
    print("start of drums----------------------------------------")
    drumGeneralVolume=120
    noteKick=Note(theKey,2,0.5,drumGeneralVolume)
    noteSnare=Note(theKey,3,0.5,drumGeneralVolume)
    noteEmpty=Note(theKey,2,0.5,0)
    noteKickFast=Note(theKey,2,0.25,drumGeneralVolume)
    noteSnareFast=Note(theKey,3,0.25,drumGeneralVolume)
    noteEmptyFast=Note(theKey,2,0.25,0)
    print("start of drums----------------------------------------")
    for i in range(0,4):
        for i in range(0,32):
            kickTrack.addNotes(noteKick)
            kickTrack.addNotes(noteEmpty)
            snareTrack.addNotes(noteEmpty)
            snareTrack.addNotes(noteSnare)
            #print(str(i)+" "+organOptions["kickTrack"]+" "+noteKick.name+organOptions["snareTrack"]+" "+noteSnare.name)
            #print("{} {} {} {} {}".format(i,organOptions["kickTrack"],noteKick.name,organOptions["snareTrack"],noteSnare.name))
        for i in range(0,32):
            for times in range(0,2):
                kickTrack.addNotes(noteKickFast)
                kickTrack.addNotes(noteEmptyFast)
                snareTrack.addNotes(noteEmptyFast)
                snareTrack.addNotes(noteSnareFast)
                #print(str(i)+" "+organOptions["kickTrack"]+" "+noteKick.name+organOptions["snareTrack"]+" "+noteSnare.name)
                #print("{} {} {} {} {}".format(i,organOptions["kickTrack"],noteKick.name,organOptions["snareTrack"],noteSnare.name))
    print("end of drums----------------------------------------")

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
    chord5=RomanChord(progression['progressionChorus'][3],4,1,theKey,progression['flavorChorus'][0],volume)
    chord6=RomanChord(progression['progressionChorus'][3],4,1,theKey,progression['flavorChorus'][1],volume)
    chord7=RomanChord(progression['progressionChorus'][3],4,1,theKey,progression['flavorChorus'][2],volume)
    chord8=RomanChord(progression['progressionChorus'][3],4,1,theKey,progression['flavorChorus'][3],volume)
    chords=[chord1,chord2,chord3,chord4,chord5,chord6,chord7,chord8]
    return chords

def addBassBar(chordNotes,bassGeneralVolume,bassVolumes):
    pattern=[]
    ch1=[chordNotes[0],chordNotes[1],chordNotes[2],chordNotes[3]]
    ch2=[chordNotes[4],chordNotes[5],chordNotes[6],chordNotes[7]]
    totalBars=0
    for j in range(0,4):
        for difProg in range(0,4):
            for ch in ch1:
                for i in range(0,4):
                    if i==0:
                        volume=bassGeneralVolume
                        #print(ch.getNotes()[0].name)
                        note=Note(ch.getNotes()[0].name,3,0.5,volume)
                        totalBars+=0.5
                    else:
                        volume=random.choice([0,bassGeneralVolume])*bassVolumes[i]
                        note=Note(ch.getNotes()[0].name,3,0.5,volume)
                        totalBars+=0.5
                    pattern.append(note)
        print("bass first half:"+str(totalBars))
        for difProgCh in range(0,4):
            for ch in ch2:
                for i in range(0,4):
                    if i==0:
                        volume=bassGeneralVolume
                        #print(ch.getNotes()[0].name)
                        note=Note(ch.getNotes()[0].name,3,0.5,volume)
                        totalBars+=0.5
                    else:
                        volume=random.choice([0,bassGeneralVolume])*bassVolumes[i]
                        note=Note(ch.getNotes()[0].name,3,0.5,volume)
                        totalBars+=0.5
                    pattern.append(note)
                    #print("bass note")
    print(str(totalBars))
    print("bass second half:"+str(totalBars))
    assert totalBars==256
    return pattern

def addBass(progression):
    '''creates bass pattern based on parameter,and adds ut to bass track'''
    bassGeneralVolume=70
    theory=MusicTheory()
    scales=theory.getMajorScales()[theKey]
    bassVolumes=bassVolumePattern()
    print(scales)
    chordNotes=makeChordsFromPattern(progression,bassGeneralVolume)
    pattern=addBassBar(chordNotes,bassGeneralVolume,bassVolumes)
    for n in pattern:
        bassTrack.addNotes(n)

def pitchOptionsForSections(section):
    '''Provide the pitch movement options,more important sections get highlighted'''
    if section=="bridge":
        options=[0,+1,-1,+1,-1,+2,-2]
    elif section=="chorus":
        options=[0,+1,-1,+1,-1,+2,-2,+3,-3]
    elif section=="chorusVariable":
        options=[0,+1,-1,+1,-1,+3,-3,+6,-6]
    else:
        options=[0,+1,-1]
    return options

def verseSeq(section):
    '''make the basic sequence of notes used for verse lines,preferes smooth transitions'''
    theSeq=[]
    result=2
    for i in range(0,7):
        options=pitchOptionsForSections(section)
        choice=random.choice(options)
        result=result+choice
        if result<0:
            result=0
        elif result>6:
            result=6
        theSeq.append(result)
    print("-------------"+section+" sequence-----------")
    pprint(theSeq)
    return theSeq

def volumeOptionsForSections(section):
    if section=="bridge":
        options=[0,1,1,1]
    elif section=="chorus":
        options=[0,1,1,1,1]
    elif section=="chorusVariable":
        options=[0,1,1,1,1,1]
    else:
        options=[0,0,1,1]
    return options

def volumeVerseMaker(section):
    '''make the basic sequence of volumes for tge verse'''
    theSeq=[]
    for i in range(0,7):
        options=volumeOptionsForSections(section)
        choice=random.choice(options)
        theSeq.append(choice)
    print("-------------"+section+" volumes-----------")
    pprint(theSeq)
    return theSeq


def melodyPatternVariables(progression):
    v={}
    v["generalMelodyVolume"]=120
    v["sequenceVerse"]=verseSeq("verse")
    v["volumePatternVerse"]=volumeVerseMaker("verse")
    v["sequenceChorus"]=verseSeq("chorus")
    v["sequenceChorusVariable"]=verseSeq("chorusVariable")
    v["sequenceBridge"]=verseSeq("bridge")
    v["volumePatternChorus"]=volumeVerseMaker("chorus")
    v["volumePatternChorusVariable"]=volumeVerseMaker("chorusVariable")
    v["volumePatternBridge"]=volumeVerseMaker("bridge")
    v["patternVerse"]=[]
    v["patternChorus"]=[]
    v["patternChorusVariable"]=[]
    v["patternBridge"]=[]
    v["chords"]=makeChordsFromPattern(progression,v["generalMelodyVolume"])
    v["chordsChorus"]=makeChordsFromPattern(progression,v["generalMelodyVolume"])
    return v


def verseFourVaryingStartingNotes(variablesNeededForMelody):
    notes=[]
    for i in range(0,4):
        volume=variablesNeededForMelody["generalMelodyVolume"]
        nnn=random.choice(variablesNeededForMelody["chords"][i].getNotes())
        note=Note(nnn.name,4,0.5,volume)
        notes.append(note)
    return notes

def chorusFourVaryingStartingNotes(variablesNeededForMelody):
    notes=[]
    for i in range(0,4):
        volume=variablesNeededForMelody["generalMelodyVolume"]
        nnn=random.choice(variablesNeededForMelody["chordsChorus"][i].getNotes())
        note=Note(nnn.name,5,0.5,volume)
        notes.append(note)
    return notes


def bridgeFourVaryingStartingNotes(variablesNeededForMelody):
    notes=[]
    for i in range(0,4):
        volume=variablesNeededForMelody["generalMelodyVolume"]
        nnn=random.choice(variablesNeededForMelody["chords"][i].getNotes())
        note=Note(nnn.name,4,0.5,volume)
        notes.append(note)
    return notes

def verseSixRepeatingNotes(variablesNeededForMelody,scales):
    notes=[]
    for i in range(0,6):
        volume=variablesNeededForMelody["generalMelodyVolume"]*variablesNeededForMelody["volumePatternVerse"][i]
        note=Note(scales[variablesNeededForMelody["sequenceVerse"][i]],4,0.25,volume)
        notes.append(note)
    return notes


def bridgeSixRepeatingNotes(variablesNeededForMelody,scales):
    notes=[]
    for i in range(0,6):
        volume=variablesNeededForMelody["generalMelodyVolume"]*variablesNeededForMelody["volumePatternBridge"][i]
        note=Note(scales[variablesNeededForMelody["sequenceBridge"][i]],4,0.25,volume)
        notes.append(note)
    return notes

def chorusSixRepeatingNotes(variablesNeededForMelody,scales):
    notes=[]
    for i in range(0,6):
        volume=variablesNeededForMelody["generalMelodyVolume"]*variablesNeededForMelody["volumePatternChorus"][i]
        note=Note(scales[variablesNeededForMelody["sequenceChorus"][i]],5,0.25,volume)
        notes.append(note)
    return notes


def chorusSixRepeatingNotesVariable(variablesNeededForMelody,scales):
    notes=[]
    for i in range(0,6):
        volume=variablesNeededForMelody["generalMelodyVolume"]*variablesNeededForMelody["volumePatternChorusVariable"][i]
        note=Note(scales[variablesNeededForMelody["sequenceChorusVariable"][i]],5,0.25,volume)
        notes.append(note)
    return notes

def makeMelodyPattern(scales,progression):
    '''creates melody pattern based on parameter,and adds ut to melody track,verse'''
    variablesNeededForMelody=melodyPatternVariables(progression)
    verseStarting=verseFourVaryingStartingNotes(variablesNeededForMelody)
    verseRepeating=verseSixRepeatingNotes(variablesNeededForMelody,scales)
    chorusStarting=chorusFourVaryingStartingNotes(variablesNeededForMelody)
    chorusRepeating=chorusSixRepeatingNotes(variablesNeededForMelody,scales)
    chorusRepVar=chorusSixRepeatingNotesVariable(variablesNeededForMelody,scales)
    bridgeStarting=verseStarting
    bridgeRepeating=bridgeSixRepeatingNotes(variablesNeededForMelody,scales)
    for verseLength in range(0,2):
        for j in range(0,4):
            print("adding verse------------------")
            variablesNeededForMelody["patternVerse"].append(verseStarting[j])
            print(verseStarting[j].name+" "+str(verseStarting[j].octave)+" "+str(verseStarting[j].volume))
            for note in verseRepeating:
                variablesNeededForMelody["patternVerse"].append(note)
                print(note.name+" "+str(note.octave)+" "+str(note.volume))
    print("--------------------------end of verse----------------")

    for bridgeLength in range(0,2):
        for j in range(0,4):
            print("adding bridge------------------")
            variablesNeededForMelody["patternBridge"].append(bridgeStarting[j])
            print(bridgeStarting[j].name+" "+str(bridgeStarting[j].octave)+" "+str(bridgeStarting[j].volume))
            for note in bridgeRepeating:
                variablesNeededForMelody["patternBridge"].append(note)
                print(note.name+" "+str(note.octave)+" "+str(note.volume))
    print("--------------------------end of bridge----------------")

    for chorusLength in range(0,2):
        for j in range(0,4):
            print("adding chorus------------------")
            variablesNeededForMelody["patternChorus"].append(chorusStarting[j])
            print(chorusStarting[j].name+" "+str(chorusStarting[j].octave)+" "+str(chorusStarting[j].volume))
            for note in chorusRepeating:
                variablesNeededForMelody["patternChorus"].append(note)
                print(note.name+" "+str(note.octave)+" "+str(note.volume))
    print("--------------------------end of chorus----------------")


    for chorusVarLength in range(0,2):
        for j in range(0,4):
            print("adding chorus variable------------------")
            variablesNeededForMelody["patternChorusVariable"].append(chorusStarting[j])
            print(chorusStarting[j].name+" "+str(chorusStarting[j].octave)+" "+str(chorusStarting[j].volume))
            for note in chorusRepVar:
                variablesNeededForMelody["patternChorusVariable"].append(note)
                print(note.name+" "+str(note.octave)+" "+str(note.volume))
    print("--------------------------end of chorus----------------")

    return variablesNeededForMelody


def makeMelody(progression):
    '''add chorus and verse to melody track'''
    theory=MusicTheory()
    scales=theory.getMajorScales()[theKey]
    print(scales)
    patterns=makeMelodyPattern(scales,progression)
    for times in range(0,4):
        print("verse starts here----------------------------")
        for j in patterns["patternVerse"]:
            melodyTrack.addNotes(j)
            #print(j.name+"/"+str(j.volume))
        print("bridge starts here----------------------------")
        for y in patterns["patternBridge"]:
            melodyTrack.addNotes(y)
            #print(y.name+"/"+str(y.volume))
        print("chorus starts here----------------------------")
        for x in patterns["patternChorus"]:
            melodyTrack.addNotes(x)
            #print(x.name+"/"+str(x.volume))
        for z in patterns["patternChorusVariable"]:
            melodyTrack.addNotes(z)
            #print(z.name+"/"+str(z.volume))

def majorOrMinor(pattern):
    '''decides if chord comes from major or minor key'''
    ch=1
    return ch

def exportFile():
    '''adds all tracks to file and exports it,name based on date'''
    easyMIDI.addTrack(track1)
    easyMIDI.addTrack(kickTrack)
    #notesInTrack=kickTrack.getNotes()
    #for n in notesInTrack:
    #    print(n.name+"/"+str(n.volume))
    #print("-------------------")
    easyMIDI.addTrack(snareTrack)
    notesInTrackS=snareTrack.getNotes()
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


