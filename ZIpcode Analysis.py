import csv

import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

app = dash.Dash()

def drawChart(height, bars, selector):
    y_pos = np.arange(len(bars))

    # Create bars
    plt.bar(y_pos, height)

    # Create names on the x-axis
    plt.xticks(y_pos, bars)

    # Show graphic
    plt.show()
    # if selector == 1:
    #     plt.savefig('plot_one.jpg', dpi = 300, format = 'jpg')
    # if selector == 2:
    #     plt.savefig('plot_two.jpg', dpi = 300, format = 'jpg')
    # if selector == 3:
    #     plt.savefig('plot_third.jpg', dpi = 300, format = 'jpg')

total = 0
    # open the csv file
with open("Data.csv", newline='') as csvfile:
    reader = csv.reader(csvfile)
    
    # create an empty dictionary
    counties = {}
    
    # read each row of the csv file
    for row in reader:
        county = row[0]  # get the county name
        zipcode = row[1]  # get the zipcode
        
        # check if the county already exists in the dictionary
        if county not in counties:
            counties[county] = []  # if not, add it
                # append the zipcode to the value list of the respective county key
        counties[county].append(zipcode)

# print the dictionary of counties and their zipcodes
height_first_bar = []

for county, zipcodes in counties.items():
    if (county != " ") and (county != "State ") and (county != "?") and (county != ""):
    # total += len(counties[county])
        total += len(counties[county])
        height_first_bar.append(county)

breakdown_num = [] #------------------------- first report
breakdown_per = []

for county, zipcodes in counties.items():
    if (county != " ") and (county != "State ") and (county != "?") and (county != ""):
    # total += len(counties[county])
        breakdown_num.append(len(counties[county]))
        breakdown_per.append(len(counties[county]) / total * 100)

height_first = breakdown_num

drawChart(height_first, height_first_bar, 1) #--------------------first chart
firstData  = {"States" : height_first_bar, "Includes" : height_first, "Rates" : breakdown_per}
firstdf = pd.DataFrame(firstData)
first_result = firstdf.to_html()
# first_report_file = open("index.html", "w")
# first_report_file.write(first_result)
# first_report_file.close()

with open("californiaZipcode.csv", newline='') as csvfile:
    reader = csv.reader(csvfile)
    
    # create an empty dictionary
    california_counties = {}
    
    # read each row of the csv file
    for row in reader:
        california_county = row[1]  # get the county name
        california_zipcode = row[0]  # get the zipcode
        
        # check if the county already exists in the dictionary
        if california_county not in california_counties:
            california_counties[california_county] = []  # if not, add it
                # append the zipcode to the value list of the respective county key
        california_counties[california_county].append(california_zipcode)
# for zipcodes, county in california_counties.items():
    # total += len(counties[county])
    # print(f"{california_counties} : {california_zipcode}")
rate_california = []
californian = counties['CA']
countylist = []
for operator_californian in californian:
    for county, zipcode in california_counties.items():
        if operator_californian in zipcode:
            countylist.append(county)
dict_county_num = {} #---------------------------------------second report----------
count_incalifor = []
rate_incalifor = []
for oper_list in countylist:
    if oper_list not in dict_county_num:
        dict_county_num[oper_list] = []
    if len(dict_county_num[oper_list]) < 2:   
        dict_county_num[oper_list].append(countylist.count(oper_list))
        dict_county_num[oper_list].append(countylist.count(oper_list)/len(countylist) * 100)
list_cities = []
rate_cities = []

for cali_county in dict_county_num.items():
    list_cities.append(cali_county[0])
    count_incalifor.append(cali_county[1][0])
    rate_cities.append(cali_county[1][1])
SecondData  = {"Counties" : list_cities, "Includes" : count_incalifor, "Rates" : rate_cities}
seconddf = pd.DataFrame(SecondData)
second_result = seconddf.to_html()


drawChart(rate_cities, list_cities, 2)

rate_of_sandiego = dict_county_num['San Diego'][1]#------------------------third report-----------------
rate_of_outof_sandiego = 100 - rate_of_sandiego

drawChart([rate_of_sandiego, rate_of_outof_sandiego], ["San Diego", "Other"], 3)

ThirdData = {"San Diego" : ["San Diego", "Others"], "Rates" : [rate_of_sandiego, rate_of_outof_sandiego]}
thirddf = pd.DataFrame(ThirdData)
third_result = thirddf.to_html()


report_file = open("index.html", "w")
report_file.write(first_result + second_result + third_result)
report_file.close()

# Create a data frame with the specified parameters

#---------------------------------heat map for california--------------------------

# Pivot the data frame so that we can plot it as a heatmap
pivoted_df = seconddf.pivot(index='Includes', columns='Counties', values='Rates')

# Set up the heatmap using seaborn
sns.set(font_scale=1.5)
sns.heatmap(pivoted_df, cmap='coolwarm', annot=True, fmt='.2f') # adjust the colors and annotation as per your requirement

# Add labels and title to the plot
plt.title('California Cities Heatmap')
plt.ylabel('')
plt.xlabel('')

# Show the plot
plt.show()
# plt.savefig('plot_three.jpg', dpi = 300, format = 'jpg')


#--------------------------------fourth report---------------------


# df = pd.read_csv(
#     "https://raw.githubusercontent.com/ThuwarakeshM/geting-started-with-plottly-dash/main/life_expectancy.csv"
# )



# fig = px.scatter(
#     df,
#     x="GDP",
#     size="Population",
#     color="continent",
#     hover_name="Country",
#     log_x=True,
#     size_max=60,
# )

# app.layout = html.Div([dcc.Graph(id="life-exp-vs-gdp", figure=fig)])

# if __name__ == "__main__":
#     app.run_server(debug=True)






