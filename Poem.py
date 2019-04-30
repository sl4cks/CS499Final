class Poem:

    def __init__(self, poem_path=None):
        self._lines = []  # create empty list
        if poem_path is not None:
            file = open(poem_path, "r")
            self._raw_lines = file.readlines()
            for line in self._raw_lines:
                self._lines.append(self.Line(line))  # might need to be extend instead of append

    def __str__(self):
        return "".join(self._raw_lines)

        return string[1:]

    def read_poem(self, poem_path):
        file = open(poem_path, "r")
        self._lines = [] # create empty list
        for line in file.readlines():
            self._lines.append(self.Line(line)) # might need to be extend instead of append

    def get_line(self, line_number):
        return self._lines[line_number]

    class Line:

        def __init__(self, line):
            self._words = []
            for word in line.split():
                self._words.append(self.Word(word))

        def __str__(self):
            string = ""
            for word in self._words:
                string += " " + str(word)
            return string[1:] # pop the first character, an extra space

        class Word:

            def __init__(self, word):
                self.word = word
                # maybe here we put in constructing a midi message from the word?

            # for printing, simply return the stored word
            def __str__(self):
                return self.word


def __main__():
    poem = Poem("poem.txt")
    print(poem)


if __name__ == "__main__":
    __main__()
