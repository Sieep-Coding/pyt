import unittest
from unittest.mock import patch, MagicMock
from frontend.gui import create_gui


class TestGUI(unittest.TestCase):

    @patch('frontend.gui.fetch_contacts')
    def test_populate_table(self, mock_fetch_contacts):
        # Mock the return value of fetch_contacts
        mock_fetch_contacts.return_value = [
            (1, "Business A", "Contact A",
             "email@example.com", "1234567890", "Active"),
            (2, "Business B", "Contact B",
             "email2@example.com", "0987654321", "Inactive"),
        ]

        mock_table = MagicMock()
        mock_table.get_children.return_value = []

        def populate_table():
            mock_table.delete(*mock_table.get_children())
            for contact in mock_fetch_contacts():
                mock_table.insert("", "end", values=contact)

        populate_table()

        mock_table.delete.assert_called_once()
        self.assertEqual(mock_table.insert.call_count, 2)

    @patch('frontend.gui.add_contact')
    def test_add_contact_window(self, mock_add_contact):
        mock_add_contact.return_value = None

        def add_contact_window():
            business_name = "Business A"
            contact_name = "Contact A"
            email = "email@example.com"
            phone = "1234567890"
            status = "Active"

            if not all([business_name, contact_name, email, phone, status]):
                raise ValueError("All fields are required.")

            mock_add_contact(business_name, contact_name, email, phone, status)

        add_contact_window()

        # Assert add_contact was called with correct arguments
        mock_add_contact.assert_called_once_with(
            "Business A", "Contact A", "email@example.com", "1234567890", "Active"
        )


if __name__ == "__main__":
    unittest.main()
