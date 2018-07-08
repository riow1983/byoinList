import sqlite3
import pandas as pd
import folium

# db
dbname = "ihep.db"
# db connect
conn = sqlite3.connect(dbname)

# read db as pandas dataframe
df = pd.read_sql("SELECT * FROM HOSP2017", conn)

lat = df["X"]
lon = df["Y"]
name = df["医療機関名"]
docs = df["常勤医師数"]
hue = df["二次医療圏名"]

x_mean = lat.mean()
y_mean = lon.mean()


# reference: https://pythonhow.com/web-mapping-with-python-and-folium/






map = folium.Map(location = [x_mean, y_mean])
fg = folium.FeatureGroup(name="日本の医療機関")

for lt,ln,nm,dc,hu in zip(lat,lon,name,docs,hue):
	fg.add_child(folium.Marker(location=[lt,ln],
		                       popup=folium.Popup(nm)))
		                       #icon=folium.Icon(color=hu,
		                       #                 icon_color="green"))

map.add_child(fg)


map.save(outfile = "map.html")