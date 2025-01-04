import requests
import sqlite3

data = requests.get("https://randomuser.me/api/?results=100&inc=gender,name,location")

data = data.json()['results']

featuredData = []

for i in range(len(data)):
    row = (data[i]['gender'],  data[i]['name']['first'], data[i]['location']['coordinates']['latitude'], data[i]['location']['coordinates']['longitude'])
    featuredData.append(row)

#print(featuredData)

con = sqlite3.connect("fakeData.db")
cur = con.cursor()

for i in range(len(data)):
    cur.executemany("INSERT INTO user VALUES(?, ?, ?, ?)", featuredData)
    
#cur.execute(f"INSERT INTO user VALUES({data[i]['gender']}, '{data[i]['name']['first']}', '{data[i]['location']['coordinates']['latitude']}', {data[i]['location']['coordinates']['longitude']})")

res = cur.execute("SELECT gender, first, lat, long FROM user")
print(res.fetchall())

con.commit()
con.close()
