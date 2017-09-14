
import fresh_tomatoes
import media

the_boss_baby=media.Movie("THE BOSS BABY","A matured small baby",
                          "https://upload.wikimedia.org/wikipedia/en/0/0e/The_Boss_Baby_poster.jpg",
                          "https://www.youtube.com/watch?v=O2Bsw3lrhvs")

bfg = media.Movie("The big friendly giant.",
                           "An orphan human girl befriends a benevolent giant",
                           "https://upload.wikimedia.org/wikipedia/en/a/af/The_BFG_poster.jpg",
                           "https://www.youtube.com/watch?v=VG5MtenlP-A")
#print(bfg.storyline)

#print(the_boss_baby.storyline)
#bfg.show.trailer()
bahubali2 = media.Movie("Bahubali 2",
                        "Kattappa continues to narrate how he ended up killing Amarendra Baahubali",
                        "https://upload.wikimedia.org/wikipedia/en/f/f9/Baahubali_the_Conclusion.jpg",  
                        "https://www.youtube.com/watch?v=sOEg_YZQsTI")

ramona_and_beezus = media.Movie("Ramona and Beezus",
                           "Story of 2 sisters.",
                           "https://upload.wikimedia.org/wikipedia/en/9/90/Ramona_and_Beezus_Poster.jpg",
                           "https://www.youtube.com/watch?v=qjW2gNQBajs")

ghazi_attack = media.Movie("The Ghazi attack",
                        "The film based on the mysterious sinking of PNS Ghazi during Indo-Pakistani War of 1971.",
                        "https://upload.wikimedia.org/wikipedia/en/e/e7/The_Ghazi_Attack_Poster.jpg",
                        "https://www.youtube.com/watch?v=Xn2qOnKuOoc")

fast_and_furious = media.Movie("Fast and Furious",
                          "The Fast and the Furious is an American franchise based on a series of action films",
                          "https://upload.wikimedia.org/wikipedia/en/5/54/Fast_and_the_furious_poster.jpg", 
                          "https://www.youtube.com/watch?v=ZsJz2TJAPjw")

movies = [the_boss_baby,bfg,bahubali2,ramona_and_beezus,ghazi_attack,fast_and_furious]
fresh_tomatoes.open_movies_page(movies)
