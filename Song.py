import mido
from mido import Message, MidiFile, MidiTrack, MetaMessage
import time

class Song:

    def __init__(self, bpm):
        self.notes = []
        self.bpm = bpm

    def write_song(self, file_name):
        mid = MidiFile(type=0) # 0 type means all messages are on one track
        track = MidiTrack()
        mid.tracks.append(track)
        track.append(MetaMessage("set_tempo", tempo=mido.bpm2tempo(self.bpm)))
        track.append(Message('program_change', program=24, time=0))
        track.append(Message("note_on", note=60, time=0))
        track.append(Message("note_on", note=60, time=500, velocity=0))
        track.append(Message("note_on", note=64, time=0))

        mid.save(file_name)

    def play(self, midi_file, port):
        outport = mido.open_output(port)
        for msg in MidiFile(midi_file):
            time.sleep(msg.time)
            if not msg.is_meta:
                outport.send(msg)

    class Note:

        def __init__(self):
            self.duration = 0
            self.pitch = 0


def __main__():
    song = Song(240)
    file = "test.mid"
    song.write_song(file)
    song.play(file, 'IAC Driver Bus 1')


if __name__ == "__main__":
    __main__()