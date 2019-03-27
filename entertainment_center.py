import fresh_tomatoes
import media

# Creating instances with Movie & TV Data.


toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "150 mins",
    "Animation, Adventure, Comedy",
    "G",
    "https://bit.ly/1OHWo0L",
    "https://www.youtube.com/watch?v=vwyZH85NQC4")


avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "200 mins",
    "Science Fiction, Action, Adventure, Fantasy",
    "PG-13",
    "https://bit.ly/1oUhcTQ",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")


heat = media.Movie(
    "Heat 1995",
    "A Los Angeles crime saga",
    "180 mins",
    "Crime, Thriller, Action",
    "R",
    "https://bit.ly/2V020JM",
    "https://www.youtube.com/watch?v=2GfZl4kuVNI")


miami_vice = media.TvShow(
    "Miami Vice",
    "Cops, Drugs & Miami",
    "60 mins",
    "Crime, Action, Adventure",
    "R",
    "https://bit.ly/2FE188w",
    "https://www.youtube.com/watch?v=b6OymLS64Jo")


knight_rider = media.TvShow(
    "Knight Rider",
    "A lone crime fighter",
    "60 mins",
    "R",
    "Action, Crime",
    "https://bit.ly/2FF6OPS",
    "https://www.youtube.com/watch?v=oNyXYPhnUIs")


street_hawk = media.TvShow(
    "Street Hawk",
    "A desk bound cop secretly fights crime",
    "60 mins",
    "Superhero, Adventure, Action",
    "R",
    "https://bit.ly/2uvXDuI",
    "https://www.youtube.com/watch?v=sP_zFKkJgvY")


trailer = [heat, street_hawk, knight_rider, miami_vice, toy_story, avatar]
fresh_tomatoes.open_movies_page(trailer)
