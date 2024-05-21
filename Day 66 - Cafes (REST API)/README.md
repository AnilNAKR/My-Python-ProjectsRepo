Cafe RESTful API Application
====================

Overview
--------

This is a Flask-based web application that manages a collection of cafes. The application provides an interface to add, retrieve, update, and delete cafes from a SQLite database. The application also provides a RESTful API to interact with the database using Postman, an API Platform.

Features
--------

-   Home Page: A simple landing page for the application.
-   API Endpoints:
    -   `GET /random`: Get a random cafe from the database.
    -   `GET /all`: Get a list of all cafes.
    -   `GET /search?loc=<location>`: Search for cafes at a specific location.

### Following Endpoints are used with Postman
    -   `POST /add`: Add a new cafe using data from a form.
    -   `PATCH/PUT /update_price/<int:cafe_id>`: Update the price of coffee for a specific cafe.
    -   `DELETE /report-closed/<int:cafe_id>`: Delete a cafe from the database.

## Program Usage
1. Run `py main.py`
2. Open your web browser and go to `http://127.0.0.1:5000/` to view the website.

<hr>

![day 66 0](https://github.com/AnilNAKR/My-Python-ProjectsRepo/assets/16172853/1863fac4-7e38-4c69-a473-10e3bf20ff8f)
![day 66 2](https://github.com/AnilNAKR/My-Python-ProjectsRepo/assets/16172853/3fafe91c-546d-422f-bfd9-e85929cc6b70)
![day 66 1](https://github.com/AnilNAKR/My-Python-ProjectsRepo/assets/16172853/662b4bb9-547e-4895-8be8-6378dadc08be)

![day 66](https://github.com/AnilNAKR/My-Python-ProjectsRepo/assets/16172853/8efdff2a-e9b2-4a94-8867-c0535cb70a88)
![day 66 (2)](https://github.com/AnilNAKR/My-Python-ProjectsRepo/assets/16172853/d7254ba9-6341-4b9e-9564-38b6297d8486)
![day 66 (3)](https://github.com/AnilNAKR/My-Python-ProjectsRepo/assets/16172853/56ee09d3-cac4-4934-a30f-f488fd016f71)

