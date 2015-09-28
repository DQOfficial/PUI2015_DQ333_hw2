__author__ = 'Dan'
import json
import sys
import requests

# key = 1afa2d30-e80a-4ab4-9172-ls7b6bf2bdabb8
# busline = b38

key = sys.argv[1] # enter the URL
busLine = sys.argv[2] # enter the bus line number
url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (key,busLine)
request = requests.get(url)
data = request.json()

# start the bus counter at zero
buscount = 0
eachbus = data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]
#bus = eachbus[4]

for bus in eachbus:
    buscount += 1
    print "Bus #:",buscount, "Bus Latitude:",bus["MonitoredVehicleJourney"]["VehicleLocation"][u"Latitude"], "Bus Longitude:",bus["MonitoredVehicleJourney"]["VehicleLocation"][u"Longitude"]

with open(file,'wb') as csvfile:
    writer = csv.writer(csvfile)
    headers = ['Latitude']['Longitude']['Stop Name']['Stop Status']
    writer.writerow(headers)

#print "\nCurrent Bus Line:",busLine
print "\nNumber of active buses:",buscount

