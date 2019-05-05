import mido
from mido import Message, MidiFile, MidiTrack, MetaMessage
import time
import random
import Poem

class Song:

    def __init__(self, bpm):
        self.notes = []
        self.bpm = bpm

        # define arpeggios
        self._arpeggios = {"major": [0, 4, 7, 12],
                           "minor": [0, 3, 7, 12],
                           "diminished": [0, 3, 6, 12],
                           "major7": [0, 4, 7, 11],
                           "minor7": [0, 3, 7, 10],
                           "dom7": [0, 4, 7, 10]}

    def song_from_poem(self, text_file):
        poem = Poem(text_file) # read the file as a Poem object

    def write_song(self, file_name):
        root = 60
        arp = [root, root+4, root+8, root+12]
        mid = MidiFile(type=0) # 0 type means all messages are on one track
        track = MidiTrack()
        mid.tracks.append(track)
        track.append(MetaMessage("set_tempo", tempo=mido.bpm2tempo(self.bpm)))

        for i in range(50):
            pitch = arp[random.randint(0, 3)]
            track.append(Message("note_on", note=pitch, velocity=127, time=0))
            track.append(Message("note_on", note=pitch, velocity=0, time=random.randint(1,4)*250))

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