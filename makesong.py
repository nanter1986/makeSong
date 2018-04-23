from EasyMIDI import EasyMIDI,Track,Note,Chord,RomanChord 
import random
import datetime

easyMIDI = EasyMIDI()
track1 = Track("acoustic grand piano")
drumsTrack=Track("Synth Drum")

def getTheTime():
    curTime=str(datetime.datetime.now())
    return curTime


def createProgression():
    progression=1
    first=['I','VI']
    second=['II','IV']
    third=['I','VI']
    fourth=['V','VII']
    for i in range(0,3):
        track1.addChord(RomanChord(random.choice(first),4,1,'C',True,100))
        track1.addChord(RomanChord(random.choice(second),4,1,'C',True,100))
        track1.addChord(RomanChord(random.choice(third),4,1,'C',True,100))
        track1.addChord(RomanChord(random.choice(fourth),4,1,'C',True,100))
        return progression

def addPercussion(progression):
    for i in range(0,8):
        volume=100
        has=random.choice([0,1])
        if has==0 :
            volume=0
        note=Note('C',2,0.5,100)
        drumsTrack.addNotes (note)

def addBass(progression):
    #bass
    pass

def makeMelody(progression):
    #make melody based on chord progression
    pass

def exportFile():
    easyMIDI.addTrack(track1)
    name=getTheTime()
    easyMIDI.writeMIDI(name+".mid")

def makeSong():
    progression=createProgression()
    addPercussion(progression)
    addBass(progression)
    makeMelody(progression)
    exportFile()

makeSong()    


