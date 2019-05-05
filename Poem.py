import syllables as syl

class Poem:

    def __init__(self, poem_path=None):
        self.lines = []  # create empty list
        if poem_path is not None:
            file = open(poem_path, "r")
            self._raw_lines = file.readlines()
            for line in self._raw_lines:
                self.lines.append(self.Line(line))  # might need to be extend instead of append

    def __str__(self):
        return "".join(self._raw_lines)

    def read_poem(self, poem_path):
        file = open(poem_path, "r")
        self.lines = [] # create empty list
        for line in file.readlines():
            self.lines.append(self.Line(line)) # might need to be extend instead of append

    def get_line(self, line_number):
        return self.lines[line_number]

    def total_syllables(self):
        sum = 0
        for line in self.lines:
            sum += line.total_syllables()
        return sum

    class Line:

        def __init__(self, line):
            self.words = []
            for word in line.split():
                self.words.append(self.Word(word))

        def __str__(self):
            string = ""
            for word in self.words:
                string += " " + str(word)
            return string[1:] # pop the first character, an extra space

        def get_word(self, word_number):
            return self.words[word_number]

        def total_syllables(self):
            sum = 0
            for word in self.words:
                sum += word.syllables

            return sum

        class Word:

            def __init__(self, word):
                self.word = word
                self.syllables = syl.estimate(word)

            # for printing, simply return the stored word
            def __str__(self):
                return self.word


def __main__():
    poem = Poem("poem.txt")
    print(poem.get_line(0))


if __name__ == "__main__":
    __main__()
