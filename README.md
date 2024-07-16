# Quiz App

A Django-based quiz application with a RESTful API for managing quizzes, questions, and answers.

## Features

- Create and manage quizzes
- Add and manage questions for each quiz
- Provide multiple answers for each question
- RESTful API for all operations

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/quiz-app.git
   ```

2. Navigate to the project directory:
   ```bash
   cd quiz-app
   ```

3. Install the dependencies:
   ```bash
   pipenv install
   ```

4. Activate the virtual environment
   ```bash
   pipenv shell
   ```

5. Run the migrations:
   ```bash
   python manage.py migrate
   ```
7. Create superuser to access the admin interface:
   ```bash
   python manage.py createsuperuser
   ```
9. Start the server:
      ```bash
   python manage.py runserver
   ```

## Usage
- Access the admin panel at http://localhost:8000/admin to manage quizzes, questions, and answers.
- Use the API endpoints to interact with the quiz data programmatically.

## API Endpoints
* List all quizzes: GET /quiz/
* Retrieve a random question from a specific quiz: GET /quiz/r/<quiz_title>/
* List all questions from a specific quiz: GET /quiz/q/<quiz_title>/
