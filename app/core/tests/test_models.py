from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    def test_create_customer_with_email_successfull(self):
        email = 'test@example.com'
        password = 'test123'
        name = 'john doe'
        customer = get_user_model().objects.create_customer(
            email=email,
            password=password,
            name=name,
        )

        self.assertEqual(customer.email, email)
        self.assertTrue(customer.check_password(password))

    def test_new_cutomer_email_nornalized(self):
        sample_test = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]

        for email, expected in sample_test:
            user = get_user_model().objects.create_customer(
                email=email,
                name='test',
                password='test123'
            )
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raise_error(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_customer('', 'test', 'test123')

    def test_create_admin(self):
        admin = get_user_model().objects.create_admin(
            'test@example.com',
            'test123'
            )
        self.assertTrue(admin.is_superuser)
