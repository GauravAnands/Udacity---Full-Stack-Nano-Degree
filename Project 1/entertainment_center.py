import media
import fresh_tomatoes


# Movie variables
storyline = '''Janardhan Jakhar chases his dreams of becoming a big Rock star, during which
                he falls in love with Heer.'''
image_link = """https://upload.wikimedia.org/wikipedia/en/6/68/
Rockstar-Movie-Poster.jpg"""
trailer_link = "https://www.youtube.com/watch?v=bD5FShPZdpw"

# Movie's object
rock_star = media.Movie("Rockstar", storyline, image_link, trailer_link)


# Movie variables
storyline = '''A daku turned gold medal athelete wanders for life as he is haunted
             by police officials.'''
image_link = """https://upload.wikimedia.org/wikipedia/en/9/93/
Paan_Singh_Tomar_Poster.jpg"""
trailer_link = "https://www.youtube.com/watch?v=TT--NbNqiHE"

# Movie's object
tomar = media.Movie("Paan Singh Tomar", storyline, image_link, trailer_link)


# Movie variables
storyline = '''A short-term memory loss patient sets out on his journey to
             avenge the death of his lover.'''
image_link = "https://upload.wikimedia.org/wikipedia/en/9/97/Ghajini_Hindi.jpg"
trailer_link = "https://www.youtube.com/watch?v=j_DshRUOm-o"

# Movie's object
gazini = media.Movie("Gazini", storyline, image_link, trailer_link)


# Movie's array
movies = [rock_star, tomar, gazini]

# Web interface
fresh_tomatoes.open_movies_page(movies)
