class PigLatin:

    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        if self.phrase == "":
            return "nil"
        return self.phrase

    def translate(self) -> str:
        pass
