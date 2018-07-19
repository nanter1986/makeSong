from EasyMIDI import *
import random
import datetime
from pprint import *

easyMIDI = EasyMIDI()

def chooseKey():
    #returns a random key
    keys=['C','D','E','F','G','A','B']
    key=random.choice(keys)
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

def chooseIfFree():
    options=["free","limited","thirds"]
    selection=random.choice(options)
    return selection

def chooseIfRiff():
    options=[0,1]
    selection=random.choice(options)
    return selection

theKey=chooseKey()
tempo=random.choice([220,240,260,280,300])
print("key: "+theKey)
print("tempo: "+str(tempo))
track1 = Track(organOptions['track1'],tempo)
kickTrack=Track(organOptions['kickTrack'],tempo)
snareTrack=Track(organOptions['snareTrack'],tempo)
bassTrack=Track(organOptions['bassTrack'],tempo)
melodyTrack=Track(organOptions['melodyTrack'],tempo)
harmonyTrack=Track(organOptions['melodyTrack'],tempo)
riffTrack=Track(organOptions['melodyTrack'],tempo)
theory=MusicTheory()
scales=theory.getMajorScales()[theKey]
freeMelody=chooseIfFree()
riff=chooseIfRiff()
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

def riffMaker():
    container=[]
    optionsVolume=[0,100,100]
    optionNotes=scales
    for n in range(0,8):
       volume=random.choice(optionsVolume)
       pitch=random.choice(optionNotes)
       container.append(Note(pitch,4,0.5,volume))
    return container

def addRiff(progression):
    '''adds chords to the chord track'''
    volumeOfChords=40
    riff1=riffMaker()
    riff2=riffMaker()
    totalBarschords=0
    for j in range(0,4):
        for i in range(0,8):
            for n in riff1:
                riffTrack.addNotes(n)
                totalBarschords+=0.5
        for i in range(0,8):
            for n in riff2:
                riffTrack.addNotes(n)
                totalBarschords+=0.5
    print(totalBarschords)
    assert totalBarschords==256

def addBackground(progression):
    if riff:
        addRiff(progression)
        print("R I F F")
    else:
        addProgression(progression)
        print("C H O R D S")

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
    totalBarschords=0
    for vch in range(0,4):
        for i in range(0,4):
            for t1 in range(0,2):
                track1.addChord(chord1)
                notes1=chord1.getNotes()
                totalBarschords+=1
            for t2 in range(0,2):
                track1.addChord(chord2)
                notes2=chord2.getNotes()
                totalBarschords+=1
            for t3 in range(0,2):
                track1.addChord(chord3)
                notes3=chord3.getNotes()
                totalBarschords+=1
            for t4 in range(0,2):
                track1.addChord(chord4)
                notes4=chord4.getNotes()
                totalBarschords+=1
        for i in range(0,4):
            for t1 in range(0,2):
                track1.addChord(chord5)
                notes1=chord5.getNotes()
                totalBarschords+=1
            for t2 in range(0,2):
                track1.addChord(chord6)
                notes2=chord6.getNotes()
                totalBarschords+=1
            for t3 in range(0,2):
                track1.addChord(chord7)
                notes3=chord7.getNotes()
                totalBarschords+=1
            for t4 in range(0,2):
                track1.addChord(chord8)
                notes4=chord8.getNotes()
                totalBarschords+=1
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
        for i in range(0,32):
            for times in range(0,2):
                kickTrack.addNotes(noteKickFast)
                kickTrack.addNotes(noteEmptyFast)
                snareTrack.addNotes(noteEmptyFast)
                snareTrack.addNotes(noteSnareFast)
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

def addBassBar(chordNotes,bassGeneralVolume,bassVolumes,bassVolumesChorus):
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
                        note=Note(ch.getNotes()[0].name,3,0.5,volume)
                        totalBars+=0.5
                    else:
                        volume=random.choice([0,bassGeneralVolume])*bassVolumes[i]
                        note=Note(ch.getNotes()[0].name,3,0.5,volume)
                        totalBars+=0.5
                    pattern.append(note)
        for difProgCh in range(0,4):
            for ch in ch2:
                for i in range(0,4):
                    if i==0:
                        volume=bassGeneralVolume
                        note=Note(ch.getNotes()[0].name,3,0.5,volume)
                        totalBars+=0.5
                    else:
                        volume=random.choice([0,bassGeneralVolume])*bassVolumesChorus[i]
                        note=Note(ch.getNotes()[0].name,3,0.5,volume)
                        totalBars+=0.5
                    pattern.append(note)
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
    bassVolumesChorus=bassVolumePattern()
    chordNotes=makeChordsFromPattern(progression,bassGeneralVolume)
    pattern=addBassBar(chordNotes,bassGeneralVolume,bassVolumes,bassVolumesChorus)
    for n in pattern:
        bassTrack.addNotes(n)


