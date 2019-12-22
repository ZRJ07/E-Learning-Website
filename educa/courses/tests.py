from django.test import TestCase
from .models import Course, Subject
from django.contrib.auth.models import User
from django.urls import reverse


# to test the modules of the course
class CourseModelTest(TestCase):

    # test username, title etc
    def setUp(self):
        self.u1 = User.objects.create(username='user1')
        self.sub1 = Subject.objects.create(title='demo', slug='demo')
        self.course1 = Course.objects.create(owner=self.u1,
                              subject=self.sub1,
                              title='course1',
                              slug='course1',
                              overview='demo')
        self.u2 = User.objects.create(username='std')
        self.course1.students.add(self.u2)
    # test course content
    def test_course_content(self):
        expected_object_name = f'{self.course1.title}'
        self.assertEqual(expected_object_name, 'course1')
    # test subject content
    def test_subject_content(self):
        expected_object_name = f'{self.sub1.title}'
        self.assertEqual(expected_object_name, 'demo')
    # test username of student
    def test_student_field(self):
        std = self.course1.students.values_list('username').first()[0]
        expected_object_name = f'{std}'
        self.assertEqual(expected_object_name, 'std')
    # test user only
    def test_user(self):
        expected_object_name = f'{self.u1.username}'
        self.assertEqual(expected_object_name, 'user1')


### URL Test
class CoursePageViewTest(TestCase):

    # test user page
    def setup(self):
        self.u1 = User.objects.create(username='user1')
        self.sub1 = Subject.objects.create(title='demo', slug='demo')
        self.course1 = Course.objects.create(owner=self.u1,
                              subject=self.sub1,
                              title='course1',
                              slug='course1',
                              overview='demo')
        self.u2 = User.objects.create(username='std')
        self.course1.students.add(self.u2)

    # test view url exists at proper location
    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    # test view uses correct templates
    def test_view_uses_correct_templates(self):
        resp = self.client.get(reverse('course_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'courses/course/list.html')
