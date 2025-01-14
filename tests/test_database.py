import unittest
from unittest.mock import patch, MagicMock
import sqlite3

# Assuming the functions are in a module named `database`
from backend.database import (
    init_database,
    fetch_contacts,
    add_contact,
    update_contact,
    delete_contact,
    fetch_leads,
    add_lead,
    update_lead,
    delete_lead,
    fetch_projects,
    add_project,
    delete_project,
)


class TestDatabase(unittest.TestCase):
    @patch("sqlite3.connect")
    def test_init_database(self, mock_connect):
        mock_conn = MagicMock()
        mock_connect.return_value = mock_conn

        init_database()

        mock_connect.assert_called_once_with("business_contacts.db")
        # 3 CREATE TABLE + 3 SELECT COUNT
        self.assertEqual(mock_conn.cursor.return_value.execute.call_count, 6)
        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()

    @patch("sqlite3.connect")
    def test_fetch_contacts(self, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = mock_conn.cursor.return_value
        mock_cursor.fetchall.return_value = [
            (1, "Biz", "John Doe", "john@example.com", "1234567890", "Active")]
        mock_connect.return_value = mock_conn

        contacts = fetch_contacts()

        mock_connect.assert_called_once_with("business_contacts.db")
        mock_cursor.execute.assert_called_once_with("SELECT * FROM contacts")
        self.assertEqual(
            contacts, [(1, "Biz", "John Doe", "john@example.com", "1234567890", "Active")])
        mock_conn.close.assert_called_once()

    @patch("sqlite3.connect")
    def test_add_contact(self, mock_connect):
        mock_conn = MagicMock()
        mock_connect.return_value = mock_conn

        add_contact("Biz", "John Doe", "john@example.com",
                    "1234567890", "Active")

        mock_connect.assert_called_once_with("business_contacts.db")
        mock_conn.cursor.return_value.execute.assert_called_once_with(
            "INSERT INTO contacts (business_name, contact_name, email, phone, status) VALUES (?, ?, ?, ?, ?)",
            ("Biz", "John Doe", "john@example.com", "1234567890", "Active"),
        )
        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()

    @patch("sqlite3.connect")
    def test_update_contact(self, mock_connect):
        mock_conn = MagicMock()
        mock_connect.return_value = mock_conn

        update_contact("Biz", "Jane Doe", "jane@example.com",
                       "0987654321", "Inactive")

        mock_connect.assert_called_once_with("business_contacts.db")
        mock_conn.cursor.return_value.execute.assert_called_once_with(
            "UPDATE contacts (business_name, contact_name, email, phone, status) VALUES (?, ?, ?, ?, ?)",
            ("Biz", "Jane Doe", "jane@example.com", "0987654321", "Inactive"),
        )
        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()

    @patch("sqlite3.connect")
    def test_delete_contact(self, mock_connect):
        mock_conn = MagicMock()
        mock_connect.return_value = mock_conn

        delete_contact(1)

        mock_connect.assert_called_once_with("business_contacts.db")
        mock_conn.cursor.return_value.execute.assert_called_once_with(
            "DELETE FROM contacts WHERE id = ?", (1,))
        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()

    @patch("sqlite3.connect")
    def test_fetch_leads(self, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = mock_conn.cursor.return_value
        mock_cursor.fetchall.return_value = [
            (1, "Lead Biz", "Lead Name", "CEO", "lead@example.com", "1234567890", "New")]
        mock_connect.return_value = mock_conn

        leads = fetch_leads()

        mock_connect.assert_called_once_with("business_contacts.db")
        mock_cursor.execute.assert_called_once_with("SELECT * FROM leads")
        self.assertEqual(leads, [
                         (1, "Lead Biz", "Lead Name", "CEO", "lead@example.com", "1234567890", "New")])
        mock_conn.close.assert_called_once()

    @patch("sqlite3.connect")
    def test_add_lead(self, mock_connect):
        mock_conn = MagicMock()
        mock_connect.return_value = mock_conn

        add_lead("Lead Biz", "Lead Name", "CEO",
                 "lead@example.com", "1234567890", "New")

        mock_connect.assert_called_once_with("business_contacts.db")
        mock_conn.cursor.return_value.execute.assert_called_once_with(
            "INSERT INTO leads (business_name, contact_name, title, email, phone, status) VALUES (?, ?, ?, ?, ?, ?)",
            ("Lead Biz", "Lead Name", "CEO",
             "lead@example.com", "1234567890", "New"),
        )
        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()

    @patch("sqlite3.connect")
    def test_delete_project(self, mock_connect):
        mock_conn = MagicMock()
        mock_connect.return_value = mock_conn

        delete_project(1)

        mock_connect.assert_called_once_with("business_contacts.db")
        mock_conn.cursor.return_value.execute.assert_called_once_with(
            "DELETE FROM projects WHERE id = ?", (1,))
        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()


if __name__ == "__main__":
    unittest.main()
