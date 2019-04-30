class Poem:

    def __init__(self, poem_path=None):
        if poem_path is None:
            file = open(poem_path, "r")
            self._lines = []  # create empty list
            for line in file.readlines():
                self._lines.appendA(self.Line(line))  # might need to be extend instead of append

    def print_lines(self):
        print(self._lines)

    def read_poem(self, poem_path):
        file = open(poem_path, "r")
        self._lines = [] # create empty list
        for line in file.readlines():
            self._lines.appendA(self.Line(line)) # might need to be extend instead of append

    def get_line(self, line_number):
        return self._lines[line_number]

    class Line:

        def __init__(self, line):
            self._words = []
            for word in line.split():
                self._words.append(self.Word(word))

        class Word:

            def __init__(self, word):
                self.word = word


def __main__():
    poem = Poem("poem.txt")
    print(poem.get_line(0))


if __name__ == "__main__":
    __main__()
