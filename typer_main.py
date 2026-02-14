from __future__ import annotations

import random
import typer
from rich import print
from rich.console import Console
from rich.table import Table
from typing import Annotated, Dict, List, Union

data: Dict[str, Union[str, int, List[Dict[str, str]], bool]] = {
	"name": "Chris",
	"age": 31,
	"items": [{"name": "Keyboard :computer:"}, {"name": "Guitar"}],
	"active": False,
	"affiliation": "Communist",
}

console = Console()
err_console = Console(stderr=True)
app = typer.Typer()


def get_name():
	return random.choice(["Frodo", "Gandalf", "Aragorn"])


@app.command()
def main(
	dynamic_name: Annotated[
		str,
		typer.Argument(
			default_factory=get_name,
			help="The name of the user to greet",
			show_default="Think of something cool frfr",
			metavar="dynamic_name",
		),
	],
	good: Annotated[
		bool,
		typer.Argument(metavar="👍 good 👎", rich_help_panel="Secondary Arguments"),
	] = True,
	other_stuff: Annotated[
		str, typer.Argument(hidden=True, envvar=["AWESOME_NAME", "GOD_NAME"])
	] = "World",
):
	"""
	Displays a dictionary, shows a table, prints to error console.
	Says hi to NAME.
	"""
	# Displaying the data in the dictionary
	print("[bold blue]Here's the data[/bold blue]:")
	for k, v in data.items():
		if k in ["name", "age", "affiliation", "active"]:
			print(f"[bold green]{k}[/bold green]: {v}")
		elif k == "items" and isinstance(v, list):
			print(f"[bold green]{k}[/bold green]")
			for item in v:
				if isinstance(item, dict):
					item_k, item_v = next(iter(item.items()))
					print(f"  [bold red]{item_k}[/bold red]: {item_v}")
	print()

	# Displaying a table
	table = Table("Name", "Item")
	table.add_row("Frodo", "The Ring of Power")
	table.add_row("Gandalf", "Staff")
	table.add_row("Aragorn", "Sword")
	console.print(table)

	# Printing to the error console
	err_console.print("There was an error, writing to standard error")
	print()

	# Printing with bools and styles
	message_start = "everything is "
	if good:
		ending = typer.style("good", fg=typer.colors.GREEN, bold=True)
	else:
		ending = typer.style("bad", fg=typer.colors.WHITE, bg=typer.colors.RED)
	message = message_start + ending
	typer.echo(message)
	print()

	# Printing arguments with styles
	typer.secho(f"Welcome, {dynamic_name}", fg=typer.colors.MAGENTA)
	print()

	# Printing hidden variables
	if other_stuff in ["World", "Earth"]:
		typer.secho(f"Hello, {other_stuff}", fg=typer.colors.RED)


if __name__ == "__main__":
	app()
