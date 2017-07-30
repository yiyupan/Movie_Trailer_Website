import media
import fresh_tomatoes


interstellar = media.Movie("Interstellar",
                           "Explorers travel to ensure humanity's survival.",
                           "https://zayzay.com/wp-content/uploads/" +
                           "2014/10/INTERSTELLAR-POSTER.jpg",
                           "https://www.youtube.com/watch?v=0vxOhd4qlnA")

spirited_away = media.Movie("Spirited Away",
                            "A girl wanders into a world where humans " +
                            "are changed into beasts.",
                            "https://ashleycapes.files.wordpress.com/" +
                            "2013/01/spirited-away.jpg",
                            "https://www.youtube.com/watch?v=ByXuk9QqQkk")

like_stars_on_earth = media.Movie("Like Stars on Earth",
                                  "A boy is thought to be a lazy " +
                                  "trouble-maker",
                                  "https://image.tmdb.org/t/p/" +
                                  "w1280/t8aFYKTn6hfMvX7UDL8d2xYhT9S.jpg",
                                  "https://www.youtube.com/" +
                                  "watch?v=DBg6HSMF9X8")

movies = [interstellar, spirited_away, like_stars_on_earth]
fresh_tomatoes.open_movies_page(movies)
