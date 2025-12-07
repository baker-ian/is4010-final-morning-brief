import pytest
from src.sports import get_sports_scores

# We use 'mocker' (part of pytest-mock) to fake the API call
def test_get_sports_scores_found(mocker):
    """
    Test that the function correctly parses a game when a team is found.
    """
    # 1. Define the FAKE data we want ESPN to return
    # This mimics the JSON structure of a real ESPN response
    mock_espn_data = {
        "events": [
            {
                "status": {"type": {"detail": "Final"}},
                "competitions": [{
                    "competitors": [
                        {"team": {"displayName": "Cincinnati Bengals"}, "score": "24"},
                        {"team": {"displayName": "Pittsburgh Steelers"}, "score": "10"}
                    ]
                }]
            }
        ]
    }

    # 2. Tell Python: "When requests.get is called, ALWAYS return our fake data"
    mock_response = mocker.Mock()
    mock_response.json.return_value = mock_espn_data
    mocker.patch("requests.get", return_value=mock_response)

    # 3. Run your ACTUAL function
    my_teams = ["Bengals"]
    results = get_sports_scores(my_teams)

    # 4. Check if your function did its job
    # Since your code loops through 4 leagues x 2 dates = 8 calls,
    # and our mock returns the game EVERY time, we expect to find it at least once.
    assert len(results) >= 1
    
    # Check the data integrity of the first result
    assert "Bengals" in results[0]["matchup"]
    assert "24" in results[0]["score"]