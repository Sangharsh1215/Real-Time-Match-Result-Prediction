# English Premier League Real-Time Match Result Prediction Model

## Overview
This project predicts the results of upcoming English Premier League (EPL) matches, focusing on each matchweek. The model runs weekly, automatically updating the dataset with new data from the latest matchweek, enhancing future predictions.

In addition to predicting match outcomes, the project includes a comprehensive analysis of player statistics. We calculate key metrics such as the **Top 5 Goal Scorers**, **Top 5 Assist Providers**, and the **Top 5 Most Creative Players**. Furthermore, we train a machine learning model that assigns a **Player Season Rating**, which updates dynamically based on weekly performances.

## Features
1. **Match Result Prediction:**
   - Predicts the outcome (home win, away win, draw) for each match in the upcoming EPL matchweek.
   - The model accounts for key factors like home team advantage, rank bias, and points bias to ensure realistic predictions.
   - Predictions are recalculated every week with updated match statistics and results.

2. **Automated Weekly Updates:**
   - The model runs at the end of every matchweek, feeding the latest match data into the dataset for continual improvement of the predictions.
   - New player and team performance data are automatically integrated into the dataset.

3. **Player Statistics Analysis:**
   - The project tracks and calculates advanced player metrics:
     - **Top 5 Goal Scorers** for the season so far.
     - **Top 5 Assist Providers** based on total assists.
     - **Top 5 Most Creative Players**, measured by key passes and chances created.
   - These rankings are updated every matchweek, providing real-time insights into player performance.

4. **Player Season Rating:**
   - A custom machine learning model generates a **Player Season Rating**, reflecting each player’s performance throughout the season.
   - The rating is updated weekly, incorporating match-by-match contributions such as goals, assists, defensive efforts, and more.

## Data Sources
- The model uses various football statistics, including match results, player performance metrics, and team standings. The primary data sources are:
  - **Match Statistics:** Updated every gameweek for all EPL matches.
  - **Player Statistics:** Detailed data for each EPL player, such as minutes played, expected goals (xG), assists (xA), progressive passes, etc.

## How It Works
1. **Match Data Integration:**
   - After each EPL matchweek, the latest match data is added to the existing dataset, providing new input for the model’s next prediction cycle.
   - Data includes detailed player and team statistics.

2. **Prediction Model:**
   - The model analyzes the past results and team statistics to predict outcomes for the upcoming matches.
   - It uses factors like home advantage, current form, and points/rank differences to produce win probabilities for each match (home win, away win, draw).

3. **Player Rating Model:**
   - A separate model evaluates individual player performances based on their contributions to each match.
   - Player ratings are updated weekly, adjusting for new performances and helping track the overall form of each player throughout the season.

## Installation & Usage

### Requirements
- Python 3.x
- Machine Learning Libraries: `scikit-learn`, `pandas`, `numpy`
- Data Visualization: `matplotlib`, `seaborn`
- Web Scraping: `BeautifulSoup`, `requests`

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/epl-match-prediction.git
