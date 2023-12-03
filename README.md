# trending-FIFA-players

## Problem statements
This is a repository of web scrapping using selenium from [this website](https://sofifa.com/players).<br/>
It scrapped 3000 trending FIFA players' data. We tried to understand:
  1. Which country has how many players on the trending FIFA players website and what is the total value?
  2. Who are the top players in the trending sheet?
  3. PLayers of which age have good stats?
  4. Which players are ruling in the trending player's list?
  5. Top clubs having the most valued players in the trending list?
     
You can visit the Tableau public dashboards [Analysing players in respect of their clubs](https://public.tableau.com/app/profile/md.kabin.hasan.kanchon/viz/TrendingFIFAplayersanalysis/Dashboard1) and [Analysing players in respect of their national teams](https://public.tableau.com/views/TrendingFIFAplayersanalysis/Dashboard2?:language=en-GB&:display_count=n&:origin=viz_share_link) to see the analyses.

## Findings and Observations from the Dashboard
[Analysing players in respect of their clubs](https://public.tableau.com/app/profile/md.kabin.hasan.kanchon/viz/TrendingFIFAplayersanalysis/Dashboard1):
  1. From the bar chart, we can see the top 20 players according to their overalls. They are in different colours in respect of their current clubs.
  2. From the pie chart, we find out that Real Madrid has the most valuable players. And also the other clubs and their values that are on the top list.
  3. From the density graph, we can see that approximately players between 20-33 years old have better stats than others.
  4. The bubble graph shows the top 20 young players (18-25 years old) and their value comparison. They are also coloured according to their current clubs.
     
[Analysing players in respect of their national teams](https://public.tableau.com/views/TrendingFIFAplayersanalysis/Dashboard2?:language=en-GB&:display_count=n&:origin=viz_share_link):
  1. From the first bar chart, we can see that Spain has the most value and England has the most number of players. The bar chart shows the national team rankings by the total value in the trending list. It also shows the total number of players on the list.
  2. From the graphical graph, we can find out each country's values and total number of players by their spatial position.
  3. From the last bar chart, we can see the same top player rankings but coloured concerning national teams.
  

## Build From Sources and Run the Selenium Scraper
1. Clone the repository
```bash
git clone https://github.com/kavinh07/Trending-Fifa-Players-Webscrapping.git
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
python Fifa_Players_Webscrapping/fifa_players_scrapper.py
```
6. You will get a file named `trending_football_players.xlsx` containing all the required fields. 
Alternatively, check our scraped data [here](https://github.com/kavinh07/Trending-Fifa-Players-Webscrapping/blob/main/Fifa_Players_Webscrapping/trending_football_players.xlsx).
