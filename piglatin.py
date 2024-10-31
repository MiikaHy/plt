class PigLatin:

    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        vowels = ("a", "e", "i", "o", "u", "ä", "ö", "å")
        consonants = ("b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z")
        phrase = self.get_phrase()

        if not phrase:
            return "nil"

        if phrase.endswith("y"):
            return phrase + "nay"
        elif phrase.startswith(consonants):
            if phrase[1] in consonants:
                return phrase[2:] + phrase[0] + phrase[1] + "ay"
            return phrase[1:] + phrase[0] + "ay"
        elif phrase.endswith(vowels):
            return phrase + "yay"
        elif phrase.endswith(consonants):
            return phrase + "ay"

        return phrase