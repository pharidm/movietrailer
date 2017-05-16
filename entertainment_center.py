from media import Movie
import fresh_tomatoes

# Instance of the Class Movie - a class as the blue print and instance
# as physical structure with attributes

toy_story = Movie("Toy Story","A story of a boy and his  toy that comes to life",
                  "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                  "https://www.youtube.com/watch?v=c3986gGp3Qs")
#print(toy_story.storyline) Prints Story line

avatar = Movie('Avatar', 'A soldier is marine on an alien planet', 'https://resizing.flixster.com/'
                                                                   'RekPVUC5CH4Vgulb0UaiXgYDbdM='
                                                                   '/206x305/v1.bTsxMTE3Njc5MjtqOzE3MzY0OzEyMDA7ODAwOzEyMDA','https://youtu.be/cRdxXPV9GNQ')
# print(avatar.storyline)
#Example of show trailer
# avatar.show_trailer()

enders_game = Movie("Enders Game", "A story of a boy Soldier coming of age", "https://upload.wikimedia."
                                                                             "org/wikipedia/en/8/8c/Ender%27s_"
                                                                             "Game_poster.jpg", "https://youtu.be/2UNWLgY-wuo")
# print(enders_game.storyline)
# enders_game.show_trailer()

star_wars = Movie("Star Wars: The Last Jedi ","The saga continues as we discover what really happened to Luke Skywalker",
                  "https://upload.wikimedia.org/wikipedia/en/7/7f/Star_Wars_The_Last_Jedi.jpg",
                  "https://www.youtube.com/watch?v=zB4I68XVPzQ")
# print(toy_story.storyline)

ferris_bueller= Movie('Ferris Bueller', '1986 American teen comedy', "https://upload.wikimedia.org/wikipedia/en/9/9b/Ferris_Bueller%27s_Day_Off.jpg", "https://www.youtube.com/watch?v=0KFVLWX7eEY")
# print(avatar.storyline)
# avatar.show_trailer()

explorers = Movie("Explorers", "A story of a boy Soldier coming of age", "https://upload.wikimedia.org/wikipedia/en/2/26/Explorersposter1985.jpg",
                                                                             "https://www.youtube.com/watch?v=3X3VxBJzH68")
movies = [toy_story, avatar, enders_game, star_wars, ferris_bueller, explorers]
fresh_tomatoes.open_movies_page(movies)

# Example code for showing movie ratings, storyline and trailer
# print(Movie.VALID_RATINGS)
# print(enders_game.storyline)
# enders_game.show_trailer()"
