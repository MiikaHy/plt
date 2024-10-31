class PigLatin:

    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        vowels = ("a", "e", "i", "o", "u", "ä", "ö", "å")
        consonants = ("b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z")

        if not self.get_phrase():
            return "nil"

        if self.get_phrase().endswith("y"):
            return self.get_phrase() + "nay"
        elif self.get_phrase().endswith(vowels):
            return self.get_phrase() + "yay"
        elif self.get_phrase().endswith(consonants):
            return self.get_phrase() + "ay"

        return self.get_phrase()