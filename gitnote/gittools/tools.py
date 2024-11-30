import subprocess
from rich.console import Console

# Create a console object for rich output
console = Console()


def get_git_diff():
    """
    Executes the 'git diff --cached' command to retrieve the staged changes
    in the Git repository.

    Returns:
        str: The output of the 'git diff --cached' command if successful.
        None: If an error occurs during the execution, logs the error to
        the console and returns None.
    """
    result = subprocess.run(
        ["git", "diff", "--cached"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
    )

    if result.stderr:
        console.print(f"[bold red]Error:[/bold red] {result.stderr}")
        return None
    return result.stdout
