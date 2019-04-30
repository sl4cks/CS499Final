class Poem:

    def __init__(self, poem_path=None):
        if (poem_path != None):
            file = open(poem_path, "r")
            self._lines = file.readlines()

    def print_lines(self):
        print(self._lines)

    def read_poem(self, poem_path):
        file = open(poem_path, "r")
        self._lines = file.readlines()

    def get_line(self, line_number):
        return self._lines[line_number]

    def __iter__(self):
        return self._lines.__iter__()

    def __next__(self):
        return self._lines.__next__()

    class Line:

        def __init__(self):
            self.line = "test" #filler

        class Word:

            def __init__(self):
                self.word = "word" #filler


def __main__():
    poem = Poem("poem.txt")
    print(poem.get_line(0))


if (__name__ == "__main__"):
    __main__()
