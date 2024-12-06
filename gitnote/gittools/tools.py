import subprocess
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.rule import Rule

# Create a console object for rich output
console = Console()


def ensure_git_repository():
    # Check if the current directory is a Git repository
    git_path = Path(".git").resolve()
    if not git_path.exists():
        console.print(
            "[bold red]Error:[/bold red] This command must be run inside a Git repository."
        )
        exit(1)
    return True


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


def parse_diff(diff):
    # Parse the diff output into files and their changes
    """
    Parse the diff output into a dictionary with file names as keys and lists of their
    changes as values.

    Args:
        diff (str): The output of the 'git diff --cached' command.

    Returns:
        dict: A dictionary with file names as keys and lists of their changes as values.
    """
    files = {}
    current_file = None
    changes = []  # Initialize changes for the new file
    for line in diff.splitlines():
        if line.startswith("diff --git"):
            if current_file is not None:
                # Add previous file's changes to the dictionary
                files[current_file] = files.get(current_file, []) + changes
            # Set the new file name
            parts = line.split()
            current_file = parts[2][2:]  # Extract the file name
        elif current_file is not None:
            # Collect the changes for the current file
            changes.append(line)

    # Add the last file's changes to the dictionary
    if current_file is not None:
        files[current_file] = files.get(current_file, []) + changes

    return files


def style_changes(changes):
    styled_lines = []
    for line in changes:
        if line.startswith("+"):
            styled_lines.append(
                f"[bold green]{line}[/bold green]"
            )  # Positive changes (added lines)
        elif line.startswith("-"):
            styled_lines.append(
                f"[bold red]{line}[/bold red]"
            )  # Negative changes (deleted lines)
        elif line.startswith("@@"):
            styled_lines.append(f"[bold magenta]{line}[/bold magenta]")  # Hunk headers
        else:
            styled_lines.append(
                f"[dim]{line}[/dim]"
            )  # Other lines (metadata or context)
    return "\n".join(styled_lines)


def display_diff():
    diff = get_git_diff()
    if diff:
        files = parse_diff(diff)
        for file, changes in files.items():
            console.print(Rule(f"[bold cyan]File: {file}[/bold cyan]"))
            change_text = style_changes(changes)
            panel = Panel(change_text, border_style="dim", padding=(1, 2))
            console.print(panel)
    else:
        console.print("No changes to display.", style="yellow")
