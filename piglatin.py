class PigLatin:

    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        vowels = ("a", "e", "i", "o", "u", "ä", "ö", "å")
        consonants = ("b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z")
        phrase = self.get_phrase()
        split_phrase = phrase.split(" ")
        tmp = ""

        if not phrase:
            return "nil"

        if len(split_phrase) > 1:
            for word in split_phrase:
                if word.endswith("y"):
                    tmp += phrase + "nay"
                elif word.startswith(consonants):
                    if word[1] in consonants:
                        tmp += word[2:] + word[0] + word[1] + "ay"
                    tmp += word[1:] + word[0] + "ay"
                elif word.endswith(vowels):
                    tmp += word + "yay"
                elif word.endswith(consonants):
                    tmp += word + "ay"
                tmp += " "
            return tmp.rstrip(" ")

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