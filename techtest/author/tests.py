import json

from django.test import TestCase
from django.urls import reverse

from techtest.author.models import Author


class RegionListViewTestCase(TestCase):
    def setUp(self):
        self.url = reverse("author-list")
        self.author_1 = Author.objects.create(first_name="David Alaka", last_name="Alaka")
        self.author_2 = Author.objects.create(first_name="William", last_name="Shakespear")
    def test_serializes_with_correct_data_shape_and_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertCountEqual(
            response.json(),
            [
                {
                    "id": self.author_1.id,
                    "first_name": "David Alaka",
                    "last_name": "Alaka"
                },
                {
                    "id": self.author_2.id,
                    "first_name":"William",
                    "last_name":"Shakespear"
                },
            ],
        )

    def test_creates_new_author(self):
        payload = {
            "first_name": "David",
            "last_name": "Alaka",
        }
        response = self.client.post(
            self.url, data=json.dumps(payload), content_type="application/json"
        )
        author = Author.objects.last()
        self.assertEqual(response.status_code, 201)
        self.assertIsNotNone(author)
        self.assertEqual(Author.objects.count(), 3)
        self.assertDictEqual(
            {
                "id": author.id,
                "first_name": "David",
                "last_name": "Alaka",
            },
            response.json(),
        )

class AuthorViewTestCase(TestCase):
    def setUp(self):
        self.author = Author.objects.create(first_name="David", last_name="Alaka")
        self.url = reverse("author", kwargs={"author_id": self.author.id})

    def test_serializes_single_author_with_correct_data_shape_and_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertCountEqual(
            response.json(),
            {
                "id": self.author.id,
                "first_name": "David",
                "last_name": "Alaka",
            },
        )

    def test_updates_author(self):
        payload = {
            "id": self.author.id,
            "first_name": "David",
            "last_name": "Alaka",
        }
        response = self.client.put(
            self.url, data=json.dumps(payload), content_type="application/json"
        )
        author = Author.objects.filter(id=self.author.id).first()
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(author)
        self.assertEqual(Author.objects.count(), 1)
        self.assertDictEqual(
            {
                "id": author.id,
                "first_name": "David",
                "last_name": "Alaka",
            },
            response.json(),
        )

    def test_removes_author(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Author.objects.count(), 0)
