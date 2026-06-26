# MLS Player Similarity Engine
![Python](https://img.shields.io/badge/Python-3.11-blue)
![FBref](https://img.shields.io/badge/Data-FBref-green)
![Status](https://img.shields.io/badge/Status-Live-green)

## What This Does for a Front Office

When a target player is unavailable or out of budget, 
you need the next best option fast. This tool finds 
statistically similar players across MLS by role, 
playing style, and performance level — with honest 
confidence ratings on every result.

Built specifically for MLS roster construction, 
transfer targeting, and replacement player identification.

📊 **[View Tableau Dashboard](https://public.tableau.com/app/profile/joel.hastings/viz/MLSPlayerSimilarityDashboard-MessiComparison/Dashboard1)**
⚽ **[Launch Live App](https://yipeaghbjqzz9gtwkg5gbu.streamlit.app/)**

---

## The Problem It Solves

Transfer budgets are finite. Your first choice isn't 
always available. Scouts cover a fraction of the league 
at any given time.

This system covers the entire MLS player pool 
simultaneously, compares players within their actual 
role, and flags when a result is statistically 
reliable versus when sample size makes it a risk. 
You get a shortlist you can act on, not a raw 
similarity score with no context.

---

## What Makes It Different

**Role-first comparison.** The model never compares 
a striker to a central midfielder. Every player is 
categorized by role first. Similarity is measured 
only within role, so results are tactically relevant 
from the start.

**Small sample correction.** A player with 300 minutes 
looks extreme on raw stats by chance. The model adjusts 
for this automatically and tells you how much to trust 
each result with a three-tier confidence rating.

**Recruitment filters built in.** Set age range and 
minimum minutes. The tool returns practical targets, 
not theoretical matches who are 35 years old or 
played four games.

---

## What the Tool Returns for Every Match

**Similarity score** — how closely the player's 
style matches your target (1.0 is identical)

**Confidence band** — Low, Medium, or High based 
on minutes played. Low confidence means verify 
before acting. High means the signal is real.

**Fit bucket** — Younger alternative, upside bet, 
or standard match. Tells you what kind of asset 
you're looking at.

**Strengths and gaps** — where the player exceeds 
your target and where they fall short, by key 
role-specific metrics

---

## Front Office Applications

**Transfer targeting:** Find affordable players 
whose style replicates a high-cost target before 
the window closes.

**Injury replacement:** When a key player goes 
down, generate a replacement shortlist in minutes 
rather than days.

**Draft and allocation:** Identify SuperDraft 
prospects and allocation players whose profiles 
match proven contributors already on your roster.

**Retention decisions:** Before releasing a player, 
see how hard they are to replace within budget. 
The model quantifies scarcity.

---

## Data and Method

Player data pulled from FBref across multiple 
statistical tables. Role assignment covers 
strikers, wingers, central midfielders, fullbacks, 
centerbacks, and goalkeepers. Similarity measured 
using nearest neighbor comparison on role-specific 
feature sets with Bayesian adjustment for sample 
size reliability.

---

## Author

Joel Hastings — M.S. Data Science, University of Colorado Boulder  
[LinkedIn](https://www.linkedin.com/in/joel-hastings-976bb855) | [Portfolio](https://github.com/JHastings46)
