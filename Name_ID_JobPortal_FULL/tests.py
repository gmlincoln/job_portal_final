from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User, RecruiterProfile, JobSeekerProfile
from jobs.models import Job, JobApplication


class AccountTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_register_jobseeker(self):
        response = self.client.post('/accounts/register/', {
            'username': 'testuser',
            'display_name': 'Test User',
            'email': 'test@example.com',
            'password': 'testpass123',
            'password2': 'testpass123',
            'user_type': 'JOBSEEKER'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='testuser').exists())
        user = User.objects.get(username='testuser')
        self.assertEqual(user.user_type, 'JOBSEEKER')
        self.assertTrue(JobSeekerProfile.objects.filter(user=user).exists())

    def test_register_recruiter(self):
        response = self.client.post('/accounts/register/', {
            'username': 'recruiter1',
            'display_name': 'Recruiter',
            'email': 'recruiter@example.com',
            'password': 'testpass123',
            'password2': 'testpass123',
            'user_type': 'RECRUITER'
        })
        self.assertEqual(response.status_code, 302)
        user = User.objects.get(username='recruiter1')
        self.assertTrue(RecruiterProfile.objects.filter(user=user).exists())

    def test_password_mismatch(self):
        response = self.client.post('/accounts/register/', {
            'username': 'testuser2',
            'email': 'test2@example.com',
            'password': 'pass123',
            'password2': 'pass456',
            'user_type': 'JOBSEEKER'
        })
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username='testuser2').exists())

    def test_login(self):
        User.objects.create_user(
            username='loginuser',
            password='testpass123',
            user_type='JOBSEEKER',
            email='login@example.com'
        )
        response = self.client.post('/accounts/login/', {
            'username': 'loginuser',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, 302)


class JobTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.recruiter = User.objects.create_user(
            username='recruiter',
            password='testpass123',
            user_type='RECRUITER',
            email='recruiter@example.com'
        )
        RecruiterProfile.objects.create(
            user=self.recruiter,
            company_name='Tech Corp',
            company_description='A tech company'
        )

    def test_job_list_view(self):
        Job.objects.create(
            recruiter=self.recruiter,
            title='Python Developer',
            category='IT',
            description='Looking for a Python dev',
            skills='Python, Django',
            openings=2
        )
        response = self.client.get('/jobs/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Python Developer')

    def test_job_create_requires_login(self):
        response = self.client.get('/jobs/create/')
        self.assertEqual(response.status_code, 302)

    def test_job_create_by_recruiter(self):
        self.client.login(username='recruiter', password='testpass123')
        response = self.client.post('/jobs/create/', {
            'title': 'Senior Dev',
            'category': 'IT',
            'openings': 3,
            'skills': 'Python, Django, PostgreSQL',
            'description': 'Senior Python developer needed'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Job.objects.filter(title='Senior Dev').exists())


class JobApplicationTests(TestCase):
    def setUp(self):
        self.recruiter = User.objects.create_user(
            username='recruiter',
            password='testpass123',
            user_type='RECRUITER',
            email='recruiter@example.com'
        )
        RecruiterProfile.objects.create(user=self.recruiter)
        
        self.jobseeker = User.objects.create_user(
            username='jobseeker',
            password='testpass123',
            user_type='JOBSEEKER',
            email='job@example.com'
        )
        JobSeekerProfile.objects.create(
            user=self.jobseeker,
            skills='Python, Django'
        )
        
        self.job = Job.objects.create(
            recruiter=self.recruiter,
            title='Python Dev',
            category='IT',
            skills='Python, Django',
            openings=1,
            description='Dev needed'
        )
        self.client = Client()

    def test_apply_for_job(self):
        self.client.login(username='jobseeker', password='testpass123')
        response = self.client.post(f'/jobs/{self.job.id}/', {})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            JobApplication.objects.filter(
                job=self.job,
                applicant=self.jobseeker
            ).exists()
        )

    def test_cannot_apply_twice(self):
        self.client.login(username='jobseeker', password='testpass123')
        self.client.post(f'/jobs/{self.job.id}/', {})
        count_before = JobApplication.objects.count()
        self.client.post(f'/jobs/{self.job.id}/', {})
        count_after = JobApplication.objects.count()
        self.assertEqual(count_before, count_after)
