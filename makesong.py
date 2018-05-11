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

def addPercussion(progression):
    '''creates drum pattern based on parameter,and adds ut to drum track,kick and snare go in alternate patterns'''
    drumGeneralVolume=100
    pattern_kick_verse=[]
    pattern_kick_chorus=[]
    pattern_snare_verse=[]
    pattern_snare_chorus=[]
    print("pattern created empty")
    #create the repeating pattern
    for j in range(0,8):
        pattern_kick_verse.append(random.choice(range(0,4)))
        pattern_snare_verse.append(random.choice(range(0,4)))
    for u in range(0,16):
        pattern_kick_chorus.append(random.choice(range(0,4)))
        pattern_snare_chorus.append(random.choice(range(0,4)))
    #add the repeating pattern
    totalBarsDrums=0
    for loops in range(0,2):
        for loops in range(0,4):
            for i in range(0,8):
                volumeKick=drumGeneralVolume
                volumeSnare=drumGeneralVolume
                if pattern_kick_verse[i]==0 and i!=0:
                    volumeKick=0
                if pattern_snare_verse[i]==0:
                    volumeSnare=0
                noteKick=Note(theKey,3,0.5,volumeKick)
                noteSnare=Note(theKey,3,0.5,volumeSnare)
                empty=Note(theKey,3,0.5,0)
                kickTrack.addNote(noteKick)
                kickTrack.addNote(empty)
                snareTrack.addNote(empty)
                snareTrack.addNote(noteSnare)
                totalBarsDrums+=1
                print("drum bar "+str(totalBarsDrums)+"----------")
                print("kick:"+noteKick.name+" "+str(volumeKick))
                print("snare:"+noteSnare.name+" "+str(volumeSnare))
        for i in range(0,4):
            for i in range(0,16):
                volumeKick=drumGeneralVolume
                volumeSnare=drumGeneralVolume
                if pattern_kick_chorus[i]==0 and i!=0:
                    volumeKick=0
                if pattern_snare_chorus[i]==0:
                    volumeSnare=0
                noteKick=Note(theKey,3,0.25,volumeKick)
                noteSnare=Note(theKey,3,0.25,volumeSnare)
                empty=Note(theKey,3,0.25,0)
                kickTrack.addNote(noteKick)
                kickTrack.addNote(empty)
                snareTrack.addNote(empty)
                snareTrack.addNote(noteSnare)
                totalBarsDrums+=0.5
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

def addBass(progression):
    '''creates bass pattern based on parameter,and adds ut to bass track'''
    bassGeneralVolume=100
    theory=MusicTheory()
    scales=theory.getMajorScales()[theKey]
    bassVolumes=bassVolumePattern()
    print(scales)
    chord1=RomanChord(progression['progression'][0],4,1,theKey,progression['flavor'][0],100).getNotes()[0].name
    chord2=RomanChord(progression['progression'][1],4,1,theKey,progression['flavor'][1],100).getNotes()[0].name
    chord3=RomanChord(progression['progression'][2],4,1,theKey,progression['flavor'][2],100).getNotes()[0].name
    chord4=RomanChord(progression['progression'][3],4,1,theKey,progression['flavor'][3],100).getNotes()[0].name
    chordNotes=[chord1,chord2,chord3,chord4]
    print("bass notes:")
    print(chord1+" "+chord2+" "+chord3+" "+chord4)
    pattern=[]
    totalBars=0
    for j in range(0,16):
        for ch in chordNotes:
            for i in range(0,4):
                if i==0:
                    volume=bassGeneralVolume
                    note=Note(ch,3,0.5,volume)
                    totalBars+=0.5
                else:
                    volume=random.choice([0,bassGeneralVolume])*bassVolumes[i]
                    note=Note(ch,3,0.5,volume)
                    totalBars+=0.5
                pattern.append(note)
                print("bass note")
                print(str(totalBars)+" "+note.name+" "+str(volume))
    for n in pattern:
        bassTrack.addNotes(n)
    assert totalBars==128

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

