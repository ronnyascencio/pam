# Phtography Asset Management (PAM) Platform

This project aims to build a generic Photography Asset Management (PAM) platform for photographers and potentially other content creators. It will allow users to store, organize, search, and manage their digital assets efficiently.

## Technology Stack

* **Backend:** FastAPI (Python web framework), Uvicorn (ASGI server)
* **Database:** PostgreSQL
* **ORM:** SQLModel (based on SQLAlchemy and Pydantic)
* **Frontend:** Jinja2 (templating engine), HTML, CSS, JavaScript
* **Dependency Management & Environment:** uv (fast pip and venv replacement)
* **Containerization:** Docker

## Getting Started

Follow these steps to get the project up and running locally.

### Prerequisites

* Python 3.13 installed
* uv installed (`pip install uv`)
* Docker installed
* PostgreSQL installed and running

### Installation

1.  **Clone the repository (if you have one):**
    ```bash
    git clone https://github.com/ronnyascencio/pam.git
    cd pam
    ```

2.  **Create and activate the virtual environment using uv:**
    ```bash
    uv venv
    source .venv/bin/activate  # On Linux/macOS
    .venv\Scripts\activate  # On Windows
    ```

3.  **Install the project dependencies:**
    ```bash
    uv pip install -r pyproject.toml
    ```

4.  **Set up the database:**
    * Ensure PostgreSQL is running.
    * Create a database for the project (you can do this using a PostgreSQL client like `psql` or pgAdmin).
    * Update the database connection details in `app/database.py` to match your PostgreSQL setup.

5.  **Run database migrations (if you implement Alembic later):**
    ```bash
    # If using Alembic:
    alembic upgrade head
    ```
    (For the initial MVP, you might start by letting SQLModel create the tables on the first run, but for production, migrations are recommended.)

6.  **Run the FastAPI application locally (for development):**
    ```bash
    uv run uvicorn app.main:app --reload
    ```
    ```bash
    uv run fastapi dev main.py
    ```

    This will start the development server, and you can access the application in your browser (usually at `http://127.0.0.1:8000`).

## MVP Features

The Minimum Viable Product (MVP) includes the following core functionalities:

* **User Authentication:** Registration and login for users to secure their assets.
* **Asset Upload:** Users can upload image files.
* **Asset Viewing:** Display individual images and their associated metadata.
* **Asset Listing:** A gallery view to browse uploaded images with basic filtering.
* **Metadata Management:** Ability to add and edit descriptive information (title, description, tags) for assets.
* **Collection Management:** Users can create and manage collections (albums) to organize assets.
* **Adding to Collections:** Ability to add existing assets to collections.
* **Asset Deletion:** Users can delete their uploaded assets.

## Contributing

We welcome contributions to the Generic DAM Platform! If you have ideas for improvements, bug fixes, or new features, please follow these steps:

1.  **Fork the repository** on GitHub.
2.  **Create a new branch** for your contribution: `git checkout -b feature/your-feature-name` or `git checkout -b bugfix/your-bugfix-name`.
3.  **Make your changes** and ensure your code adheres to any established style guidelines (e.g., using a linter like Flake8 or Ruff).
4.  **Write tests** for any new functionality or bug fixes.
5.  **Ensure all tests pass:** `pytest` (or your preferred testing framework).
6.  **Commit your changes:** `git commit -m "Add your descriptive commit message"`.
7.  **Push your changes to your fork:** `git push origin feature/your-feature-name`.
8.  **Submit a Pull Request** to the main repository on GitHub, clearly describing your changes and why they should be merged.

We appreciate your contributions to making this platform better!

## License

This project is licensed under the **Apache License**. See the `LICENSE` file in the root of the repository for more information.


