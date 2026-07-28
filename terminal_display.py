from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box

console = Console()

MATURITY_COLORS = {
    "Initial": "red",
    "Basic": "orange3",
    "Developing": "yellow",
    "Managed": "cyan",
    "Mature": "green",
}


def show_scorecard(policy_name, scorecard):
    color = MATURITY_COLORS.get(scorecard["maturity_label"], "white")
    console.print(Panel(
        f"[bold]{policy_name}[/bold]\n"
        f"Overall: [bold {color}]{scorecard['overall_pct']}% - {scorecard['maturity_label']}[/bold {color}]  "
        f"(Weighted: {scorecard['weighted_pct']}%)",
        title="GapBridge Analysis",
        border_style=color,
    ))

    table = Table(box=box.ROUNDED)
    table.add_column("NIST Function")
    table.add_column("Coverage", justify="right")
    table.add_column("Status")
    table.add_column("Controls Met", justify="right")

    for fn, data in scorecard["by_function"].items():
        pct = data["pct"]
        if pct >= 60:
            status, style = "Strong", "green"
        elif pct >= 30:
            status, style = "Moderate", "yellow"
        else:
            status, style = "Weak", "red"

        table.add_row(fn, f"{pct}%", f"[{style}]{status}[/{style}]", f"{data['met']}/{data['total']}")

    console.print(table)


def show_roadmap_summary(roadmap):
    table = Table(title="Improvement Roadmap", box=box.ROUNDED)
    table.add_column("Priority Band")
    table.add_column("Items", justify="right")

    table.add_row("Short Term (0-3 months)", str(len(roadmap["short_term_0_3_months"])))
    table.add_row("Mid Term (3-6 months)", str(len(roadmap["mid_term_3_6_months"])))
    table.add_row("Long Term (6-12 months)", str(len(roadmap["long_term_6_12_months"])))

    console.print(table)