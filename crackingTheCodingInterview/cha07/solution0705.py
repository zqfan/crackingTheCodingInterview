#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

"""Design the data structures for an online book reader system."""

class Book(object):
    def __init__(self, id, details):
        pass


class BookStore(object):
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def delete_book(self, book_id):
        for book in self.books:
            if book.id == book_id:
                index = self.books.index(book)
                del self.books[index]
                return

    def get_book(self, attrs={'id':'0'}):
        """Return a book or books satisfy attrs"""
        pass


class User(object):
    def __init__(self, id, details):
        # store the passing info
        self.book_list = []

    def read_book(self, book_id):
        # sending REST request to host
        self.book_list.append(book_id)

    def search_book(self, attrs=None):
        # sending REST request to host
        pass

    def search_user(self, attrs=None):
        # sending REST request to host
        pas


class OnlineBookReaderSystem(object):
    def __init__(self):
        self.book_store = BookStore()
        self.users = []

    def add_user(self, user):
        pass

    def delete_user(self, user):
        pass

    def get_user(self, attrs=None):
        pass

    def listen_request(self):
        pass
