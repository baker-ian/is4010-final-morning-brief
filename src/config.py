import json
import os
from pathlib import Path

# Define where we save the user's settings
# We use Path.home() so it saves in a standard user folder, 
# or we can just save it in the current directory for simplicity.
# For this project, let's keep it simple: current directory.
CONFIG_FILE = "user_config.json"

DEFAULT_CONFIG = {
    "city": "Cincinnati",
    "teams": ["Cincinnati Bengals", "Cincinnati Reds"],
    "units": "imperial"
}

def load_config() -> dict:
    """
    Loads the user configuration from the JSON file.
    If the file doesn't exist, it creates it with defaults.
    """
    if not os.path.exists(CONFIG_FILE):
        print(f"⚙️  Creating new config file at {CONFIG_FILE}...")
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG
    
    try:
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("⚠️  Config file is corrupted. Resetting to defaults.")
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG

def save_config(config_data: dict) -> None:
    """
    Saves the dictionary to the JSON config file.
    """
    with open(CONFIG_FILE, "w") as f:
        json.dump(config_data, f, indent=4)

def update_city(new_city: str) -> None:
    """
    Updates the city in the config.
    """
    config = load_config()
    config["city"] = new_city
    save_config(config)
    print(f"✅ City updated to: {new_city}")

def add_team(team_name: str) -> None:
    """
    Adds a team to the list if it's not already there.
    """
    config = load_config()
    if team_name not in config["teams"]:
        config["teams"].append(team_name)
        save_config(config)
        print(f"✅ Added team: {team_name}")
    else:
        print(f"ℹ️  {team_name} is already in your list.")

if __name__ == "__main__":
    # Test the module
    print("Testing config module...")
    current_conf = load_config()
    print(f"Current Config: {current_conf}")
    
    # Test updating
    # update_city("Chicago")
    # add_team("Chicago Bears")