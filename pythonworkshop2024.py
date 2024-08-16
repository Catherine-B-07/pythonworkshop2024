import os
import csv
import requests
import pandas as pd
import numpy as np

import plotly
import plotly.express as px
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib_venn

print("all packages have been imported successfully")


groupone = set(["oak", "pecan", "walnut", "bald cypress", "sycamore"])
grouptwo = set(["pecan", "walnut", "black locust", "elm"])

matplotlib_venn.venn2((groupone, grouptwo), ("Park 1 Trees", "Park 2 Trees"))

plt.show()
#function to visualize the current plot - in this case it is the venn diagram

#City of Austin tree inventory data from https://data.austintexas.gov/Locations-and-Maps/Tree-Inventory/wrik-xasw
treeinventoryrequest = requests.get("https://data.austintexas.gov/api/views/wrik-xasw/rows.csv?accessType=DOWNLOAD")
treeinventory = treeinventoryrequest.text

#Dive characteristics of Weddell seals 2014-2016 from https://dataverse.tdl.org/file.xhtml?fileId=62725&datasetVersionId=1894
sealdivedatarequest = requests.get("https://dataverse.tdl.org/api/access/datafile/62725?gbrecs=true")
sealdivedata = sealdivedatarequest.text

#2014 Survey of licensed street vendors in Sao Paulo, Brazil from
saopaulovendorsurveyrequest = requests.get("https://dataverse.tdl.org/api/access/datafile/20495?gbrecs=true")
saopaulovendorsurvey = saopaulovendorsurveyrequest.text

#prepare data from csv file
csvrows = sealdivedata.split("\n")

avgdepthlist = []
totaldistancelist = []
hourlist = []
divedurationlist = []

for i, row in enumerate(csvrows):
  values = row.split(",")
  if i < 50 and i > 0:
    hour = int(values[7])
    avgdepthm = float(values[17])
    totaldistancem = float(values[18])
    divedurationseconds = float(values[22])

    hourlist.append(hour)
    avgdepthlist.append(avgdepthm)
    totaldistancelist.append(totaldistancem)
    divedurationlist.append(divedurationseconds)


#create scatterplot
x = divedurationlist
y = avgdepthlist


plt.title('Scatter Plot of Weddell Seal Dive Duration vs. Dive Depth')
plt.xlabel('Duration (seconds)')
plt.ylabel('Avg. Depth (meters)')

figure = plt.scatter(x,y)

plt.show()

plt.savefig("scatterplot.png")

# matplotlib.pyplot.bar(avgdepthlist,  label="Average Weddell Seal Dive Depth (m)")
#create histogram using matplot

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
n, bins, patches = ax.hist(avgdepthlist, bins=10, range=(min(avgdepthlist), max(avgdepthlist)), histtype='bar')

for patch in patches:
    patch.set_facecolor('#000099')

plt.title('Histogram of Average Depths of Weddell Seal Dives')
plt.xlabel('Average Depth (m)')
plt.ylabel('Count')

plt.show()

#create histogram using plotly



#create a base for network visualization

examplegraphdata = nx.florentine_families_graph()

g = Network(height="600px", width="100%", bgcolor="#222222", font_color="white", notebook=True, cdn_resources='in_line')

g.from_nx(graphdata)

g.show("nx.html")

display(HTML('nx.html'))

#build a network visualization

g = Network(height="600px", width="100%", bgcolor="#222222", font_color="white", notebook=True, cdn_resources='in_line')

g.add_node(0, label='A')
g.add_node(1, label='B')


g.show("nx.html")

display(HTML('nx.html'))
