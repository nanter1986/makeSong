from EasyMIDI import EasyMIDI,Track,Note,Chord,RomanChord
from random import choice

easyMIDI = EasyMIDI()
track1 = Track("acoustic grand pino")

c = Note('C', octave = 5, duration = 1/4, volume = 100)
e = Note('E', 5)
g = Note('G', 5)
chord = Chord([c,e,g])  # a chord of notes C, E and G
track1.addNotes([c, e, g, chord])

track1.addNotes(RomanChord('I*', octave = 5, duration = 1))


def createProgression():
    first=['I','VI']
    second=['II','IV']
    third=['I','VI']
    fourth=['V','VII']
    track1.addChord(RomanChord(random.choice(first),4,1 'C',True,100))
    track1.addChord(RomanChord(random.choice(second),4,1 'C',True,100))
    track1.addChord(RomanChord(random.choice(third),4,1 'C',True,100))
    track1.addChord(RomanChord(random.choice(fourth),4,1 'C',True,100))

def addPercussion(progression):
    #drums

def addBass(progression):
    #bass

def makeMelody(progression):
    #make melody based on chord progression

def exportFile():
    easyMIDI.addTrack(track1)
    easyMIDI.writeMIDI("output.mid")


