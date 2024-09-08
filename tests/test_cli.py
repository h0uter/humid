"""Check if the cli works as intended."""

import subprocess


def test_humid_cli():
    """Can we run the help flag."""
    # Call the CLI tool using subprocess
    result = subprocess.run(
        ["hrid", "--help"], capture_output=True, text=True, check=True
    )

    # Check the exit code
    assert result.returncode == 0, "CLI tool did not exit with code 0"

    # Check that the output contains the expected help message or some part of it
    assert "usage" in result.stdout, "CLI tool did not output the expected help message"
