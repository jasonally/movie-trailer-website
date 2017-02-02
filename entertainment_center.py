import fresh_tomatoes
import media

# Each movie is initialized as an instance of the Movie class.
# Each movie has a title, duration in minutes, storyline, poster image URL,
# year the movie was released, and a YouTube trailer URL.
star_trek = media.Movie("Star Trek",
                        "127",
                        "During the USS Enterprise's maiden voyage the crew \
                            faces a threat to the entire Federation.",
                        "https://upload.wikimedia.org/wikipedia/en/2/29/Startrekposter.jpg",
                        "2009",
                        "https://www.youtube.com/watch?v=iGAHnZ555nI")
                        
the_dark_knight = media.Movie("The Dark Knight",
                              "152",
                              "Batman takes on his toughest opponent yet: a \
                                  criminal who doesn't play by the normal \
                                  rules.",
                              "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                              "2008",
                              "https://www.youtube.com/watch?v=EXeTwQWrcwY")
                              
fast_five = media.Movie("Fast Five",
                        "130",
                        "Dom Toretto and his crew must do one final job in Rio \
                            before gaining their freedom for good.",
                        "https://upload.wikimedia.org/wikipedia/en/0/0c/Fast_Five_poster.jpg",
                        "2011",
                        "https://www.youtube.com/watch?v=mw2AqdB5EVA")
                        
inside_out = media.Movie("Inside Out",
                         "94",
                         "The story of our feelings and what's going on inside \
                             our heads.",
                         "https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg",
                         "2015",
                         "https://www.youtube.com/watch?v=yRUAzGQ3nSY")
                         
harry_potter = media.Movie("Harry Potter and the Philosopher's Stone",
                           "152",
                           "A orphan learns he is part of a magical world he \
                               never dreamed existed.",
                           "http://www.tribute.ca/harrypotter/images/HP1/harry_potter_and_the_sorcerers_stone_poster5.jpg",
                           "2001",
                           "https://www.youtube.com/watch?v=PbdM1db3JbY")
                           
casino_royale = media.Movie("Casino Royale",
                            "144",
                            "A reboot of the James Bond film series that \
                                establishes a new timeline and framework.",
                            "http://www.the007dossier.com/007Dossier/james-bond-007-movie-posters/casino-royale/Casino%20Royale%20Poster%203.jpg",
                            "2006",
                            "https://www.youtube.com/watch?v=GV_18deeAXk")
                            
star_wars = media.Movie("Star Wars: The Force Awakens",
                        "136",
                        "New and old characters alike team up as a threat to \
                            the galaxy emerges.",
                        "https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg",
                        "2015",
                        "https://www.youtube.com/watch?v=ngElkyQ6Rhs&t=4s")
                        
superbad = media.Movie("Superbad",
                       "113",
                       "Two high school seniors hope to become part of the \
                           in-crowd before graduating.",
                       "https://upload.wikimedia.org/wikipedia/en/8/8b/Superbad_Poster.png",
                       "2007",
                       "https://www.youtube.com/watch?v=_f_MlMY3X2c")
                        
the_lion_king = media.Movie("The Lion King",
                        "88",
                        "A young lion's quest to take back his homeland from \
                            his wicked uncle.",
                        "https://upload.wikimedia.org/wikipedia/en/3/3d/The_Lion_King_poster.jpg",
                        "1994",
                        "https://www.youtube.com/watch?v=4sj1MT05lAA")

# The movies list contains the name of every initialized movie.
movies = [star_trek, the_dark_knight, fast_five, inside_out, casino_royale, 
          star_wars, superbad, the_lion_king, harry_potter]

fresh_tomatoes.open_movies_page(movies)