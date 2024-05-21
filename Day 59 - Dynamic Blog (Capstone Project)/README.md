# BlogMaster - A Comprehensive Flask Blog Application

Project Description
-------------------

BlogMaster is a comprehensive blog application built using Flask, a Python web framework. The application fetches blog post data from an external API and displays it on a well-designed, responsive web interface. Users can browse through a list of blog posts on the homepage, read individual posts, and access additional pages such as About and Contact.

### Features

-   Home Page: Displays a list of blog posts with their titles, subtitles, and images.
-   Post Page: Allows users to read individual blog posts in detail by clicking on a post from the home page.
-   About Page: Provides information about the blog or author.
-   Contact Page: Provides contact information or a form for users to get in touch.

### Technologies Used

-   Flask: A lightweight WSGI web application framework for Python.
-   Jinja: A templating engine for Python used with Flask.
-   Requests: A Python library for making HTTP requests to external APIs.
-   HTML5 and CSS3: For structuring and styling the web pages.

### APIs Utilized

-   Npoint.io: For fetching blog post data.

## Usage
1. Run `py main.py`
2. Open your web browser and go to `http://127.0.0.1:5000/` to view the website.

### Application Routes

-   Home (`/`):
    -   Displays a list of all blog posts with their titles, subtitles, and images.
-   About (`/about`):
    -   Displays the About page.
-   Contact (`/contact`):
    -   Displays the Contact page.
-   Post (`/post/<int:index>`):
    -   Displays the full content of a single blog post based on its ID.
 

### Files and Directories

-   app.py: The main Flask application file that defines the routes and handles API requests.
-   posts.py: Contains the `Posts` class used to create post objects.
-   templates/: Directory containing the HTML templates (`index.html`, `post.html`, `about.html`, `contact.html`) used by Flask.
-   static/: Contains static assets like CSS, JavaScript, and images used in the website.


<hr>

![day 59 1](https://github.com/AnilNAKR/My-Python-ProjectsRepo/assets/16172853/f577af2a-292c-4fad-ae23-3d4b83e3a0e8)

![day 59 2](https://github.com/AnilNAKR/My-Python-ProjectsRepo/assets/16172853/95f940c3-4f18-4549-8714-c62db358aed6)

![day 59 3](https://github.com/AnilNAKR/My-Python-ProjectsRepo/assets/16172853/7cb633ba-4201-4959-b202-462a527f87e8)

<hr>

https://github.com/AnilNAKR/My-Python-ProjectsRepo/assets/16172853/eb8392b7-0a24-4814-b109-b6eb03605362



