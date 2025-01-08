from rest_framework.test import APITestCase
from rest_framework import status

from users.tests.utils import get_admin_user


class UserTestCase(APITestCase):
    """Тесты для модели User 2 опции:
    1. ОБЩИЙ для запуска тестов из терминала
    2. ЛОКАЛЬНЫЙ для запуска тестов только в этом файле"""

    def setUp(self) -> None:
        """Базовые настройки"""
        self.user = get_admin_user()
        response = self.client.post('/users/token/', {"email": "tester@test1.com", "password": "qwerty"})
        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer  {self.access_token}')

    """если вы хотите запустить ЛОКАЛЬНЫЙ тест только для этого файла"""

    def test_user_create(self):
        data = {
            'email': 'tester_create@test.com',
            'role': 'member',
            'password': 'testdrfweb320'
        }
        response = self.client.post('/users/create/', data=data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['email'], 'tester_create@test.com')

    def test_user_delete(self):
        response = self.client.delete(f'/users/{self.user.id}/delete/')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_detail(self):
        response = self.client.get(f'/users/{self.user.id}/')
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['email'], 'tester@test1.com')
        self.assertEqual(response.json()['is_active'], True)

    def test_user_list(self):
        response = self.client.get('/users/')
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()[0]['email'], 'tester@test1.com')

    def test_user_update(self):
        data = {
            'email': 'tester_update@test1.com',
            'password': 'qwerty',
        }
        response = self.client.patch(f'/users/{self.user.id}/update/', data=data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['email'], "tester_update@test1.com")
