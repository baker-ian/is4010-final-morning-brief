import typer
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.table import Table  # <--- Make sure this is imported!

# Import our own modules
from src.weather import get_weather
from src.sports import get_sports_scores  # <--- Make sure this is imported!
from src.config import load_config, update_city, add_team

app = typer.Typer()
console = Console()

@app.command()
def start():
    """
    Runs the Morning Brief dashboard.
    """
    # 1. Load Settings
    config = load_config()
    city = config.get("city", "Cincinnati")
    my_teams = config.get("teams", [])
    
    console.print(Panel(f"[bold blue]Good Morning![/bold blue]\nFetching data for [bold]{city}[/bold]...", title="Morning Brief CLI"))

    # 2. Get Weather
    weather = get_weather(city)
    
    if "error" in weather:
        console.print(f"[bold red]Error:[/bold red] {weather['error']}")
    else:
        weather_display = f"""
# Weather in {weather['city']}
* **Temperature:** {weather['temp']}°F
* **Condition:** {weather['description'].title()}
* **Humidity:** {weather['humidity']}%
        """
        console.print(Panel(Markdown(weather_display), title="🌤️  Current Weather", border_style="green"))

    # 3. Get Sports
    console.print("\n[italic]Checking for games...[/italic]")
    games = get_sports_scores(my_teams)
    
    if not games:
        console.print(f"[yellow]No active games found for your teams: {', '.join(my_teams)}[/yellow]")
    else:
        # Create a nice table for sports
        table = Table(title="🏈 Sports Scoreboard 🏀")
        table.add_column("League", style="cyan")
        table.add_column("Matchup", style="magenta")
        table.add_column("Score", style="green")
        table.add_column("Status", style="yellow")

        for game in games:
            table.add_row(game["league"], game["matchup"], game["score"], game["status"])
            
        console.print(table)

@app.command()
def set_city(city_name: str):
    """
    Update the default city for the weather report.
    """
    update_city(city_name)

@app.command()
def add_sport_team(team_name: str):
    """
    Add a new sports team to track.
    """
    add_team(team_name)

if __name__ == "__main__":
    app()