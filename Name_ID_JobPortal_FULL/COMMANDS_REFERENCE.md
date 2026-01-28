# Quick Command Reference

## Running the Application

### Start Development Server
```bash
cd Name_ID_JobPortal_FULL
python manage.py runserver
# Access at: http://127.0.0.1:8000/
```

### Start on Different Port
```bash
python manage.py runserver 8001
# Access at: http://127.0.0.1:8001/
```

## Testing

### Run All Tests
```bash
python manage.py test
```

### Run with Verbose Output
```bash
python manage.py test -v 2
```

### Run Specific Test Module
```bash
python manage.py test tests.AccountTests
python manage.py test tests.JobTests
python manage.py test tests.JobApplicationTests
```

### Run Specific Test
```bash
python manage.py test tests.AccountTests.test_register_jobseeker
```

## Database Management

### Create New Database (Fresh Start)
```bash
rm db.sqlite3
python manage.py migrate
```

### Show Migration Status
```bash
python manage.py showmigrations
```

### Create Migrations
```bash
python manage.py makemigrations
```

### Apply Migrations
```bash
python manage.py migrate
```

## Django Shell (Interactive Python)

### Launch Django Shell
```bash
python manage.py shell
```

### Create Test User (in shell)
```python
from accounts.models import User
User.objects.create_user(
    username='testuser',
    password='testpass123',
    user_type='JOBSEEKER',
    email='test@example.com'
)
```

### Create Recruiter (in shell)
```python
from accounts.models import User
User.objects.create_user(
    username='recruiter1',
    password='testpass123',
    user_type='RECRUITER',
    email='recruiter@example.com'
)
```

### Create Job (in shell)
```python
from accounts.models import User
from jobs.models import Job
recruiter = User.objects.get(username='recruiter1')
Job.objects.create(
    recruiter=recruiter,
    title='Python Developer',
    category='IT',
    skills='Python, Django',
    openings=2,
    description='Looking for experienced Python developer'
)
```

### List All Users
```python
from accounts.models import User
User.objects.all()
```

### List All Jobs
```python
from jobs.models import Job
Job.objects.all()
```

## Admin Interface

### Create Superuser
```bash
python manage.py createsuperuser
# Then access: http://127.0.0.1:8000/admin/
```

### Access Admin Panel
Open browser to: http://127.0.0.1:8000/admin/
Login with superuser credentials

## Static Files & Media

### Collect Static Files (for production)
```bash
python manage.py collectstatic --noinput
```

### Check File Uploads
Resume files are stored in: `media/resumes/`

## System Check

### Run Django System Checks
```bash
python manage.py check
```

### List All Installed Apps
```bash
python manage.py shell
from django.apps import apps
for app in apps.get_app_configs():
    print(app.name)
```

## URL Paths Quick Reference

### Authentication URLs
- `/accounts/register/` - Register new user
- `/accounts/login/` - Login
- `/accounts/logout/` - Logout
- `/accounts/profile/` - Edit profile

### Job URLs
- `/jobs/` - Browse jobs
- `/jobs/create/` - Create new job (recruiters)
- `/jobs/<id>/` - View job details

### Dashboard
- `/` - Dashboard (authenticated users)

### Admin
- `/admin/` - Admin panel (superuser)

## Helpful Terminal Commands

### Check Python Version
```bash
python --version
```

### Check Django Version
```bash
python -m django --version
```

### List Project Files
```bash
dir  # Windows
ls -la  # Mac/Linux
```

### Search for Files
```bash
find . -name "*.html"  # Find all HTML files
find . -name "*.py"    # Find all Python files
```

## Development Workflow

### 1. Edit Code
```bash
# Edit your files in an editor
# Save changes
```

### 2. Test Changes
```bash
# Server auto-reloads on file changes
# Check: http://127.0.0.1:8000/
```

### 3. If Errors Occur
```bash
# Check terminal output for error messages
# Fix the issue
# Refresh browser (Ctrl+F5 for hard refresh)
```

### 4. Run Tests
```bash
python manage.py test -v 2
```

### 5. Commit Changes (if using Git)
```bash
git add .
git commit -m "Add feature description"
git push
```

## Common Issues & Solutions

### Port Already in Use
```bash
# Use different port
python manage.py runserver 8001
```

### Database Locked Error
```bash
# Remove and recreate database
rm db.sqlite3
python manage.py migrate
```

### ModuleNotFoundError
```bash
# Install missing package
pip install django
```

### Template Not Found
```bash
# Check TEMPLATES setting in settings.py
# Ensure template file exists in templates/ directory
```

### Migrations Error
```bash
# Reset migrations
python manage.py migrate --fake-initial
python manage.py migrate
```

## Performance Testing

### Run Tests with Timing
```bash
python manage.py test -v 2 --debug-mode
```

### Profile Database Queries
```python
from django.test.utils import override_settings
from django.conf import settings
from django.db import connection

# In your code
from django.db import reset_queries
reset_queries()
# ... run your code ...
print(len(connection.queries), 'queries executed')
for query in connection.queries:
    print(query)
```

## Debugging

### Print Debug Info
```python
# In views.py
import pprint
pprint.pprint(some_variable)
```

### Django Debug Toolbar (if installed)
```bash
pip install django-debug-toolbar
# Then add to INSTALLED_APPS and URLs
```

### Check Template Context
```python
# In views.py
context = {'jobs': jobs, 'query': q}
print(context)  # See what's passed to template
```

## Production Deployment Preparation

### Check for Production Issues
```bash
python manage.py check --deploy
```

### Create Requirements File
```bash
pip freeze > requirements.txt
```

### Settings for Production
1. Change `DEBUG = False` in settings.py
2. Set `ALLOWED_HOSTS = ['yourdomain.com']`
3. Set `SECRET_KEY` to random value
4. Configure `DATABASES` for PostgreSQL
5. Set up `STATIC_ROOT` and `MEDIA_ROOT`

## Backup & Restore

### Backup Database
```bash
# SQLite: just copy db.sqlite3
cp db.sqlite3 db.sqlite3.backup
```

### Restore Database
```bash
cp db.sqlite3.backup db.sqlite3
```

## Useful Django Commands

### List All Registered Commands
```bash
python manage.py help
```

### Get Help on Specific Command
```bash
python manage.py help runserver
python manage.py help test
python manage.py help migrate
```

### Clear Cache
```bash
python manage.py clear_cache
```

### Create App (if needed)
```bash
python manage.py startapp newapp
```

---

## Quick Shortcuts

| Task | Command |
|------|---------|
| Start server | `python manage.py runserver` |
| Run tests | `python manage.py test -v 2` |
| Database reset | `rm db.sqlite3 && python manage.py migrate` |
| Open shell | `python manage.py shell` |
| Check errors | `python manage.py check` |
| Django version | `python -m django --version` |
| Access app | http://127.0.0.1:8000/ |
| Access admin | http://127.0.0.1:8000/admin/ |

---

**Last Updated**: January 24, 2026
