import time
from typing import Annotated
import typer
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.console import Console
from gitnote.gittools.tools import get_git_diff, display_diff, ensure_git_repository
from gitnote.commitgen.generator import commit_generator
from gitnote.utils import validate_token
from gitnote.config.settings import load_token, save_token


app = typer.Typer()
console = Console()


@app.command(name="generate", help="Generate commit messages")
def generate():
    """
    Generate commit messages based on the staged changes in the Git repository.

    If no changes are found, a warning message is displayed.
    """
    pass
    token = load_token()
    if validate_token(token):
        diff = get_git_diff()
        if diff:
            with Progress(
                TextColumn("[bold blue]{task.description}"),
                SpinnerColumn("aesthetic"),
                transient=True,
            ) as progress:
                progress.add_task(description="Generating", total=None)
                time.sleep(3)
            commit_generator(diff)
        else:
            console.print(
                "⚠️ No staged changes found! Please make sure you've staged your changes using 'git add' and try again.",
                style="red",
            )


@app.command(name="diff", help="Display staged changes")
def diff():
    """Display staged changes in a pretty way"""
    display_diff()


@app.command(name="set-token", help="Set token")
def set_token(token: Annotated[str, typer.Argument()] = ""):
    """Set HuggingFace Token

    Args:
        token (str, optional): A huggingface valid token. Defaults to "".
    """
    if token:
        save_token(token)
    else:
        token = typer.prompt("Enter Token", hide_input=True)
        save_token(token)


@app.callback()
def main():
    """✨ Welcome to gitnote: The Commit Message Geneator ✨"""
    ensure_git_repository()
