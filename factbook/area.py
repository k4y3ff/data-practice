import sqlite3

conn = sqlite3.connect("factbook.db")
c = conn.cursor()

area_land_total = c.execute("SELECT SUM(area_land) FROM facts WHERE area_land != '';").fetchone()[0]
area_water_total = c.execute("SELECT SUM(area_water) FROM facts WHERE area_water != '';").fetchone()[0]

land_water_ratio = area_land_total / area_water_total

print(land_water_ratio)