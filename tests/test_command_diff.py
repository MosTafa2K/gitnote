from typer.testing import CliRunner
from unittest.mock import patch
from gitnote.main import app


runner = CliRunner()


@patch("gitnote.gittools.tools.get_git_diff", return_value="")
def test_main_diff_empty_stage(mock_get_git_diff):
    result = runner.invoke(app, ["diff"])
    assert result.exit_code == 0
    assert "No changes to display." in result.stdout
    mock_get_git_diff.assert_called_once()


@patch(
    "gitnote.gittools.tools.get_git_diff",
    return_value="diff --git a/test.py b/test.py\n+print('Hello')",
)
def test_main_diff_not_empty_stage(mock_get_git_diff):
    result = runner.invoke(app, ["diff"])
    assert result.exit_code == 0
    assert "File: test.py" in result.stdout
    assert "Hello" in result.stdout
    mock_get_git_diff.assert_called_once()
