class Poem:

    def __init__(self, poem_path = None):
        if(poem_path != None):
            file = open(poem_path, "r")
            self._lines = file.readlines()

    def print_lines(self):
        print(self._lines)

    def read_poem(self, poem_path):
        file = open(poem_path, "r")
        self._lines = file.readlines()


def __main__():
    poem = Poem("poem.txt")
    poem.print_lines()

if(__name__ == "__main__"):
    __main__()