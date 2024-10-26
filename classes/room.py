class Room:
    def __init__(self, name="", alias="", desc="", exits={}):
        self.name=name
        self.alias=alias
        self.desc=desc
        self.exits=exits