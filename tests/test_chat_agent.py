import sys
import os
import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from agent import chat_agent_utils as chat_agent

@pytest.mark.parametrize(
    "user_input,expected", [
        ([("active"), ("mild"), ("mountain")], [
            ("Bali", 120, "Indonesia", "Uptown"),
            ("Paro Valley", 54, "Bhutan", "WearyTraveller"),
            ("Waikato", 89, "New Zealand", "ForestRetreat")
        ]),
        ([("lazy"), ("mild"), ("city")], [
            ("New Orleans", 28, "USA", "Relaxamax"),
            ("Edinburgh", 53, "Scotland", "CastleTown"),
            ("Rome", 25, "Italy", "WineValley"),
            ("Havana", 29, "Cuba", "Casablanca")
        ]),
        ([('active'), ('cold'), ('mountain')], [
            ('Base Marambio', 270, 'Antartica', 'IceHotel'),
            ('', 250, 'Greenland', 'NorthStar')
        ])
    ]
)
def test_retrieve_holiday_data_single_query(user_input, expected):
    """
    Given data about category, climate, terrain and star rating;
    when executed, check that the list of holidays returned is correct
    """
    user_input = user_input
    actual = chat_agent.retrieve_holiday_data(user_input)
    expected = expected
    assert actual == expected


def test_retrieve_holiday_data_no_recommendations():
    """
    Given particular data about category, climate and terrain;
    when executed, check that a standard response is returned
    """
    user_input = [('lazy'), ('hot'), ('city')]
    actual = chat_agent.retrieve_holiday_data(user_input)
    assert "Unfortunately we couldn't find any recommendations" in actual[0]
    