# Table Builder

This project is designed to provide a dynamic table management API. It allows users to create tables with dynamic columns and manage rows within those tables.

## Getting Started

To run this project locally, you'll need to have Docker and Docker Compose installed on your system.

### Prerequisites

- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/)

### Running the Project

Follow these steps to run the project using Docker Compose:

1. Clone the repository:

   ```bash
   git clone git@github.com:asucic/table-builder.git
   ```

2. Navigate to the project directory:

   ```bash
   cd table-builder
   ```

3. Start the Docker Compose environment:

   ```bash
   docker compose up -d
   ```

4. Apply database migrations:

   ```bash
   docker compose exec web python manage.py migrate
   ```

5. Create a superuser (optional):

   ```bash
   docker compose exec web python manage.py createsuperuser
   ```

6. The project should now be running. You can access the API at http://localhost:8000.

7. You can authenticate yourself with superuser created earlier on http://localhost:8000/admin.

### Running Tests

To run the tests for this project, use the following command:

   ```bash
   docker compose exec web python manage.py test api_tables.tests
   ```


