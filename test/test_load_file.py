import unittest
from unittest.mock import mock_open, patch

from src.blueprint.markdown_server import domain


class TestLoadFile(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data="content")
    def test_load_file(self, mock_file):
        path = "some_path"
        result = domain.load_file(path)
        self.assertIsNotNone(result)
        mock_file.assert_called_once_with("content/some_path/index.md", "r")
        if result is not None:
            result.close()

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_load_file_file_not_found(self, mock_file):
        path = "not_found_path"
        result = domain.load_file(path)
        self.assertIsNone(result)
        mock_file.assert_called_once_with("content/not_found_path/index.md", "r")


if __name__ == "__main__":
    unittest.main()
