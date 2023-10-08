from django.test import TestCase

# Create your tests here.


class RekrutoTesting(TestCase):
    def test_homepage(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_hello_funk(self):
        response = self.client.get('/rekruto',data={'name':'Илья','message':'Я Илья'})
        self.assertEqual(response.status_code, 200)

    def test_redirect(self):
        response = self.client.get('/rekruto', data={'name': '', 'message': 'Я Илья'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, 'https://www.youtube.com/watch?v=eBGIQ7ZuuiU')
