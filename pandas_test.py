import pandas
heading = ["Country", "Deaths", "Births", "Year"]
data = [
    ["India", 30000, 1000, 2020],
    ["U.S", 25000, 2000, 2020],
    ["India", 50000, 100, 1983],
    ["U.S", 4000, 500, 1983],
    ["U.S", 25000, 100, 2019],
]

data2 = {
    "Country": ["India", "U.S.", "India", "U.S."],
    "Deaths": [30001, 25000, 50000, 4000],
    "Births": [1000, 2000, 100, 500],
    "Year": [2020, 2020, 1983, 1983]
}

frame = pandas.DataFrame(data,columns=heading)
#frame = pandas.DataFrame(data2)
#print(frame[["Deaths", "Country"]])
#print(frame.iloc[0])
#print(frame["Deaths"].value_counts())
print(frame["Deaths"].value_counts(normalize=True))
#print(frame.median())
#print(frame.describe())
#print(frame.quantile(0.99))
#print(frame.count())