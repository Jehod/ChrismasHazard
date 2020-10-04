class Participant:

    def __init__(self, name: str, exclusion='', mail=None) -> None:
        super().__init__()
        self.name = name
        self.exclusion = exclusion
        self.mail = mail

    def __str__(self) -> str:
        desc = f"Participant: {self.name}.   "
        if not self.exclusion:
            excl = "Il n'exlut personne.    "
        else:
            excl = f"Il ne peut être associé à : {self.exclusion}.    "
        mel = ""
        if self.mail:
            mel = f"Son mail est: {self.mail}.    "

        return desc + excl + mel
