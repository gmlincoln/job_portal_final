# JobPortal - Django Job Portal Platform

A full-featured, Level-4 compliant Django job portal connecting recruiters with jobseekers. Features include user registration, profile management, job posting, resume uploads, and intelligent skill-based job matching.

## Features

### 👥 User Management
- **Registration**: Username, display name, email, password confirmation, user type selection
- **Authentication**: Secure login/logout with session management
- **Roles**: 
  - **Recruiters**: Post jobs, manage listings, view applications
  - **Jobseekers**: Search jobs, apply, upload resumes, view matched jobs

### 💼 Job Management
- **Job Posting** (Recruiters): Title, category, number of openings, description, required skills
- **Job Search** (All users): Filter by keyword, category
- **Job Categories**: IT, Finance, HR, Sales, Marketing, Other
- **Job Details**: View full job description, skills required, openings

### 🎯 Skill Matching
- **Intelligent Matching**: Dashboard shows jobseekers jobs matching their skills
- **For Recruiters**: View all job postings and applications
- **Responsive Dashboard**: Different views for jobseekers and recruiters

### 📄 Profile Management
- **Jobseeker Profiles**: 
  - Add/edit skills (comma-separated)
  - Upload and manage resumes
- **Recruiter Profiles**: 
  - Company name and description
  - View posted jobs and application counts

### 📱 Responsive UI
- Built with **Tailwind CSS** for modern, mobile-friendly design
- Clean navigation with user authentication status
- Success/error message system
- Beautiful cards and layouts

## Project Structure

```
Name_ID_JobPortal/
├── Name_ID_JobPortal/          # Project settings & configuration
│   ├── settings.py             # Django settings (DB, apps, middleware)
│   ├── urls.py                 # Project URL routing
│   └── wsgi.py                 # WSGI application
├── accounts/                   # User authentication & profiles
│   ├── models.py              # User, RecruiterProfile, JobSeekerProfile
│   ├── views.py               # Login, register, logout, profile edit
│   ├── urls.py                # Auth routes
│   └── admin.py               # Admin interface
├── jobs/                       # Job management
│   ├── models.py              # Job, JobApplication models
│   ├── views.py               # Job list, create, detail, apply
│   ├── urls.py                # Job routes
│   └── admin.py               # Admin interface
├── dashboard/                  # User dashboard
│   ├── views.py               # Dashboard with skill matching
│   └── urls.py                # Dashboard route
├── templates/                  # HTML templates
│   ├── base.html              # Base template with navbar
│   ├── accounts/              # Auth templates
│   │   ├── login.html
│   │   ├── register.html
│   │   └── profile.html
│   ├── jobs/                  # Job templates
│   │   ├── list.html
│   │   ├── detail.html
│   │   └── create.html
│   └── dashboard.html         # Dashboard template
├── manage.py                   # Django management script
├── db.sqlite3                  # SQLite database
├── requirements.txt            # Python dependencies
├── tests.py                    # Unit and integration tests
└── README.md                   # This file
```

## Database Models

### User (Custom User Model)
- `username`: Unique identifier
- `email`: Email address
- `first_name`: Display name
- `user_type`: RECRUITER or JOBSEEKER
- Inherits from Django's AbstractUser

### RecruiterProfile
- `user`: OneToOne link to User
- `company_name`: Company name
- `company_description`: Company details

### JobSeekerProfile
- `user`: OneToOne link to User
- `skills`: Comma-separated skill list
- `resume`: Uploaded resume file

### Job
- `recruiter`: ForeignKey to User (Recruiter)
- `title`: Job title
- `category`: Job category (IT, Finance, HR, Sales, Marketing, Other)
- `description`: Full job description
- `skills`: Required skills
- `openings`: Number of positions
- `created_at`: Job creation timestamp

### JobApplication
- `job`: ForeignKey to Job
- `applicant`: ForeignKey to User (Jobseeker)
- `applied_on`: Application timestamp

## Setup & Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Steps

1. **Clone/Navigate to project**
   ```bash
   cd Name_ID_JobPortal_FULL
   ```

2. **Create a virtual environment** (Optional but recommended)
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Mac/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (Optional, for admin panel)
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Running Tests

```bash
# Run all tests
python manage.py test

# Run specific test module
python manage.py test tests.AccountTests
python manage.py test tests.JobTests
python manage.py test tests.JobApplicationTests

# Run with verbose output
python manage.py test -v 2
```

