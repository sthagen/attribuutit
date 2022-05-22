from scan import app
from typer.testing import CliRunner

runner = CliRunner()


def test_app():
    non_existing_command = 'uncommand'
    result = runner.invoke(app, [non_existing_command, '--city', 'Oslo'])
    assert result.exit_code == 2
    assert 'Usage: ' in result.stdout
    assert f"Error: No such command '{non_existing_command}'." in result.stdout
