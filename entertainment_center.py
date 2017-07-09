import media
import fresh_tomatoes


# Movie variables
storyline = '''Janardhan Jakhar chases his dreams of becoming a big Rock star, during which he falls in love with Heer.'''
image_link = "http://st1.bollywoodlife.com/wp-content/uploads/2011/10/rockstar-musicreview051011.jpg"
trailer_link = "https://www.youtube.com/watch?v=bD5FShPZdpw"

# Movie's object
rock_star = media.Movie("Rockstar", storyline, image_link, trailer_link)


# Movie variables
storyline = '''A daku turned gold medal athelete wanders for life as he is haunted by police officials.'''
image_link = "http://www.travelindia-guide.com/bollywood-movies/moviesbanner/paan-singh-tomar.jpg"
trailer_link = "https://www.youtube.com/watch?v=TT--NbNqiHE"

# Movie's object
singh_tomar = media.Movie("Paan Singh Tomar", storyline, image_link, trailer_link)
                          

# Movie variables
storyline = '''A short-term memory loss patient sets out on his journey to avenge the death of his lover.'''
image_link = "https://upload.wikimedia.org/wikipedia/en/9/97/Ghajini_Hindi.jpg"
trailer_link = "https://www.youtube.com/watch?v=j_DshRUOm-o"

# Movie's object
gazini = media.Movie("Gazini", storyline, image_link, trailer_link)                     

 

# Movie's array
movies = [rock_star, singh_tomar, gazini]

# Web interface
fresh_tomatoes.open_movies_page(movies)
