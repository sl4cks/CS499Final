import mido
from mido import Message, MidiFile, MidiTrack, MetaMessage
import time
from Poem import Poem

class Song:

    def __init__(self, bpm):
        self.notes = []
        self.bpm = bpm
        self.beat = mido.bpm2tempo(bpm)
        self._scale_intervals = [0, 2, 4, 5, 7, 9, 11, 12]

        # define arpeggios
        self._arpeggios = {"major": [0, 4, 7, 12],
                           "minor": [0, 3, 7, 12],
                           "diminished": [0, 3, 6, 12],
                           "major7": [0, 4, 7, 11],
                           "minor7": [0, 3, 7, 10],
                           "dom7": [0, 4, 7, 10]}

    def sum_string(self, syllable):
        sum = 0
        for letter in str(syllable):
            sum += ord(letter)

        return sum

    def song_from_poem(self, text_file):
        poem = Poem(text_file) # read the file as a Poem object

        # choose a root to our arpeggio
        root = 60 + (poem.total_syllables() % 12)

        # iterate over each syllable
        for line in poem.lines:
            chord_root = root + self._scale_intervals[(self.sum_string(str(line)) % 8)]
            for word in line.words:
                if chord_root == 1 or chord_root == 3 or chord_root == 5:
                    chord_type = "major"
                else:
                    chord_type = "minor"

                # determine pitch by summing characters
                pitch = (self.sum_string(str(word))) % len(self._arpeggios[chord_type])

                # determine duration by length of syllable
                duration = (word.syllables % 3)+1

                # add the new note to our local list of notes
                self.notes.append(self.Note(chord_root+self._arpeggios[chord_type][pitch], duration))

    def write_song(self, file_name):
        mid = MidiFile(type=0) # 0 type means all messages are on one track
        track = MidiTrack()
        mid.tracks.append(track)
        track.append(MetaMessage("set_tempo", tempo=mido.bpm2tempo(self.bpm)))

        for note in self.notes:
            track.append(Message("note_on", note=note.pitch, velocity=127, time=0))
            track.append(Message("note_on", note=note.pitch, velocity=0, time=note.duration*mid.ticks_per_beat))

        mid.save(file_name)

    def play(self, midi_file, port):
        outport = mido.open_output(port)
        for msg in MidiFile(midi_file):
            time.sleep(msg.time)
            if not msg.is_meta:
                outport.send(msg)

    class Note:

        def __init__(self, pitch, duration):
            self.pitch = pitch
            self.duration = duration


def __main__():
    song = Song(360)
    file = "mariner.mid"
    song.song_from_poem("mariner.txt")
    song.write_song(file)
    # song.play(file, 'IAC Driver Bus 1')


if __name__ == "__main__":
    __main__()