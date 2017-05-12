from unittest.mock import MagicMock
from dobjobs import dobjobs

class Test_dobjobs:
    def test_create_table(self):
        mock_cursor = MagicMock()
        dobjobs.create_table(mock_cursor)
        with open('dobjobs/schema.sql', 'r') as f:
            mock_cursor.execute.assert_called_with(f.read())
