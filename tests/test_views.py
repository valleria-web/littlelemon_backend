from rest_framework import status
from rest_framework.test import APITestCase
from . import Menu
from . import MenuSerializer

class MenuViewTest(APITestCase):

    def setUp(self):
        self.first_menu = Menu.objects.create(
            ID=1,
            Title='Pizza',
            Price=20.99,
            Inventory=10
        )
        self.second_menu = Menu.objects.create(
            ID=2,
            Title='Hamburger',
            Price=15.99,
            Inventory=20
        )
        self.third_menu = Menu.objects.create(
            ID=3,
            Title='Sandwich',
            Price=10.99,
            Inventory=30
        )

    def test_getall(self):
        response = self.client.get('/api/menu/')
        menus = Menu.objects.all()
        serialized = MenuSerializer(menus, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
