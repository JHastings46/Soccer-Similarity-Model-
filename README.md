## Project Readme: Finding Similar Soccer Players (MLS Edition)

This project is a **Soccer Player Similarity Model** designed specifically for **Major League Soccer (MLS)** data from FBref. Its main goal is to help soccer teams find new players who play a lot like their current stars or specific targets.

### What does it do?

Imagine you have a great player and you want to find others who have a similar playing style, or perhaps a younger version of them. This model helps with that by:

1.  **Collecting Player Data**: It gathers all sorts of statistics (goals, assists, minutes played, shots, etc.) for MLS players from different FBref tables.
2.  **Cleaning and Combining**: It cleans up this data, removes duplicates, and combines it into one comprehensive record for each player-season.
3.  **Assigning Roles**: It smartly categorizes each player into a specific role like 'striker', 'winger', 'central midfielder', etc., so you're always comparing apples to apples (e.g., a striker to another striker, not a defender).
4.  **Measuring Similarity**: It compares players based on key statistics that are important for their specific role. The more similar their stats, the higher their 'similarity score'.
5.  **Adjusting for Experience**: Players who haven't played many minutes might have stats that look extreme by chance. The model adjusts these stats to be more realistic, so it doesn't get tricked by small sample sizes.
6.  **Highlighting Uncertainty**: It tells you how confident it is in its comparison. A player with lots of minutes played will have a 'Low' uncertainty, meaning their stats are more reliable. Someone with fewer minutes might have 'High' uncertainty.
7.  **Recruitment Filters**: You can tell the model to focus on players within a certain age range or with a minimum number of minutes, making the results more practical for scouting.

### How to use the results?

The model outputs a list of players most similar to your target player. For each similar player, you get:

*   **Similarity Score**: How closely they match your target player's style (closer to 1.0 is more similar).
*   **Uncertainty Band**: How reliable their stats are (Low, Medium, High).
*   **Fit Bucket**: Categorizes candidates (e.g., 'younger alternative', 'upside bet', 'standard match').
*   **Strengths/Weaknesses**: A quick summary of how they compare to your target player in key areas (e.g., 'above target in goals', 'below target in assists').

This project helps scouts and recruiters make more informed decisions by providing a structured, data-driven way to identify potential new talent, considering not just raw stats but also context like player role, experience, and potential.
