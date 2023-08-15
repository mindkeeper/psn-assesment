from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    def test_create_customer_with_email_successfull(self):
        email = 'test@example.com'
        password = 'test123'
        phone_number = '081234567890'
        name = 'john doe'
        customer = get_user_model().objects.create_customer(
            email=email,
            password=password,
            phone_number=phone_number,
            name=name,
        )

        self.assertEqual(customer.email, email)
        self.assertTrue(customer.check_password(password))