def chorusSeq():
    '''make the basic sequence of notes used for chorus lines,preferes smooth transitions'''
    theSeq=[]
    result=2
    for i in range(0,16):
        options=[0,-1,+1]
        choice=random.choice(options)
        result=result+choice
        if result<0:
            result=0
        elif result>6:
            result=6
        theSeq.append(result)
    print("------------chorus sequence -----------")
    pprint(theSeq)
    return theSeq

def makeChordsFromPattern(progression,volume):
    chord1=RomanChord(progression['progression'][0],4,1,theKey,progression['flavor'][0],volume)
    chord2=RomanChord(progression['progression'][1],4,1,theKey,progression['flavor'][1],volume)
    chord3=RomanChord(progression['progression'][2],4,1,theKey,progression['flavor'][2],volume)
    chord4=RomanChord(progression['progression'][3],4,1,theKey,progression['flavor'][3],volume)
    chords=[chord1,chord2,chord3,chord4]
    return chords

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
    

def volumeChorusMaker():
    '''make the basic sequence of volumes for the chorus'''
    theSeq=[]
    for i in range(0,15):
        options=[0,1]
        choice=random.choice(options)
        theSeq.append(choice)
    print("-------------chorus volumes-----------")
    pprint(theSeq)
    return theSeq

def makeMelodyPattern(scales,progression):
    '''creates melody pattern based on parameter,and adds ut to melody track,verse'''
    generalMelodyVolume=120
    sequenceVerse=verseSeq()
    volumePatternVerse=volumeVerseMaker()
    sequenceChorus=chorusSeq()
    volumePatternChorus=volumeChorusMaker()
    pattern=[]
    chords=makeChordsFromPattern(progression,generalMelodyVolume)
    print("---------chords------------")
    pprint(chords)
    print("--------------next round -verse----------")
    totalBars=0
    for times in range(0,4):
        for verseLength in range(0,2):
            for j in range(0,4):
                for i in range(0,7):
                    if i==0:
                        volume=generalMelodyVolume*volumePatternVerse[i]
                        nnn=random.choice(chords[j].getNotes())
                        note=Note(nnn.name,4,0.5,volume)
                        totalBars+=0.5
                        print("variable verse note")
                        print(note.name+"-"+str(volume)+" "+str(totalBars))
                        pattern.append(note)
                    else:
                        volume=generalMelodyVolume*volumePatternVerse[i]
                        totalBars+=0.25
                        print("fixed verse note")
                        note=Note(scales[sequenceVerse[i]],4,0.25,volume)
                        print(note.name+"-"+str(volume)+" "+str(totalBars))
                        pattern.append(note)
        print("--------------------------end of verse----------------")
        
        for chorusLength in range(0,2):
            for j in range(0,4):
                print("--------------next round chorus----------")
                for i in range(0,15):
                    if i==0:
                        volume=generalMelodyVolume*volumePatternChorus[i]
                        nnn=random.choice(chords[j].getNotes())
                        note=Note(nnn.name,5,0.25,volume)
                        totalBars+=0.25
                        print("fixed chorus note")
                        print(note.name+"-"+str(volume)+" "+str(totalBars))
                        pattern.append(note)
                    else:
                        volume=random.choice([0,generalMelodyVolume])*volumePatternChorus[i]
                        #pattern.append(random.choice(scales))
                        note=Note(scales[sequenceChorus[i]],5,0.125,volume)
                        totalBars+=0.125
                        print("variable chorus note")
                        print(note.name+"-"+str(volume)+" "+str(totalBars))
                        pattern.append(note)
        print("--------------------------end of chorus----------------")
    assert totalBars==128
    return pattern


def makeMelody(progression):
    '''add chorus and verse to melody track'''
    theory=MusicTheory()
    scales=theory.getMajorScales()[theKey]
    print(scales)
    pattern1=makeMelodyPattern(scales,progression)
    for j in pattern1:
        melodyTrack.addNotes(j)

def majorOrMinor(pattern):
    '''decides if chord comes from major or minor key'''
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