def pitchOptionsForSectionsFree(section):
    '''Provide the pitch movement options,more important sections get highlighted'''
    if section=="bridge":
        options=[0,+1,-1,+1,-1,+2,-2,+3,-3,+4,-4,+5,-5,+6,-6,+7,-7]
    elif section=="chorus":
        options=[0,+1,-1,+1,-1,+2,-2,+3,-3,+4,-4,+5,-5,+6,-6,+7,-7]
    elif section=="chorusVariable":
        options=[0,+1,-1,+1,-1,+2,-2,+3,-3,+4,-4,+5,-5,+6,-6,+7,-7]
    else:
        options=[0,+1,-1,+1,-1,+2,-2,+3,-3,+4,-4,+5,-5,+6,-6,+7,-7]
    return options

def pitchOptionsForSectionsLimited(section):
    if section=="bridge":
        options=[0,+1,-1,+1,-1,+2,-2]
    elif section=="chorus":
        options=[0,+1,-1,+1,-1,+2,-2,+3,-3]
    elif section=="chorusVariable":
        options=[0,+1,-1,+1,-1,+3,-3,+6,-6]
    else:
        options=[0,+1,-1]
    return options

def pitchOptionsForSectionsThirds(section):
    if section=="bridge":
        options=[0,+2,-2]
    elif section=="chorus":
        options=[0,+2,-2,+3,-3]
    elif section=="chorusVariable":
        options=[0,+2,-2,+5,-5]
    else:
        options=[0,+1,-1]
    return options

def pitchOptionsForSections(section):
    options=[]
    if freeMelody=="free":
        options=pitchOptionsForSectionsFree(section)
        print("F R E E  M E L O D Y")
    elif freeMelody=="limited":
        options=pitchOptionsForSectionsLimited(section)
        print("L I M I T E D  M E L O D Y")
    elif freeMelody=="thirds":
        options=pitchOptionsForSectionsThirds(section)
        print("T H I R D S   M E L O D Y")
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
            variablesNeededForMelody["patternVerse"].append(verseStarting[j])
            for note in verseRepeating:
                variablesNeededForMelody["patternVerse"].append(note)

    for bridgeLength in range(0,2):
        for j in range(0,4):
            variablesNeededForMelody["patternBridge"].append(bridgeStarting[j])
            for note in bridgeRepeating:
                variablesNeededForMelody["patternBridge"].append(note)

    for chorusLength in range(0,2):
        for j in range(0,4):
            variablesNeededForMelody["patternChorus"].append(chorusStarting[j])
            for note in chorusRepeating:
                variablesNeededForMelody["patternChorus"].append(note)


    for chorusVarLength in range(0,2):
        for j in range(0,4):
            variablesNeededForMelody["patternChorusVariable"].append(chorusStarting[j])
            print(chorusStarting[j].name+" "+str(chorusStarting[j].octave)+" "+str(chorusStarting[j].volume))
            for note in chorusRepVar:
                variablesNeededForMelody["patternChorusVariable"].append(note)

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
        for y in patterns["patternBridge"]:
            melodyTrack.addNotes(y)
        for x in patterns["patternChorus"]:
            melodyTrack.addNotes(x)
        for z in patterns["patternChorusVariable"]:
            melodyTrack.addNotes(z)
    return patterns

def noteAbsoluteTranslator(inputNote):
    absolutePosition=0
    theory=MusicTheory()
    scales=theory.getMajorScales()[theKey]
    pprint(scales)
    for note in scales:
        if note==inputNote.name:
            print("match found")
            print(note)
            index=scales.index(note)
            print("index of note:")
            print(str(index))
            octave=inputNote.getOctave()
            print("octave of note:")
            print(str(octave))
            print("print absolute position:")
            absolutePosition=index+octave*7
            print(absolutePosition)
            break
    return absolutePosition

