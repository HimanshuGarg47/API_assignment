# Client Artist Work API EndPoints

It allows users to view, search, and filter works of art, as well as register for an account.

## Installation

1. Clone the repository to your local machine.
2. Create a virtual environment and activate it.
3. Install the required packages using `pip install -r requirements.txt`.
4. Set up the database by running `python manage.py migrate`.

## Usage

### API Endpoints

The following API endpoints are available:

- `/api/works`: Returns a list of all works of art.
- `/api/works?artist=[Artist Name]`: Returns a list of works of art by the specified artist.
- `/api/works?work_type=[Work Type]`: Returns a list of works of the specified type (e.g. "painting", "sculpture").
- `/api/register`: Allows users to register for an account. The payload should include a `username` and `password`.

### Creating a Superuser

To access the Django admin panel, you'll need to create a superuser account. You can do this by running `python manage.py createsuperuser` and following the prompts.

### Running the Server

To run the server, use the command `python manage.py runserver`. The server will be accessible at `http://localhost:8000/`.

### Working Output

Client Api endpoint (http://127.0.0.1:8000/api/client)

![This is an image](home/static/images/Screenshot%20(159).png))

![This is an image](home/static/images/Screenshot%20(156).png)

Work List (http://127.0.0.1:8000/api/works)

![This is an image](home/static/images/Screenshot%20(157).png)

Artist List API (http://127.0.0.1:8000/api/register)

![This is an image](home/static/images/Screenshot%20(158).png)

Registration API Endpoint Post only (http://127.0.0.1:8000/api/register)

![This is an image](home/static/images/Screenshot%20(160).png)

Client API Endpoint (http://127.0.0.1:8000/api/client)

![This is an image](home/static/images/Screenshot%20(162).png)

Admin Interface (http://127.0.0.1:8000/admin)

![This is an image](home/static/images/Screenshot%20(163).png)



## Contributing

This project is open to contributions! If you find a bug or want to add a new feature, please create a new issue or pull request.
