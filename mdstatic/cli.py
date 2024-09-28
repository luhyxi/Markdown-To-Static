
from typing import Optional

from pathlib import Path

import typer

from mdstatic import ArchiveGetter

app = typer.Typer()


@app.command()
def create_main(temp_dir : Path, mock_json_file: Path) -> None:
    try:
        Getter = ArchiveGetter(temp_dir, mock_json_file) 
        Getter.create_maindir(temp_dir)
    except Exception as e:
        typer.echo(f"An error occurred while creating the main directory: {e}")
        raise typer.Exit()


def _version_callback() -> None:
    from mdstatic import __app_name__, __version__
    typer.echo(f"{__app_name__} v{__version__}")
    raise typer.Exit()

@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return