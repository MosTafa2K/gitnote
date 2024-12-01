import time
import typer
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.console import Console
from gitnote.gittools.tools import get_git_diff
from gitnote.commitgen.generator import commit_generator
from gitnote.utils import validate_token
from gitnote.config.settings import load_token


app = typer.Typer()
console = Console()


@app.command(name="generate", help="Generate commit messages")
def generate():
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


@app.callback()
def main():
    """✨ Welcome to gitnote: The Commit Message Geneator ✨"""