### Test Coverage
- **AccountTests**: User registration, login, validation
- **JobTests**: Job creation, listing, recruiter-only access
- **JobApplicationTests**: Job applications, duplicate prevention

## Usage Guide

### For Jobseekers
1. **Register** as a jobseeker at `/accounts/register/`
2. **Update Profile** at `/accounts/profile/` - Add skills and upload resume
3. **Browse Jobs** at `/jobs/` - Search by keyword or category
4. **Apply for Jobs** - View job details and click "Apply Now"
5. **View Dashboard** at `/` - See jobs matching your skills
6. **Logout** when done

### For Recruiters
1. **Register** as a recruiter at `/accounts/register/`
2. **Update Company Profile** at `/accounts/profile/` - Add company info
3. **Post Jobs** at `/jobs/create/` - Fill in job details and skills required
4. **View Dashboard** at `/` - See all your posted jobs and application counts
5. **Browse Jobs** - View all jobs on the platform
6. **Logout** when done

## Features in Detail

### Skill Matching Algorithm
- Converts both jobseeker skills and job required skills to lowercase
- Splits comma-separated values into sets
- Finds intersection (matching skills)
- Displays jobs with any matching skills on jobseeker dashboard

### Resume Upload
- Jobseekers can upload files (PDF, DOC, DOCX)
- Files stored in `/media/resumes/` directory
- Accessible via profile page

### Search & Filtering
- Full-text search across job title, description, and skills
- Category filtering
- Combined search + filter support

## API Endpoints

### Authentication
- `POST /accounts/register/` - Register new user
- `POST /accounts/login/` - User login
- `GET /accounts/logout/` - User logout
- `GET /accounts/profile/` - View/edit profile

### Jobs
- `GET /jobs/` - List all jobs (search & filter)
- `POST /jobs/create/` - Create new job (recruiters only)
- `GET /jobs/<id>/` - View job details
- `POST /jobs/<id>/` - Apply for job (jobseekers only)

### Dashboard
- `GET /` - Dashboard (authenticated users)

## Security Features
- Password confirmation on registration
- Duplicate username/email prevention
- Login required decorators on protected views
- CSRF protection on all forms
- Role-based access control (recruiter vs jobseeker)
- Secure password hashing (Django default)

## Performance Considerations
- Database indexed by created_at for job ordering
- Efficient skill matching with set operations
- Lazy loading of related objects
- Pagination ready (can be added to job lists)

## Future Enhancements
- Email notifications for applications
- Job bookmarking/favorites
- Advanced filtering (salary range, experience level)
- Application status tracking (accepted, rejected, pending)
- Company ratings and reviews
- Real-time notifications
- API for mobile app
- Social login integration
- Advanced analytics for recruiters

## Technology Stack
- **Backend**: Django 6.0+
- **Database**: SQLite3
- **Frontend**: HTML5, CSS3, Tailwind CSS 2.2
- **Python Version**: 3.8+

## Known Limitations
- SQLite recommended for development only; use PostgreSQL for production
- Media files served via Django in development (use CDN in production)
- Single-threaded dev server (use Gunicorn/uWSGI for production)
- No caching implemented

## Compliance
✅ **Level-4 Requirements Met**
- Django project with proper structure
- SQLite database with proper storage
- User registration with all required fields
- Login functionality
- Role-based profile management (recruiter/jobseeker)
- Job posting with all required fields
- Job search for jobseekers
- Skill-based job matching dashboard
- Modern UI with Tailwind CSS
- Comprehensive test suite
- Complete documentation

## File Structure Checklist
- ✅ `manage.py` - Django management script
- ✅ `settings.py`, `urls.py`, `wsgi.py` - Project configuration
- ✅ App configs, models, views, urls - App structure
- ✅ `db.sqlite3` - Database file (created after migrations)
- ✅ Templates with Tailwind CSS styling
- ✅ Media storage for resume uploads

## Troubleshooting

### Port Already in Use
```bash
# Use a different port
python manage.py runserver 8001
```

### Database Errors
```bash
# Reset database
rm db.sqlite3
python manage.py migrate
```

### Migration Issues
```bash
# Check migrations
python manage.py showmigrations
# Reapply migrations
python manage.py migrate --fake-initial
```

### Static Files Not Loading
```bash
# Collect static files (for production)
python manage.py collectstatic --noinput
```

## Support
For issues or questions, refer to the Django documentation at https://docs.djangoproject.com/

## License
Educational project - Feel free to use and modify

---

**Created**: January 2026  
**Version**: 1.0 (Level-4 Complete)
