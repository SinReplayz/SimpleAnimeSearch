from AnimeList import anime_list
new_list = anime_list
def intro():
    intro = ("""
         _______________________________
        *                               *
        *                               *
        *    Willy The Hippo Anime's    *
        *                               *
        *_______________________________*""")
    print(intro)
    choosing()

def choosing():
        choice = input("""
         _______________________________
        *           -Choice-            *
        *                               *
        *       Type in key words       *
        *       or genre that you       *
        *    migth be interested inn    *
        *    like 'magic', fighting,    *
        *         'isekai' ,etc.        *
        *_______________________________*\n""")
        find(choice)
            
def find(answer):
    pick_list = []
    for anime in new_list:
        if anime.genres != []:
            for genre in anime.genres:
                if genre.lower().find(answer.lower()) != -1:
                    pick_list.append(anime)
                    continue
        if anime.description.lower().find(answer.lower()) != -1:
            pick_list.append(anime)
    if pick_list == []:
        print("""\n
            'Sorry no choices please try another'      """)
        choosing()
    pick_anime(pick_list)

def pick_anime(animes):
    print("""
        *_______________________________*
                Choice your Anime       
          or type 0 for other choices   \n""")
    count = 1
    for anime in animes:
        print(f"\n            {count} - {anime.name}")
        print(f"            Description: {anime.description}")
        count += 1

    choice = int(input("""        *_______________________________*
                       """))
    if choice == 0:
        choosing()
    elif choice - 1 <= len(animes) and choice - 1 > -1:
        animes[choice - 1].portray()
    else:
        print("""\n
              'Pick a valid choice'      """)
        choosing()

intro()
