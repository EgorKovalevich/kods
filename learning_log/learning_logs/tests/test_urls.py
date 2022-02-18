from django.test import TestCase
from django.urls import reverse


class UrlsTestCase(TestCase):
    def test_urls(self):
        url = ('http://localhost:8000/topics/')
        print(url)
        response = self.client.get(url)
        print(response)

        url = ('http://localhost:8000/topic/47/')
        print(url)
        response = self.client.get(url)
        print(response)

        url = ('http://localhost:8000/new_entry/47/')
        print(url)
        response = self.client.get(url)
        print(response)

        url = ('http://localhost:8000/edit_entry/42/')
        print(url)
        response = self.client.get(url)
        print(response)

        url = ('http://localhost:8000/entry/42/delete')
        print(url)
        response = self.client.get(url)
        print(response)

        url = ('http://localhost:8000/topic/47/delete')
        print(url)
        response = self.client.get(url)
        print(response)

        url = ('http://localhost:8000/users/logout/')
        print(url)
        response = self.client.get(url)
        print(response)

        url = ('http://localhost:8000/users/register/')
        print(url)
        response = self.client.get(url)
        print(response)

        url = ('http://localhost:8000/users/login/')
        print(url)
        response = self.client.get(url)
        print(response)

        url = ('http://localhost:8000/')
        print(url)
        response = self.client.get(url)
        print(response)