def noteOctavePositionTranslator(inputNoteAbsolutePosition):
    octave=0
    index=0
    print("note octave translator runs")
    theory=MusicTheory()
    scales=theory.getMajorScales()[theKey]
    pprint(scales)
    octave=inputNoteAbsolutePosition//7
    index=inputNoteAbsolutePosition%7
    print("input absolute position")
    print(str(inputNoteAbsolutePosition))
    print("index of note:")
    print(str(index))
    print("octave of note:")
    print(str(octave))
    theDict={"index":index,"octave":octave}
    return theDict

def patternHarmonizer(pattern):
    harmonizedPattern=[]
    for note in pattern:
        nKey=theKey
        nIndex=scales.index(note.name)
        nOctave=note.getOctave()
        nDuration=note.getDuration()
        nVolume=note.getVolume()
        absNote=noteAbsoluteTranslator(note)
        newAbs=absNote-2
        octaveAndIndexDict=noteOctavePositionTranslator(newAbs)
        print("key:"+nKey)
        print("index:"+str(nIndex))
        print("octave old:"+str(nOctave))
        print("duration:"+str(nDuration))
        print("volume:"+str(nVolume))
        print("octave new:"+str(octaveAndIndexDict["octave"]))
        print("index new:"+str(octaveAndIndexDict["index"]))
        newNote=Note(scales[octaveAndIndexDict["index"]],octaveAndIndexDict["octave"],nDuration,nVolume)
        harmonizedPattern.append(newNote)
    return harmonizedPattern

def makeHarmony(patterns,melodyToFeedHarmonyCreation):
    noteEmpty=Note(theKey,2,1,0)
    total=[]
    for i in range(0,128):
        total.append(noteEmpty)
    print("harmony track")
    notesEmpty=harmonyTrack.getNotes()
    for n in notesEmpty:
       print(n.name+" "+str(notesEmpty.index(n))+" "+str(len(notesEmpty)))
    print("-----------patterns---------------")
    pprint(patterns)
    theory=MusicTheory()
    scales=theory.getMajorScales()[theKey]
    print("---------------feed--------------")
    harmonizedVerse=patternHarmonizer(melodyToFeedHarmonyCreation["patternVerse"])
    harmonizedBridge=patternHarmonizer(melodyToFeedHarmonyCreation["patternBridge"])
    harmonizedChorus=patternHarmonizer(melodyToFeedHarmonyCreation["patternChorus"])
    harmonizedChorusVariable=patternHarmonizer(melodyToFeedHarmonyCreation["patternChorusVariable"])
    for round in range(0,2):
        for v in harmonizedVerse:
            total.append(v)
        for b in harmonizedBridge:
            total.append(b)
        for c in harmonizedChorus:
            total.append(c)
        for cv in harmonizedChorusVariable:
            total.append(cv)
    harmonyTrack.addNotes(total)
    print("----------pprint harmony track---------")
    print("-----------patterns end---------------")

def majorOrMinor(pattern):
    '''decides if chord comes from major or minor key'''
    ch=1
    return ch

def exportFile():
    '''adds all tracks to file and exports it,name based on date'''
    easyMIDI.addTrack(track1)
    easyMIDI.addTrack(kickTrack)
    easyMIDI.addTrack(snareTrack)
    notesInTrackS=snareTrack.getNotes()
    easyMIDI.addTrack(bassTrack)
    easyMIDI.addTrack(melodyTrack)
    easyMIDI.addTrack(harmonyTrack)
    name=getTheTime()
    hasRiff="riff"
    if not riff:
        hasRiff="Chords"
    if freeMelody=="free":
        freedom="FREE"
    elif freeMelody=="thirds":
        freedom="THIRDS"
    else:
        freedom="LIMITED"
    #easyMIDI.writeMIDI("songs/"+name+".mid")
    easyMIDI.writeMIDI("../../../storage/downloads/"+name+freedom+hasRiff+".mid")
    #easyMIDI.writeMIDI("../../storage/"+name+".mid")

def makeSong():
    '''main function,delegates to other functions'''
    progression=createProgression()
    addBackground(progression)
    addPercussion(progression)
    addBass(progression)
    melodyToFeedHarmonyCreation=makeMelody(progression)
    makeHarmony(progression,melodyToFeedHarmonyCreation)
    notes=harmonyTrack.getNotes()
    pprint(notes)
    totalDuration=0
    exportFile()

makeSong()


