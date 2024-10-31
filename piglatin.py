class PigLatin:

    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if not self.get_phrase():
            return "nil"

        if self.get_phrase().endswith("y"):
            return self.get_phrase() + "nay"
        return self.get_phrase()