# Django Blog Application

A feature-rich blog application built with Django 5.1.5, featuring user authentication, comment system, post tagging, search functionality, and RSS feed.

## Features

-   Post Creation and Management

    -   Create, edit, and delete blog posts
    -   Draft and published post status
    -   SEO-friendly URLs
    -   Markdown support for post content
    -   Post tagging system

-   User Interaction

    -   User comments on posts
    -   Email post sharing
    -   Comment moderation system
    -   RSS feed for latest posts

-   Search and Navigation

    -   Full-text search with PostgreSQL
    -   Tag-based post filtering
    -   Similar posts suggestions
    -   Pagination

-   Admin Interface
    -   Django admin customization
    -   User-friendly post management
    -   Comment moderation tools

## Technologies Used

-   Django 5.1.5
-   PostgreSQL
-   Python Markdown
-   django-taggit
-   HTML/CSS

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd myblog
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set up environment variables:

```bash
cp .env.example .env
# Edit .env with your settings
```

5. Set up the database:

```bash
python manage.py migrate
```

6. Create a superuser:

```bash
python manage.py createsuperuser
```

7. Run the development server:

```bash
python manage.py runserver
```

## Environment Variables

Create a `.env` file in the project root with the following variables:

```plaintext
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
EMAIL_HOST=smtp.gmail.com
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
EMAIL_PORT=587
EMAIL_USE_TLS=True
DB_NAME=blog
DB_USER=blog
DB_PASSWORD=your-db-password
DB_HOST=localhost
DB_PORT=5432
```

## Project Structure

```
myblog/
├── blog/
│   ├── admin.py         # Admin interface configuration
│   ├── models.py        # Database models
│   ├── views.py         # View functions
│   ├── urls.py          # URL configurations
│   ├── forms.py         # Form definitions
│   ├── sitemaps.py      # Sitemap configuration
│   └── templates/       # HTML templates
├── static/              # Static files (CSS, JS)
├── manage.py            # Django management script
├── requirements.txt     # Project dependencies
└── README.md           # Project documentation
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License.
