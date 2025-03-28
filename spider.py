import pandas as pd

# 11 teams: 16-22

# 读取Summer文件夹中的teamid.csv
teamid = pd.read_csv("./Summer/teamid.csv")
print(teamid)
seansonid = pd.read_csv("./Summer/seasonid.csv")
print(seansonid)

# 遍历seasonid, 用seasonid和teamid拼接url
for season in range(0, 6):
    for team in range(0, 11):
        url = "http://valleybbleague.wttbaseball.pointstreak.com/team_schedule.html?" + str(teamid.iloc[team, 0]) + "&" + str(seansonid.iloc[season, 0])
        tables = pd.read_html(url)
        df = tables[0]
        df.to_csv("./Summer/" + str(seansonid.iloc[season, 1]) + "_" + str(teamid.iloc[team, 1]) + ".csv", index=False)
        print("Save " + str(seansonid.iloc[season, 1]) + "_" + str(teamid.iloc[team, 1]) + ".csv")
