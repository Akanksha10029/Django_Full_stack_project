# Review Management System

A Django-based web application enabling users to review YouTube videos. This Review Management System allows users to share their insights and help others make informed choices about which videos to watch based on community reviews.

## Table of Contents
- [Features](#features)
- [Skills Used](#skills-used)
- [Installation](#installation)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [Link to Repository](#link-to-repository)

## Features

- **User Registration and Authentication**
- **Add, Edit, and Delete Reviews**
- **Video Search Functionality**
- **Review Ratings and Comments**
- **Insights and Recommendations**

## Skills Used

- **Django** (backend framework)
- **Python** (server-side logic)
- **SQLite3** (database management)
- **HTML/CSS** (frontend structure and design)
- **JavaScript** (UI interactivity)
  
## Installation
Follow these steps to set up and run the Review Management System locally.

## Prerequisites
- **Python 3.8+** installed on your machine.
- **Git** (for cloning the repository).
- **Virtual Environment** (recommended for dependency management).

## Setup Instructions

### Clone the repository:
```bash
git clone https://github.com/Akanksha10029/Django_Full_stack_project.git
cd Django_Full_stack_project
```
### Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
### Install required dependencies:
```bash
pip install -r requirements.txt
```
### Create a .env file: In the root directory, create a .env file to securely store environment variables such as the Django secret key and any API keys.
Example .env file:
```env
SECRET_KEY=your_secret_key_here
DEBUG=True
```
### Apply database migrations:
```bash
python manage.py migrate
```
### Create a superuser (for accessing the admin panel):
```bash
python manage.py createsuperuser
```
### Run the server:
```bash
python manage.py runserver
```
Access the application: Open http://localhost:8000 in your web browser.

## Usage:
- Register/Login: Create an account or log in to access review functionalities.
- Browse Videos: Search and browse videos within the platform.
- Add a Review: Navigate to a video’s page and submit your review along with a rating.
- Edit or Delete Reviews: Manage your submitted reviews directly from your profile.
- View Community Insights: Browse through reviews and ratings from other users to make informed decisions.

## Troubleshooting
- Dependency Issues: Ensure all dependencies in requirements.txt are installed. Use pip freeze to check installed packages.
- Database Errors: Run python manage.py migrate to apply any missing migrations.
- Environment Variable Issues: Make sure the .env file is correctly configured with required variables like SECRET_KEY.

## Link to Repository

[Akanksha10029/Django_Full_stack_project (GitHub)](https://github.com/Akanksha10029/Django_Full_stack_project)
