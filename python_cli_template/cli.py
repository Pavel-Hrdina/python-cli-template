import typer
from rich import print

app = typer.Typer(help="Template cli application", add_completion=False)


@app.command()
def hello(user: str) -> None:
    """Display a greeting for the user."""
    typer.echo(f"Hello {user}")


@app.command()
def goodbye(user: str) -> None:
    """Display a farewell message for the user."""
    typer.echo(f"Goodbye {user}!")


if __name__ == "__app__":
    app()
