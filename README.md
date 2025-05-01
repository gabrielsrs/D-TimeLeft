# dateEnd

An API to store final dates and return various parameters related to these dates.

## Features

- Create, update, retrieve, and delete date objects.
- Calculate time differences and provide detailed time unit breakdowns.
- Validate and handle timezones using `tzdata`.
- RESTful API built with Flask-RESTx.
- MongoDB integration for data persistence.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/gabrielsrs/dateEnd.git
   cd dateEnd
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables: Create a .env file in the root directory and add the following:

    ```
    MONGO_CONNECTION=<your_mongo_connection_string>
    ```

4. Run the application:

    ```bash
    python app.py
    ```

## Usage
- The API provides the following endpoints:

    - `POST /date`: Create a new date.
    - `GET /date/<date_id>`: Retrieve a date by ID.
    - `PATCH /date/<date_id>`: Update an existing date.
    - `DELETE /date/<date_id>`: Delete a date.
    - `GET /timezones`: Retrieve all available timezones.
- Use tools like Postman or cURL to interact with the API.

## Running Tests
  To run the test suite, execute the following command:

```bash
pytest
```

## Contributing
Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-name
    ```
3. Commit your changes:
    ```bash
    git commit -m "Add feature-name"
    ```
4. Push to the branch:
    ```bash
    git push origin feature-name
    ```
5. Open a pull request.

## License
This project is licensed under the [MIT License](https://github.com/gabrielsrs/D-TimeLeft?tab=MIT-1-ov-file#readme). See the LICENSE file for details.
