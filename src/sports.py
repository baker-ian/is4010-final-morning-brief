import requests
from datetime import datetime, timedelta

# ESPN Public API Endpoints
SPORTS_URLS = {
    "NFL": "http://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard",
    "NBA": "http://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard",
    "MLB": "http://site.api.espn.com/apis/site/v2/sports/baseball/mlb/scoreboard",
    "NHL": "http://site.api.espn.com/apis/site/v2/sports/hockey/nhl/scoreboard"
}

def get_sports_scores(my_teams: list) -> list:
    """
    Fetches scores for Yesterday and Today for NFL, NBA, MLB, and NHL.
    Filters to only return games involving 'my_teams'.
    """
    relevant_games = []
    
    # Calculate dates: Today and Yesterday
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    
    # Format them as YYYYMMDD strings for the API
    dates_to_check = [yesterday.strftime("%Y%m%d"), today.strftime("%Y%m%d")]

    # Loop through all 4 leagues
    for league, base_url in SPORTS_URLS.items():
        # Loop through both dates (Yesterday + Today)
        for date_str in dates_to_check:
            try:
                # Add the ?dates= parameter to the URL
                url = f"{base_url}?dates={date_str}"
                
                response = requests.get(url)
                data = response.json()
                
                events = data.get("events", [])
                
                for event in events:
                    status = event.get("status", {}).get("type", {}).get("detail", "Scheduled")
                    
                    competitions = event.get("competitions", [])[0]
                    competitors = competitions.get("competitors", [])
                    
                    home_team = competitors[0].get("team", {}).get("displayName", "")
                    away_team = competitors[1].get("team", {}).get("displayName", "")
                    
                    home_score = competitors[0].get("score", "0")
                    away_score = competitors[1].get("score", "0")
                    
                    # CHECK: Is one of my teams in this game?
                    game_found = False
                    for team in my_teams:
                        if team.lower() in home_team.lower() or team.lower() in away_team.lower():
                            game_found = True
                            break
                    
                    if game_found:
                        matchup = f"{away_team} vs {home_team}"
                        score_display = f"{away_score} - {home_score}"
                        
                        # Add a visual indicator if the game is from Yesterday/Final
                        if "Final" in status:
                            date_label = "[Final]"
                        else:
                            date_label = "[Live/Today]"

                        game_info = {
                            "league": league,
                            "matchup": matchup,
                            "score": score_display,
                            "status": f"{date_label} {status}"
                        }
                        relevant_games.append(game_info)
                        
            except Exception as e:
                print(f"⚠️  Debug: Could not fetch {league} scores for {date_str}: {e}")

    return relevant_games

if __name__ == "__main__":
    # Test teams
    test_teams = ["Reds", "Bengals", "Blue Jackets", "Celtics", "Cavaliers"]
    print(get_sports_scores(test_teams))