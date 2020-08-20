from django.test import TestCase

from .models import Hood, User

class TestHood(TestCase):
    def setUp(self):
        self.a_user = User(username='grishon', email='grish@gmail.com', password='123@Iiht')
        self.a_hood = Hood(name='Kasa', location='Thika Rd', population='68971')
        self.a_user.save()
        self.a_hood.save()

    def tearDown(self):
        pass

    def test_createHood(self):
        self.a_hood.admin.add(self.a_user)

        self.assertEqual(len(Hood.objects.all()), 1)
        self.assertEqual(len(User.objects.all()), 1)

    def test_get_all_hoods(self):
        self.assertEqual(len(Hood.get_all_hoods()), 1)