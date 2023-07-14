# NBA_V3 - Streamlining Faculty Contribution Evaluation for NBA

The project aims to develop an online platform for the National Board of Accreditation (NBA) to evaluate and monitor faculty members' performance in educational institutions as per Criteria 5 of NBA. The objective is to provide a comprehensive system to track and analyze faculty members' performance and facilitate the accreditation process.

## Features
- User-friendly interface
- Secure login
- Faculty dashboard
- Report generation

## Getting Started
To get started with the project, follow these steps:

1. Clone the repository: git clone https://github.com/NaveenNannick/NBA_V3.git

2. Install the required dependencies. It is recommended to set up a virtual environment:
```bash
cd NBA_V3
python -m venv venv
source venv/bin/activate  # For macOS/Linux
.\venv\Scripts\activate  # For Windows
pip install -r requirements.txt
```
3. Configure the database settings in the settings.py file. Make sure to update the DATABASES section with your MySQL database credentials.

4. Apply the database migrations:
```bash
python manage.py migrate
```
5. Start the development server:
```bash
python manage.py runserver
```
6. Open a web browser and navigate to http://localhost:8000 to access the application.




