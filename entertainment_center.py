import fresh_tomatoes
import media

# Creating instances with Movie & TV Data.


toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "150 mins",
    "Animation, Adventure, Comedy",
    "G",
    "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
    "https://www.youtube.com/watch?v=vwyZH85NQC4")


avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "200 mins",
    "Science Fiction, Action, Adventure, Fantasy",
    "PG-13",
    "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")


heat = media.Movie(
    "Heat 1995",
    "A Los Angeles crime saga",
    "180 mins",
    "Crime, Thriller, Action",
    "R",
    "https://upload.wikimedia.org/wikipedia/en/6/6c/Heatposter.jpg",
    "https://www.youtube.com/watch?v=2GfZl4kuVNI")


miami_vice = media.TvShow(
    "Miami Vice",
    "Cops, Drugs & Miami",
    "60 mins",
    "Crime, Action, Adventure",
    "R",
    "https://upload.wikimedia.org/wikipedia/en/thumb/2/25/Miami_Vice_Season_2_Logo_sm.jpg/250px-Miami_Vice_Season_2_Logo_sm.jpg",
    "https://www.youtube.com/watch?v=b6OymLS64Jo")


knight_rider = media.TvShow(
    "Knight Rider",
    "A lone crime fighter",
    "60 mins",
    "R",
    "Action, Crime",
    "https://upload.wikimedia.org/wikipedia/en/thumb/3/31/Knightlogo.png/250px-Knightlogo.png",
    "https://www.youtube.com/watch?v=oNyXYPhnUIs")


street_hawk = media.TvShow(
    "Street Hawk",
    "A desk bound cop secretly fights crime",
    "60 mins",
    "Superhero, Adventure, Action",
    "R",
    "https://m.media-amazon.com/images/M/MV5BMTU2MzQ1MDEzMF5BMl5BanBnXkFtZTcwMzUyMTkxMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg",
    "https://www.youtube.com/watch?v=sP_zFKkJgvY")


trailer = [heat, street_hawk, knight_rider, miami_vice, toy_story, avatar]
fresh_tomatoes.open_movies_page(trailer)
