# from turtle import title
# from django.test import TestCase
# from django.urls import reverse
# from .models import Book

# class BookTests(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         cls.book = Book.objects.create(
#             title="Java the complete Reference",
#             subtitle="Ninth edition",
#             author="schildt",
#             isbn="123456789JBORCL"
#         )
#     def test_book_content(self):
#         self.assertEqual(self.book.title,'Java the complete Reference')
#         self.assertEqual(self.book.subtitle,"Ninth edition")
#         self.assertEqual(self.book.author,"schildt")
#         self.assertEqual(self.book.isbn,"123456789JBORCL")
# def test_book_listview(self):
#     response = self.client.get(reverse("home"))
#     self.assertEqual(response.status_code,200)
#     self.assertEqual(response,"excellent subtitle")
#     self.assertEqual(response,"books/book_list.html")