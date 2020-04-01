import json
from django.test import TestCase
from django.test.testcases import SerializeMixin
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Article



# Create your tests here.
MOCK_ARTICLE = {
    "title": "this is title"
}


class TestBase(APITestCase):

    def setUp(self):
        self.client = self.create_http_client()

    @staticmethod
    def create_http_client(token=None):
        client = APIClient()
        if token:
            client.credentials(HTTP_AUTHORIZATION='Token %s' % token)
        return client

    def status_code_test(self, uri, expected_status_code, method='GET', params=None, format='json'):
        try:
            resp = getattr(self.client, method.lower())(path=uri, data=params, format=format)
        except Exception as e:
            print(e)
            return
        err_msg = "Expected status-code => %s, received => %s" % (expected_status_code, resp.status_code)
        self.assertEqual(expected_status_code, resp.status_code, err_msg)


class ArticleTestCase(TestBase):
    def setUp(self):
        super(TestBase, self).setUp()

    def list_article(self):
        uri = "/blog/article/"
        self.status_code_test(uri, 200)

    def create_article_with_invalid_data(self):
        uri = "/blog/article/"
        self.status_code_test(uri, 200, 'POST', {})

    def create_article_with_valid_data(self):
        uri = "/blog/article/"
        self.status_code_test(uri, 200, 'POST', MOCK_ARTICLE)

    def update_article_with_invalid_data(self):
        article = Article.objects.get(title=MOCK_ARTICLE['title'])
        uri = "/blog/article/%s/" % "33"
        self.status_code_test(uri, 200, 'POST', MOCK_ARTICLE)

    def update_article_with_valid_data(self):
        article = Article.objects.get(title=MOCK_ARTICLE['title'])
        uri = "/blog/article/%s/" % article.id
        self.status_code_test(uri, 200, 'POST', MOCK_ARTICLE)

    def delete_article_with_invalid_data(self):
        uri = '/blog/article/%s/' % '10000'
        self.status_code_test(uri, 400, 'DELETE')

    def delete_article_with_valid_data(self):
        article = Article.objects.get(title=MOCK_ARTICLE['title'])
        uri = '/blog/article/%d/' % article.id
        self.status_code_test(uri, 200, 'DELETE')

    def test_sequential_article(self):
        self.list_article()
        self.create_article_with_invalid_data()
        self.create_article_with_valid_data()
        self.update_article_with_invalid_data()
        self.update_article_with_valid_data()
        self.delete_article_with_invalid_data()
        self.delete_article_with_valid_data()
