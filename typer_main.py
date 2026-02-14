from __future__ import annotations

import typer
from rich import print
from typing import Dict, List, Union

data: Dict[str, Union[str, int, List[Dict[str, str]], bool]] = {
	"name": "Chris",
	"age": 31,
	"items": [{"name": "Keyboard"}, {"name": "Guitar"}],
	"active": True,
	"affiliation": "Communist",
}

app = typer.Typer()


@app.command()
def main():
	print("Here's the data")
	for k, v in data.items():
		if k == "name":
			print(f"[bold green]{k}[/bold green]: {v}")
		elif k == "age":
			print(f"[bold green]{k}[/bold green]: {v}")
		elif k == "items" and isinstance(v, list):
			print(f"[bold green]{k}[/bold green]")
			for item in v:
				if isinstance(item, dict):
					item_k, item_v = next(iter(item.items()))
					print(f"  [bold red]{item_k}[/bold red]: {item_v}")
		elif k == "active":
			if v:
				print(f"[bold green]{k}[/bold green]: True")
			else:
				print(f"[bold green]{k}[/bold green]: False")
		elif k == "affiliation":
			print(f"[bold green]{k}[/bold green]: {v}")


if __name__ == "__main__":
	app()
