import fresh_tomatoes
import media

# Create Movie instances
the_croods = media.Movie("The Croods",
                         "https://upload.wikimedia.org/wikipedia/en/thumb/7/72/The_Croods_poster.jpg/220px-The_Croods_poster.jpg",
                         "https://www.youtube.com/watch?v=4fVCKy69zUY")

finding_dory = media.Movie("Finding Dory",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/3/3e/Finding_Dory.jpg/220px-Finding_Dory.jpg",
                           "https://www.youtube.com/watch?v=JhvrQeY3doI")

the_avengers = media.Movie("The Avengers",
                           "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
                           "https://www.youtube.com/watch?v=eOrNdBpGMv8")

war_room = media.Movie("War Room",
                       "https://upload.wikimedia.org/wikipedia/en/thumb/a/a7/WarRoomMoviePoster.jpg/220px-WarRoomMoviePoster.jpg",
                       "https://www.youtube.com/watch?v=2DbRwcrhiLA")

kung_fu_panda = media.Movie("Kung Fu Panda",
                            "https://upload.wikimedia.org/wikipedia/en/thumb/7/76/Kungfupanda.jpg/220px-Kungfupanda.jpg",
                            "https://www.youtube.com/watch?v=NRc-ze7Wrxw")

the_lego_movie = media.Movie("The LEGO Movie",
                             "https://upload.wikimedia.org/wikipedia/en/1/10/The_Lego_Movie_poster.jpg",
                             "https://www.youtube.com/watch?v=fZ_JOBCLF-I")

# List of movies
movie_list = [the_croods, finding_dory, the_avengers, war_room, kung_fu_panda, the_lego_movie]

fresh_tomatoes.open_movies_page(movie_list)
