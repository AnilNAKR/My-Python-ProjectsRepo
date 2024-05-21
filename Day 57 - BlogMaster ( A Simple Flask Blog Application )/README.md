# BlogMaster - A Simple Flask Blog Application

Project Description
-------------------

BlogMaster is a simple blog application built using Flask, a Python web framework. The application fetches blog post data from an external API and displays it on a clean, responsive web interface. Users can view a list of blog posts on the homepage and read individual posts by clicking on them.

## Features

-   Home Page: Displays a list of blog posts with their titles and subtitles.
-   Post Page: Allows users to read individual blog posts in detail by clicking on a post from the home page.

## Technologies Used

-   Flask: A lightweight WSGI web application framework for Python.
-   Jinja: A templating engine for Python used with Flask.
-   Requests: A Python library for making HTTP requests to external APIs.
-   HTML5 and CSS3: For structuring and styling the web pages.

## APIs Utilized

-   Npoint.io: For fetching blog post data.

## Usage
1. Run `py main.py`
2. Open your web browser and go to `http://127.0.0.1:5000/` to view the website.

## Application Routes

-   Home (`/`):
    -   Displays a list of all blog posts with their titles and subtitles.
-   Post (`/post/<int:index>`):
    -   Displays the full content of a single blog post based on its ID.

## Files and Directories

-   app.py: The main Flask application file that defines the routes and handles API requests.
-   post.py: Contains the `Post` class used to create post objects.
-   templates/: Directory containing the HTML templates (`index.html`, `post.html`) used by Flask.
-   static/: Contains static assets like CSS, JavaScript, and images used in the website.

<hr>

![day 57 blog](https://github.com/AnilNAKR/My-Python-ProjectsRepo/assets/16172853/30a2caad-39f3-43b8-a26c-611dea780285)

![day 57 blog post](https://github.com/AnilNAKR/My-Python-ProjectsRepo/assets/16172853/893968d9-ee15-4b0b-8099-3a3b669a1ea5)

<hr>

https://github.com/AnilNAKR/My-Python-ProjectsRepo/assets/16172853/529bbc0e-2c2f-4378-9872-c9a56d6b74eb



