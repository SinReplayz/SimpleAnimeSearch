from AnimeEpisode import Episode
class Anime:
    def __init__(self,name, desciption = "", genre = []):
        self.name = name
        self.description = desciption
        self.genres = genre
        self.episodes = []

    def add_episodes(self, epi_name, audio = "Sub/Dub"):
        epi= Episode(self.name, epi_name, audio)
        self.episodes.append(epi)

    def remove_episodes(self, episode):
        if type(episode) == int:
            rev_episode = self.episodes.pop(episode)
            print(f"{rev_episode} has been remove form the list of episodes.")
        elif episode in self.episodes:
            self.episodes.remove(episode)
            print(f"{episode}  has been remove form the list of episodes.")
        
    def add_genres(self, genre):
        self.genres.append(genre)

    def remove_genres(self, genre):
        if genre in self.genres:
            self.genres.remove(genre)
            print(f"{genre} has been remove form {self.genres}")
        else:
            print(f"{genre} was not found in {self.genres}")

    def portray(self):
        count = 1
        print(f""" {self.name}  """)
        for episode in self.episodes:
            print(f""" {count} - {episode.name} """)