import mido

class Song:

    def __init__(self):
        self.Note = self.Note()

    class Note:

        def __init__(self):
            self.Rhythm = self.Rhythm()
            self.pitch = 0

        class Rhythm:

            def __init__(self):
                self.duration = 0
