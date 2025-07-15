import json
from typing import Any

from requests import RequestException, Response, get
from rich import pretty

player_id: int = 1630162  # Anthony Edwards
url: str = (
    f"https://stats.nba.com/stats/playerdashboardbyyearoveryearcombined?"
    f"DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&Location=&"
    f"MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&"
    f"PerMode=PerGame&Period=0&PlayerID={player_id}&PlusMinus=N&Rank=N&"
    f"Season=2024-25&SeasonSegment=&SeasonType=Regular Season&ShotClockRange=&"
    f"VsConference=&VsDivision="
)


headers: dict[str, str] = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:140.0) Gecko/20100101 Firefox/140.0^",
    "Accept": "*/*",
    "Referer": "https://www.nba.com/",
    "Origin": "https://www.nba.com",
}


def get_player_dashboard_data(
    url: str, headers: dict[str, str]
) -> dict[str, Any]:
    response: Response = get(url, headers=headers)
    response.raise_for_status()
    return response.json()


def dump_json_to_file(data: dict[str, Any], filename: str) -> None:
    with open(filename, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    pretty.pprint(
        f'Dashboard data for player ID {player_id} saved to "{filename}" successfully ✅'
    )


if __name__ == "__main__":
    try:
        data: dict[str, Any] = get_player_dashboard_data(url, headers)
        filename: str = f"{player_id}_dashboard_data.json"

        dump_json_to_file(data, filename)
    except RequestException as e:
        print(f"An error occurred while fetching the data: {e}")
