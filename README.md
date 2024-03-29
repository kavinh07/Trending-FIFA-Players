# Trending FIFA Players
This is a trending FIFA player's data analysis project where we have done web scraping using selenium from this [website](https://sofifa.com/players).
We scrapped 3000 trending FIFA players' data and stored them in an Excel sheet. There are 12 columns as given:
  - Player_name
  - Images
  - Age
  - National_team
  - Positions
  - Overall
  - Potential_overall
  - Current_club
  - Current_contract
  - Value
  - Wage
  - Total_stats </br>
  
## Problem statements
Then we have done some data processing using Python libraries like pandas and re.
By organising the data in Tableau, we tried to understand:
  1. Which country has how many players on the trending FIFA players website and what is the total value?
  2. Who are the top players in the trending sheet?
  3. PLayers of which age have good stats?
  4. Which players are ruling in the trending player's list?
  5. Top clubs having the most valued players in the trending list?
     
You can visit the Tableau Public dashboards [Player Performance Analysis in clubs](https://public.tableau.com/app/profile/md.kabin.hasan.kanchon/viz/TrendingFIFAplayersanalysis/Dashboard1) and [Player Performance Analysis in national teams](https://public.tableau.com/views/TrendingFIFAplayersanalysis/Dashboard2?:language=en-GB&:display_count=n&:origin=viz_share_link) to see the analysis.

## Findings and Observations from the Dashboard
[Player Performance Analysis in clubs](https://public.tableau.com/app/profile/md.kabin.hasan.kanchon/viz/TrendingFIFAplayersanalysis/Dashboard1):
![Player Performance Analysis in clubs image](https://github.com/kavinh07/trending-FIFA-players/blob/main/images/Player%20Performance%20Analysis%20in%20clubs.png)
  1. From the bar chart, we can see the top 20 players according to their overalls. They are in different colours in respect of their current clubs.
  2. From the pie chart, we find out that Real Madrid has the most valuable players. And also the other clubs and their values that are on the top list.
  3. From the density graph, we can see that approximately players between 20-33 years old have better stats than others.
  4. The bubble graph shows the top 20 young players (18-25 years old) and their value comparison. They are also coloured according to their current clubs.
     
[Player Performance Analysis in national teams](https://public.tableau.com/views/TrendingFIFAplayersanalysis/Dashboard2?:language=en-GB&:display_count=n&:origin=viz_share_link):
![Player Performance Analysis in national teams](https://github.com/kavinh07/trending-FIFA-players/blob/main/images/Player%20Performance%20Analysis%20in%20national%20teams.png)
  1. From the first bar chart, we can see that Spain has the most value and England has the most number of players. The bar chart shows the national team rankings by the total value in the trending list. It also shows the total number of players on the list.
  2. From the graphical graph, we can find out each country's values and total number of players by their spatial position.
  3. From the last bar chart, we can see the same top player rankings but coloured concerning national teams.
  

## Build From Sources and Run the Selenium Scraper
1. Clone the repository
```bash
git clone https://github.com/kavinh07/trending-FIFA-players.git
```
2. Initialize and activate the virtual environment
```bash
virtualenv --no-site-packages  venv
source venv/bin/activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Run the fifa_players_scrapper.py
```bash
python trending-FIFA-players/scraper.py
```
6. You will get a file named `trending_football_players.xlsx` containing all the required fields. 
Alternatively, check our scraped data [trending_football_players.xlsx](https://github.com/kavinh07/trending-FIFA-players/blob/main/data/trending_football_players.xlsx).
