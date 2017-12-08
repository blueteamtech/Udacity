import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                         "A story of a boy and his toys that come to life",
                         "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                         "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)
#avatar.show_trailer()
spectre = media.Movie("Spectre",
                      "Bond agains global surveillance",
                      "https://upload.wikimedia.org/wikipedia/en/c/c3/Spectre_poster.jpg",
                      "https://www.youtube.com/watch?v=ashLaclKCik")
#spectre.show_trailer()
La_La_Land = media.Movie(
    "La La Land",
    "An actor and musician fall in love while pursuing their dreams",
    "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png",
    "https://www.youtube.com/watch?v=0pdqf4P9MB8")

Arrival = media.Movie(
    "Arrival",
    "Alien encounter brings global mystery",
    "https://upload.wikimedia.org/wikipedia/en/d/df/Arrival%2C_Movie_Poster.jpg",
    "https://www.youtube.com/watch?v=tFMo3UJ4B4g")

Logan = media.Movie(
    "Logan",
    "Logan is on a mission to bring mutants to safety",
    "https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg",
    "https://www.youtube.com/watch?v=Div0iP65aZo")

Ex_Machina = media.Movie(
    "Ex Machina",
    "Uncovering the birth of AI",
    "https://upload.wikimedia.org/wikipedia/en/b/ba/Ex-machina-uk-poster.jpg",
    "https://www.youtube.com/watch?v=bggUmgeMCdc")

movies = [toy_story, avatar, La_La_Land, Arrival, Logan, Ex_Machina]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
    

