import pandas as pd

csv_file = 'Real-Time-Match-Result-Prediction\Current_Premier_League_Player_Stats.csv'
existing_stats = pd.read_csv(csv_file)


def get_stats(url,TeamName):
    df = pd.read_html(url, attrs={"id": "stats_standard_9"})[0]
    df.columns = df.columns.droplevel(0)
    team = df
    team['Nation'] = team['Nation'].str.replace(r'[a-z]', '', regex=True)
    team['Team'] = TeamName
    team = team.drop(columns=['Matches'])
    return df
AstonVilla = get_stats("https://fbref.com/en/squads/8602292d/Aston-Villa-Stats", 'AstonVilla')
Arsenal =  get_stats("https://fbref.com/en/squads/18bb7c10/Arsenal-Stats", 'Arsenal')
Bournemouth = get_stats("https://fbref.com/en/squads/4ba7cbea/Bournemouth-Stats", 'Bournemouth')
Brentford = get_stats("https://fbref.com/en/squads/cd051869/Brentford-Stats", 'Brentford')
Brighton = get_stats("https://fbref.com/en/squads/d07537b9/Brighton-and-Hove-Albion-Stats", 'Brighton')
Chelsea = get_stats("https://fbref.com/en/squads/cff3d9bb/Chelsea-Stats", 'Chelsea')
CrystalPalace = get_stats("https://fbref.com/en/squads/47c64c55/Crystal-Palace-Stats", 'CrystalPalace')
Fulham = get_stats("https://fbref.com/en/squads/fd962109/Fulham-Stats", 'Fulham')
Liverpool = get_stats("https://fbref.com/en/squads/822bd0ba/Liverpool-Stats", 'Liverpool')
ManchesterCity = get_stats("https://fbref.com/en/squads/b8fd03ef/Manchester-City-Stats", 'ManchesterCity')
ManchesterUnited = get_stats("https://fbref.com/en/squads/19538871/Manchester-United-Stats", 'ManchesterUnited')
NewcastleUnited = get_stats("https://fbref.com/en/squads/b2b47a98/Newcastle-United-Stats", 'NewcastleUnited')
NottinghamForest = get_stats("https://fbref.com/en/squads/e4a775cb/Nottingham-Forest-Stats", 'NottinghamForest')
Southampton = get_stats("https://fbref.com/en/squads/33c895d4/Southampton-Stats", 'Southampton')
LeicesterCity = get_stats("https://fbref.com/en/squads/a2d435b3/Leicester-City-Stats", 'LeicesterCity')
IpswichTown = get_stats("https://fbref.com/en/squads/b74092de/Ipswich-Town-Stats", 'IpswichTown')
TottenhamHotspur = get_stats("https://fbref.com/en/squads/361ca564/Tottenham-Hotspur-Stats", 'TottenhamHotspur')
WestHamUnited = get_stats("https://fbref.com/en/squads/7c21e445/West-Ham-United-Stats", 'WestHamUnited')
WolverhamptonWanderers = get_stats("https://fbref.com/en/squads/8cec06e1/Wolverhampton-Wanderers-Stats", 'WolverhamptonWanderers')
Everton = get_stats("https://fbref.com/en/squads/d3fd31cc/Everton-Stats", 'Everton')


dataframes = {
    "Arsenal": Arsenal,
    "AstonVilla": AstonVilla,
    "Bournemouth": Bournemouth,
    "Brentford": Brentford,
    "Brighton": Brighton,
    "Chelsea": Chelsea,
    "CrystalPalace": CrystalPalace,
    "Everton": Everton,
    "Fulham": Fulham,
    "Liverpool": Liverpool,
    "ManchesterCity": ManchesterCity,
    "ManchesterUnited": ManchesterUnited,
    "NewcastleUnited": NewcastleUnited,
    "NottinghamForest": NottinghamForest,
    "Southampton": Southampton,
    "LeicesterCity": LeicesterCity,
    "IpswichTown": IpswichTown,
    "TottenhamHotspur": TottenhamHotspur,
    "WestHamUnited": WestHamUnited,
    "WolverhamptonWanderers": WolverhamptonWanderers
}


combined_df_list = []

for team, df in dataframes.items():
    last_two_rows = df.tail(2)
    
    last_two_rows['Team'] = team
    
    combined_df_list.append(last_two_rows)

combined_totals_df = pd.concat(combined_df_list)

combined_totals_df.reset_index(drop=True, inplace=True)

combined_df_list
teams = [
    Arsenal,
    AstonVilla,
    Bournemouth,
    Brentford,
    Brighton,
    Chelsea,
    CrystalPalace,
    Everton,
    Fulham,
    Liverpool,
    ManchesterCity,
    ManchesterUnited,
    NewcastleUnited,
    NottinghamForest,
    Southampton,
    LeicesterCity,
    IpswichTown,
    TottenhamHotspur,
    WestHamUnited,
    WolverhamptonWanderers
]


combined_df = pd.concat(teams, ignore_index=True)
updated_combined_df = combined_df[~combined_df['Player'].isin(['Squad Total', 'Opponent Total'])]

import pymysql
import pandas as pd

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='hotspurs',
    database='premier_league'
)

cursor = connection.cursor()


merged_stats = pd.merge(existing_stats, updated_combined_df, on=['Player', 'Team'], how='outer', suffixes=('_old', '_new'))


stat_columns = [col for col in merged_stats.columns if '_old' in col and col not in ['Player', 'Team']]


for index, row in merged_stats.iterrows():
    
    columns_to_update = []
    values_to_update = []
    
    for stat in stat_columns:
        stat_old = stat
        stat_new = stat.replace('_old', '_new')
        
       
        if row[stat_old] != row[stat_new]:
            column_name = stat.replace('_old', '')  # Get the actual column name (e.g., 'Goals')
            columns_to_update.append(f"{column_name} = %s")
            values_to_update.append(row[stat_new])
    
    
    if columns_to_update:
       
        values_to_update.extend([row['Player'], row['Team']])

       
        update_query = f"""
            UPDATE player_stats
            SET {', '.join(columns_to_update)}, UpdatedAt = NOW()
            WHERE PlayerName = %s AND Team = %s
        """
        
        
        cursor.execute(update_query, values_to_update)

connection.commit()
cursor.close()
connection.close()



existing_stats.update(updated_combined_df)
existing_stats.to_csv(csv_file, index=False)
