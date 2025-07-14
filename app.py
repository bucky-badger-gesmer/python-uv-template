import requests
from rich import pretty

url = "https://stats.nba.com/stats/playerdashboardbyyearoveryearcombined?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerID=1630162&PlusMinus=N&Rank=N&Season=2024-25&SeasonSegment=&SeasonType=Regular Season&ShotClockRange=&VsConference=&VsDivision="

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:140.0) Gecko/20100101 Firefox/140.0^",
    "Accept": "*/*",
    "Referer": "https://www.nba.com/",
    "Origin": "https://www.nba.com",
}


try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    data = response.json()
    pretty.pprint(data)

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
