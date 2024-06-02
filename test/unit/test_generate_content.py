import unittest
from unittest.mock import Mock, patch

from markdown_server import domain


class TestGenerateContent(unittest.TestCase):
    def test_generate_content_none_file(self):
        self.assertIsNone(domain.generate_content(None))

    @patch("frontmatter.load")
    @patch("markdown.markdown", return_value="rendered_content")
    def test_generate_content_with_file(self, mock_markdown, mock_frontmatter_load):
        mock_file = Mock()
        mock_frontmatter_file = Mock()
        mock_frontmatter_file.content = "mock_content"
        mock_frontmatter_file.metadata = {"title": "Mock Title"}
        mock_frontmatter_load.return_value = mock_frontmatter_file

        result = domain.generate_content(mock_file)

        mock_frontmatter_load.assert_called_once_with(mock_file)
        mock_markdown.assert_called_once_with(
            "mock_content", extensions=["fenced_code", "tables"]
        )
        expected_result = {"title": "Mock Title", "content": "rendered_content"}
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
