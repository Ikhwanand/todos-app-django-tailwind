# Django Todo App with Tailwind CSS

A modern, responsive Todo application built with Django and styled with Tailwind CSS. This application features user authentication, task management, and a beautiful user interface.

## Features

- **User Authentication**
  - User registration and login
  - Password reset functionality
  - Secure session management

- **Task Management**
  - Create, read, update, and delete tasks
  - Mark tasks as complete/incomplete
  - Add descriptions to tasks
  - User-specific task lists

- **Modern UI/UX**
  - Clean and responsive design using Tailwind CSS
  - Interactive modals for editing tasks
  - Real-time task updates
  - Success notifications
  - Mobile-friendly interface

## Technologies Used

- **Backend**
  - Django 5.1
  - django-allauth (Authentication)
  - SQLite (Database)

- **Frontend**
  - Tailwind CSS
  - JavaScript (Fetch API)
  - HTML5

## Installation

1. Clone the repository
   ```bash
   git clone <repository-url>
   cd todos-app-django-tailwind
   ```

2. Create and activate a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations
   ```bash
   python manage.py migrate
   ```

5. Create a superuser (Optional)
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server
   ```bash
   python manage.py runserver
   ```

7. Visit `http://127.0.0.1:8000` in your browser

## Project Structure

```
todos-app-django-tailwind/
├── core/                   # Project settings
├── todos/                  # Main app directory
│   ├── migrations/        # Database migrations
│   ├── templates/        # HTML templates
│   ├── admin.py          # Admin configuration
│   ├── models.py         # Database models
│   ├── urls.py           # URL configurations
│   └── views.py          # View logic
├── templates/             # Global templates
│   ├── account/          # Authentication templates
│   └── base.html         # Base template
├── static/               # Static files
├── manage.py             # Django management script
├── requirements.txt      # Project dependencies
└── README.md            # Project documentation
```

## Features in Detail

### Task Management
- Create new tasks with title and optional description
- Mark tasks as complete with a single click
- Edit existing tasks through a modal interface
- Delete tasks you no longer need
- Tasks are private to each user

### User Interface
- Clean and intuitive design
- Responsive layout that works on all devices
- Interactive feedback for user actions
- Smooth animations and transitions

### Authentication
- Secure user registration and login
- Password reset via email
- User session management
- Protected routes for authenticated users

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.