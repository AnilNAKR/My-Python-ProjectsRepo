# URL Building and Templating with Jinja in Flask

This project demonstrates a Flask application that utilizes URL building and Jinja templating. The application fetches and displays data from various APIs based on user input and routes.

## Features

1.  **Home Page:** Displays a random number and the current year.
2.  **Guess Page:** Accepts a name as a URL parameter and fetches data such as age, country, and gender for the given name using external APIs.
3.  **Blog Page**: Fetches and displays a list of blog posts from an external API.

### Technologies Used

-   **Flask:** A lightweight WSGI web application framework for Python.
-   **Jinja**: A templating engine for Python used with Flask.
-   **Requests:** A Python library for making HTTP requests to external APIs.
-   **HTML5 and CSS3**: For structuring and styling the web pages.

### APIs Utilized

-   **Agify.io:** For predicting the age based on a given name.
-   **Nationalize.io:** For predicting the country of origin based on a given name.
-   **Genderize.io:** For predicting the gender based on a given name.
-   **First.org Countries:** For retrieving country names based on country codes.
-   **Npoint.io:** For fetching blog posts data.

## Usage
1. Run `py server.py`
2. Open your web browser and go to `http://127.0.0.1:5000/` to view the website.

### Application Routes

-   Home (`/`):
    -   Displays a random number between 1 and 10.
    -   Shows the current year.
-   Guess (`/guess/<name>`):
    -   Accepts a name as a URL parameter.
    -   Fetches and displays the predicted age, gender, and country of the given name.
-   Blog (`/blog`):
    -   Fetches and displays blog posts from an external API.
<hr>

![day 57](https://github.com/AnilNAKR/My-Python-ProjectsRepo/assets/16172853/8e25c010-969c-4b95-ba31-f1e8bd23d252)
![day 57 1](https://github.com/AnilNAKR/My-Python-ProjectsRepo/assets/16172853/ca51ed72-01e7-45f0-800c-c5dccdaaac3d)

<hr>

https://github.com/AnilNAKR/My-Python-ProjectsRepo/assets/16172853/22d46fd5-31c3-4bdf-bf84-d6ec66fdf689

