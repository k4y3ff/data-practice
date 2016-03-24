import math
import pandas as pd
import sqlite3

conn = sqlite3.connect("factbook.db")

facts = pd.read_sql_query("SELECT * FROM facts;", conn)
facts = facts[facts["area_land"] != 0]

def final_population(initial_population, growth_rate):
    return initial_population * (math.e ** (growth_rate / 100 * 35))
    
facts["population_2050"] = facts.apply(lambda r: final_population(r["population"], r["population_growth"]), axis=1)

# top 10 countries with highest projected populations for 2050
top_10_projected = facts.sort(columns="population_2050", ascending=False)[["name", "population_2050"]].head(10)