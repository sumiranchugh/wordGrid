
class Dictionary:

    def __init__(self, path):
        self.words = []
        with open(path, "r") as f:
            self.words = f.read().lower().split('\n')

    def is_valid_word(self, word, exclude_list=[]):
        if word.lower() in self.words and word not in exclude_list:
            return True

    def is_partial_match(self, word):
        for w in self.words:
            if w.startswith(word.lower()):
                return True
        return False
