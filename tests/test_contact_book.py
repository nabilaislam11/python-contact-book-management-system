"""Regression tests for the Contact Book command-line modules."""
import contextlib
import io
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import add_contacts
import delete_all_contact
import load_contacts
import save_contacts
import search_contacts
import update_contacts
import view_all_contacts


class ContactBookTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.old_dir = os.getcwd()
        os.chdir(self.temp_dir.name)

    def tearDown(self):
        os.chdir(self.old_dir)
        self.temp_dir.cleanup()

    @staticmethod
    def sample():
        return {"name": "Nabila", "email": "nabila@example.com", "phone": "01700000000", "address": "Dhaka"}

    def test_save_load_round_trip(self):
        expected = [self.sample()]
        save_contacts.save_to_file(expected)
        self.assertEqual(load_contacts.load_all_contacts(), expected)

    def test_empty_contact_list(self):
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(load_contacts.load_all_contacts(), [])
            view_all_contacts.view_contacts([])

    def test_add_contact_persists(self):
        answers = ["Nabila", "nabila@example.com", "01700000000", "Dhaka"]
        with patch("builtins.input", side_effect=answers), contextlib.redirect_stdout(io.StringIO()):
            contacts = add_contacts.add_contactss([])
        self.assertEqual(len(contacts), 1)
        self.assertEqual(load_contacts.load_all_contacts(), contacts)

    def test_duplicate_phone_is_rejected(self):
        existing = [self.sample()]
        with patch("builtins.input", side_effect=["Other", "other@example.com", "01700000000"]), contextlib.redirect_stdout(io.StringIO()):
            results = add_contacts.add_contactss(existing)
        self.assertEqual(results, existing)
        self.assertEqual(len(results), 1)

    def test_update_contact_persists(self):
        contacts = [self.sample()]
        answers = ["1", "Borno", "", "", "Chattogram"]
        with patch("builtins.input", side_effect=answers), contextlib.redirect_stdout(io.StringIO()):
            update_contacts.update_contactss(contacts)
        loaded = load_contacts.load_all_contacts()
        self.assertEqual(loaded[0]["name"], "Borno")
        self.assertEqual(loaded[0]["address"], "Chattogram")

    def test_search_by_name(self):
        result = io.StringIO()
        with patch("builtins.input", return_value="nabila"), contextlib.redirect_stdout(result):
            search_contacts.search_contacts([self.sample()])
        self.assertIn("nabila@example.com", result.getvalue())

    def test_delete_contact_persists(self):
        contacts = [self.sample()]
        save_contacts.save_to_file(contacts)
        with patch("builtins.input", return_value="1"), contextlib.redirect_stdout(io.StringIO()):
            delete_all_contact.delete_contactss(contacts)
        self.assertEqual(load_contacts.load_all_contacts(), [])


if __name__ == "__main__":
    unittest.main()
