# Morning Brief CLI 🌤️ 🏈

A command-line interface tool that delivers a personalized "Morning Briefing" directly to your terminal. It fetches current weather conditions and checks for active or recent games for your favorite sports teams, visualizing the data with beautiful terminal tables.

![Tests](https://github.com/baker-ian/is4010-final-morning-brief/actions/workflows/tests.yml/badge.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Testing](#testing)
- [AI-Assisted Development](#ai-assisted-development)
- [License](#license)

## Installation

Follow these steps to get the Morning Brief CLI running on your local machine.

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/baker-ian/is4010-final-morning-brief.git](https://github.com/baker-ian/is4010-final-morning-brief.git)
   cd is4010-final-morning-brief
   ```

2. **Create a virtual environment (recommended):**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Mac/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Setup API Key:** This application requires an API key from OpenWeatherMap to fetch weather data.
    * Get a free API Key from [OpenWeatherMap](https://openweathermap.org/)
    * Create a file named .env in the root folder.
    * Add your key to the .env file:
    ```plaintext
    WEATHER_API_KEY=your_key_here
    ```

## Usage

Run the application using the module syntax

```bash
python -m src.main [COMMAND]
```

1. **Run the Daily Brief**
The default command shows the weather in Cincinnati and sports summary for Ohio sports teams.
```bash
python -m src.main start
```

2. **Add a Sports Team**
Add a team to your tracking list. You can use full names or common parts.

```bash
python -m src.main add-sport-team "Cincinnati Bengals"
```

```bash
python -m src.main add-sport-team "Blue Jackets"
```
3. **Change Your City**
Update the location for weather reports.

```bash
python -m src.main set-city "Chicago"
```

To generate your individual daily briefing, run the application module from the root directory:

```bash
python -m src.main start
```

## Example Output

```bash
$ python -m src.main start
---- Morning Brief CLI ----
+-------------------------+
| Good Morning!           |
| Fetching data...        |
+-------------------------+

--- ⛅ Current Weather ---

 [ Weather in Cincinnati ]

 • Temp:      43.39°F
 • Condition: Broken Clouds
 • Humidity:  77%

Checking for games...
 🏈 Sports Scoreboard 🏀

+---+------------------+-------+
| L | Matchup          | Score |
+---+------------------+-------+
|NFL| CIN Bengals vs   | 14-11 |
|   | BUF Bills        | (2nd) |
+---+------------------+-------+
|NHL| CBJ Blue Jackets | 6-7   |
|   | vs FLA Panthers  | (Fin) |
+---+------------------+-------+
|NHL| CBJ Blue Jackets | 0-0   |
|   | vs WSH Capitals  | (7PM) |
+---+------------------+-------+
```

## Features

* ✅ **Real-time Weather:** Fetches live temperature and condition data via the OpenWeatherMap API.
* ✅ **Sports Updates:** Tracks scores and schedules for NFL, NBA, MLB, and NHL (Yesterday & Today).
* ✅ **Data Persistence:** Saves your favorite city and team preferences to a local JSON config file so you don't have to re-enter them.
* ✅ **Rich UI:** Utilizes the rich Python library to generate beautiful, readable terminal tables and panels.

## Testing

This project uses pytest for automated testing. To run the test suite locally:

1. Ensure your virtual environment is activated.
2. Run the following command:
    ```bash
    pytest
    ```
To see verbose output:
    ```bash
    pytest -v
    ```

## AI-Assisted Development

This project was developed with assistance from AI tools including GitHub Copilot and Gemini. For details on prompts used, debugging assistance, and code generation, see AGENTS.md.

## License

This project is licensed under the MIT License - see the LICENSE file for details.