Flask Blog Application with User Authentication and Authorization
=================================================================

This project is a Flask web application that features user registration, login authentication, blog post creation, editing, deletion, and commenting. It also includes an admin-only section for managing posts and comments.

Features
--------

-   User Registration and Login: Users can register with a name, email, and password. Passwords are securely hashed.
-   User Authentication: Users can log in and out, and session management is handled by Flask-Login.
-   Blog Posts: Logged-in users can create, edit, and delete blog posts.
-   Comments: Logged-in users can comment on posts.
-   Admin Panel: Certain actions (creating, editing, and deleting posts) are restricted to admin users only.
-   Gravatar Integration: User avatars are displayed using Gravatar.
-   CKEditor: A rich text editor is used for creating and editing blog posts.

Technologies Used
-----------------

-   Flask: Web framework for Python.
-   Flask-Bootstrap: Integrates Bootstrap for responsive design.
-   Flask-CKEditor: Integrates CKEditor for rich text editing.
-   Flask-Gravatar: Integrates Gravatar for user avatars.
-   Flask-Login: Manages user sessions and authentication.
-   Flask-SQLAlchemy: SQL toolkit and Object-Relational Mapping (ORM) system.
-   Werkzeug: Provides utilities for password hashing.
-   SQLite: Database engine for storing user and post data.

Code Explanation
----------------

### Flask Application Setup

The application is created and configured with a secret key and database URI. Flask-Login is initialized for session management, and Flask-Bootstrap, CKEditor, and Gravatar are configured.

### Database Models

-   User: Stores user information, including name, email, and hashed password.
-   BlogPost: Stores blog post information, including title, subtitle, date, body, and author.
-   Comment: Stores comments on blog posts, including text, author, and associated post.

### Routes

-   Home Route: Displays all blog posts.
-   Register Route: Handles user registration.
-   Login Route: Handles user login.
-   Logout Route: Logs the user out.
-   Create Post Route: Allows admin users to create new posts.
-   Edit Post Route: Allows admin users to edit existing posts.
-   Delete Post Route: Allows admin users to delete posts.
-   Post Detail Route: Displays a single blog post and its comments, and allows logged-in users to comment.
-   About and Contact Routes: Display the about and contact pages.

### Admin-Only Decorator

A decorator is used to restrict certain routes to admin users only.

### Password Hashing

Passwords are hashed using Werkzeug's `generate_password_hash` method with PBKDF2 and SHA256.

### Session Management

Flask-Login manages user sessions, ensuring that users stay logged in across different pages. The `login_required` decorator protects routes that require authentication.

Security
--------

-   Secret Key: Ensure that the `SECRET_KEY` is securely stored in an environment variable and not hard-coded.
-   Password Hashing: Passwords are securely hashed and stored in the database.

<hr>

![day 69 1](https://github.com/AnilNAKR/My-Python-ProjectsRepo/assets/16172853/1e46b59d-79f5-4b65-8e9b-756087fcae71)

<hr>

https://github.com/AnilNAKR/My-Python-ProjectsRepo/assets/16172853/7916b00b-79fc-4cf8-93ef-8ecc98b4bfd1



