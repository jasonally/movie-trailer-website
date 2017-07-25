# Project: Movie Trailer Website

### About
This project uses a backend script to create a website with information about my favorite movies as well as the ability to watch their trailers from YouTube. The course material for this project comes from Udacity's [Programming Foundations with Python](https://www.udacity.com/course/programming-foundations-with-python--ud036) course.

### Directory contents
This directory has three Python files as well as this `README.md` file:
* **entertainment_center.py** - Generates the movie list and calls the method in `fresh_tomatoes.py` to display the website.
* **fresh_tomatoes.py** - Takes in a list of movies, builds the relevant `HTML` and opens your default browser to display the generated website.
* **media.py** - Contains the classes used to hold movie data.

After `entertainment_center.py` is run for the first time, it will generate an `HTML` file, `fresh_tomatoes.html`, which contains the movie trailer website.

### How to run
1. If your computer doesn't already have Python installed, install [it](https://www.python.org).
2. Download the directory and, if the directory is in a compressed file, extract it.
3. Open Terminal and navigate to the directory.
4. Run `entertainment_center.py` by typing `python entertainment_center.py`.
5. The movie trailer website will load in a new tab in your web browser.
6. Each movie will display its movie poster, year, duration, and storyline.
7. Click on a movie to view its trailer on YouTube.

You can also view view a web version of my movie trailer website [here](https://jasonally.github.io/movie-trailer-website/).

### How to update the list of movies
1. Open `entertainment_center.py` in a text editor.
2. Each movie's data is stored as an instance of a class, Movie. Each instance requires the movie's title, duration in minutes, storyline, URL to a movie poster, year of release, and a URL to the movie's YouTube trailer. For instance:
```
star_wars = media.Movie("Star Wars: The Force Awakens",
                        "136",
                        "New and old characters alike team up as a threat to the galaxy emerges.",
                        "https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg",
                        "2015",
                        "https://www.youtube.com/watch?v=ngElkyQ6Rhs&t=4s")
```
3. Add a new instance to the file with the movie's relevant data.
4. Update the `movies` list at the bottom of the file with the names of your new movie instance(s).

### Opportunities for improvement
The Movies class in `media.py` inherits from a parent class, Video, which contains instance variables that can be used for movies and for TV shows: title, duration, storyline, and poster URL. Someone could use the Video class to create a new child class, TVShows, which could be used to generate data about someone's favorite TV shows for the website.
