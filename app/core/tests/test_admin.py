from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email = 'admin@tm.com',
            password='password123'
        )
        self.client.force_login(self.admin_user)

        self.user = get_user_model().objects.create_user(
            email='test@GMAIL.com',
            password='password1234', 
            name='Test user Full Name'
        )

    def test_users_listed(self):
        """ Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        # /admin/core/user/
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200) # status code of HTTP for OKAY.
    
    def test_create_user_page(self):
        """Tests that the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200) # status code of HTTP for OKAY.
