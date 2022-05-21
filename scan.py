#! /usr/bin/env python
"""Scan a tree of files and extract attributes of the underlying vector or raster data."""
import sys

import typer

app = typer.Typer()


@app.command()
def eject(name: str) -> int:
    """Eject an example configuration in JSON format with stem equal to name."""
    typer.echo(f"This will eject an example configuration as {name}.json")
    return 0


@app.command()
def scan(name: str, dry_run: bool = False) -> int:
    """Scan the file system based on the configuration given in name.json and persist the report eventually."""
    if not dry_run:
        typer.echo(f"Real run changing the world following the configuration {name}.json - later ...")
        return 2
    else:
        typer.echo(f"Dry run exposing the plan of execution when following the configuration {name}.json - later ...")
        return 0

    return 1


if __name__ == "__main__":
    sys.exit(app())
