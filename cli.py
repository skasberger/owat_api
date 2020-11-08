# !/usr/bin/env python
# -*- coding: utf-8 -*-
""""""
import typer
from pathlib import Path

from app.database import init_db, drop_db, import_basedata_states
from app.models import Base


app = typer.Typer()


@app.command("initdb")
def initdb_command():
    init_db(Base)
    typer.echo("Initialized the database")


@app.command("dropdb")
def dropdb_command():
    drop_db(Base)
    typer.echo("Dropped the database")


@app.command("deploy")
def deploy_command():
    typer.echo("Deployed")


@app.command("resetdb")
def resetdb_command():
    drop_db(Base)
    init_db(Base)
    typer.echo("Dataset dropped and initialized (reset)")


@app.command("import-basedata")
def import_basedata_command():
    import_basedata_states()
    # import_basedata_parties()
    # import_basedata_nonparties()
    # import_basedata_reds()
    # import_basedata_districts()
    # import_basedata_municipalities()
    typer.echo("Basedata imported")


@app.command("import-results")
def import_results_command(csv_filename: Path, json_filename: Path):
    import_result()
    typer.echo("Election results data imported")


@app.command("create-json")
def create_json_command(election: str):
    typer.echo("JSON of election {0} created".format(election))


if __name__ == "__main__":
    app()
