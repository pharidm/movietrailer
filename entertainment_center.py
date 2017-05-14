from media import Movie
import fresh_tomatoes

# Instance of the Class Movie - thing of a class as the blue print and instance
# as physical structure with attributes
toy_story = Movie("Toy Story","A story of a boy and his  toy that comes to life",
                  "https://lumiere-a.akamaihd.net/v1/images/open-uri20160811-32147-1ut41la_"
                  "40c7984a.jpeg?region=0%2C0%2C1536%2C480",
                  "https://www.youtube.com/watch?v=c3986gGp3Qs")
print(toy_story.storyline)

avatar = Movie('Avatar', 'A soldier is marine on an alien planet', 'https://resizing.flixster.com/'
                                                                   'RekPVUC5CH4Vgulb0UaiXgYDbdM='
                                                                   '/206x305/v1.bTsxMTE3Njc5MjtqOzE3MzY0OzEyMDA7ODAwOzEyMDA','https://youtu.be/cRdxXPV9GNQ')
# print(avatar.storyline)
# avatar.show_trailer()

enders_game = Movie("Enders Game", "A story of a boy Soldier coming of age", "https://upload.wikimedia."
                                                                             "org/wikipedia/en/8/8c/Ender%27s_"
                                                                             "Game_poster.jpg", "https://youtu.be/2UNWLgY-wuo")
# print(enders_game.storyline)
# enders_game.show_trailer()
toy_story_2 = Movie("Toy Story2","A story of a boy and his  toy that comes to life",
                  "https://lumiere-a.akamaihd.net/v1/images/open-uri20160811-32147-1ut41la_"
                  "40c7984a.jpeg?region=0%2C0%2C1536%2C480",
                  "https://www.youtube.com/watch?v=c3986gGp3Qs")
# print(toy_story.storyline)

avatar_2 = Movie('Avatar2', 'A soldier is marine on an alien planet', 'https://resizing.flixster.com/'
                                                                   'RekPVUC5CH4Vgulb0UaiXgYDbdM='
                                                                   '/206x305/v1.bTsxMTE3Njc5MjtqOzE3MzY0OzEyMDA7ODAwOzEyMDA','https://youtu.be/cRdxXPV9GNQ')
# print(avatar.storyline)
# avatar.show_trailer()

enders_game_2 = Movie("Enders Game2", "A story of a boy Soldier coming of age", "https://upload.wikimedia."
                                                                             "org/wikipedia/en/8/8c/Ender%27s_"
                                                                     "Game_poster.jpg", "https://youtu.be/2UNWLgY-wuo")
movies = [toy_story, avatar, enders_game, toy_story_2, avatar_2, enders_game_2]
fresh_tomatoes.open_movies_page(movies)

# print(Movie.VALID_RATINGS)
# print(enders_game.storyline)
# enders_game.show_trailer()""
