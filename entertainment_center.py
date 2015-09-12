import media
import fresh_tomatoes

toy_story=media.Movie("Toy Story","A story in which toys come to life",
                      "http://img1.wikia.nocookie.net/__cb20140816182710/disney/images/4/4c/Toy-story-movie-posters-4.jpg"
                      ,"https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toy_story.storyline)

#toy_story.show_trailer()

twmr=media.Movie("Tanu weds Manu returns",
                 "Story of life after marriage"
                 ,"http://media2.intoday.in/indiatoday/images/stories/tanu-fullsize-story_032315071941.jpg"
                 ,"www.youtube.com/watch?v=wGGmyaurjAI")

#twmr.show_trailer()

ddlj=media.Movie("Dilwale Dulhania Le Jayenge",
                 "Raj and Simran meet on a trip to Europe. After some initial misadventures, they fall in love. The battle begins to win over two traditional families."
                 ,"https://kayfil.files.wordpress.com/2013/04/dilwale-dulhania-le-jayenge.jpg"
                 ,"www.youtube.com/watch?v=c25GKl5VNeY")

rnbdj=media.Movie("Rab Ne Bana Di Jodi"
                  ,"After the wedding ceremony between Surinder Sahni and Taani, Surinder discovers that his new wife cares little for him. When she decides to enter a dance competition, Surinder disguises himself, joins the class and tries to befriend her. Taani soon falls in love with her new dance partner, Raj, unaware that he is in fact her husband."
                  ,"https://upload.wikimedia.org/wikipedia/en/a/ab/Rab_Ne_Bana_Di_Jodi.jpg"
                  ,"www.youtube.com/watch?v=eBi8syxPd14")

Avengers=media.Movie("Avengers-The Age of Ultron"
                     ,"When Tony Stark (Robert Downey Jr.) jump-starts a dormant peacekeeping program, things go terribly awry, forcing him, Thor (Chris Hemsworth), the Incredible Hulk (Mark Ruffalo) and the rest of the Avengers to reassemble. As the fate of Earth hangs in the balance, the team is put to the ultimate test as they battle Ultron, a technological terror hell-bent on human extinction. Along the way, they encounter two mysterious and powerful newcomers, Pietro and Wanda Maximoff."
                     ,"https://upload.wikimedia.org/wikipedia/en/1/1b/Avengers_Age_of_Ultron.jpg"
                     ,"www.youtube.com/watch?v=JAUoeqvedMo")

minions=media.Movie("Minions"
                    ,"Evolving from single-celled yellow organisms at the dawn of time, Minions live to serve, but find themselves working for a continual series of unsuccessful masters, from T. Rex to Napoleon. Without a master to grovel for, the Minions fall into a deep depression. But one minion, Kevin, has a plan; accompanied by his pals Stuart and Bob, Kevin sets forth to find a new evil boss for his brethren to follow. Their search leads them to Scarlet Overkill, the world's first-ever super-villainess."
                    ,"http://sumnersunsettheatre.com/wp-content/uploads/Minions-poster.jpg"
                    ,"www.youtube.com/watch?v=P9-FCC6I7u0")

movies=[toy_story,twmr,ddlj,rnbdj,Avengers,minions]

fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)



