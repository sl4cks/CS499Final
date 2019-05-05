import mido
from mido import Message, MidiFile, MidiTrack, MetaMessage
import time

class Song:

    def __init__(self, bpm, corpus):
        self.notes = []
        self.bpm = bpm

    def write_song(self):
        mid = MidiFile()
        track = MidiTrack()
        mid.tracks.append(track)
        track.append(MetaMessage("set_tempo", mido.bpm2tempo(self.bpm)))
        track.append(Message("note_on", note=60, time=50))
        track.append(MetaMessage("end_of_track"))

    def play(self, output):
        outport = mido.open_output()
        for note in self.notes:
            outport.send(mido.Message("note_on", note=note.pitch, velocity=127))
            time.sleep(note.duration)
            outport.send(mido.Message("note_on", note=note.pitch, velocity=0))

    class Note:

        def __init__(self):
            self.duration = 0
            self.pitch = 0

def __main__():
    print("Running main!")

if(__name__ == __main__):
    __main__()