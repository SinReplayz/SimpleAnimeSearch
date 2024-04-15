class Episode:
    def __init__(self, ani_name, epi_name, audio):
        self.ani_name = ani_name
        self.name = epi_name
        if audio == "Sub":
            self.audio = "Sub"
        else:
            self.audio = audio
