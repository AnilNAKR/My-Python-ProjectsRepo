# Flask Application Intro with Decorators

### 1\. `hello_world` Function:

-   Route: `/`
-   Description: Renders the `index.html` template, which serves as the home page of the application.
-   Usage: Accessing the root URL of the application (`/`) will display the content of the `index.html` template.

### 2\. `bye` Function:

-   Route: `/bye`
-   Description: Decorated with `make_bold`, `make_emphasis`, and `make_underline` decorators to format the output message.
-   Usage: Accessing the `/bye` URL will display the message "Bye!" in bold, emphasis, and underline format.

### 3\. `greet` Function:

-   Route: `/username/<name>`
-   Description: Greets the user with the provided name, capitalized using the `title()` method.
-   Usage: Accessing the `/username/<name>` URL will display a greeting message with the provided name.

### 4\. `talk` Function:

-   Route: `/talk/<name>/<int:number>`
-   Description: Displays a message with the provided name and rank, both capitalized using the `title()` method.
-   Usage: Accessing the `/talk/<name>/<int:number>` URL will display a message with the provided name and rank.

### 5\. `create_blog_post` Function:

-   Description: Demonstrates a decorator (`is_authenticated_decorator`) to restrict access to the `create_blog_post` function based on user authentication status.
-   Usage: Not directly accessible via a URL. Requires authentication to create a new blog post.

### 6\. `User` Class:

-   Description: Defines a simple `User` class with attributes `name` and `is_logged_in` to simulate user authentication.

### 7\. `is_authenticated_decorator` Function:

-   Description: Decorator function that checks if a user is logged in before allowing access to the decorated function.
-   Usage: Applied to the `create_blog_post` function to restrict access based on authentication status.


https://github.com/AnilNAKR/My-Python-ProjectsRepo/assets/16172853/523ca13d-ecd1-42c8-b6fc-a440903b62e9

