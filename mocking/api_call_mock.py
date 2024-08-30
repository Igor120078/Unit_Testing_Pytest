import requests
import unittest
from unittest.mock import patch, Mock


# below is fake example of production api call
def get_user_data(user_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    return response.json()


class TestUserData(unittest.TestCase):
    @patch("requests.get")
    def test_get_user_data(self, mock_get):
        mock_response = Mock()
        responce_dict = {'name': 'Igor', 'email': 'igor@email.cz', 'id': 1}
        mock_response.json.return_value = responce_dict

        mock_get.return_value = mock_response

        user_data = get_user_data(1)
        mock_get.assert_called_with("https://jsonplaceholder.typicode.com/users/1")
        self.assertEqual(user_data, responce_dict)

