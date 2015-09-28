__author__ = 'Dan'
import json
import sys
import requests
import urllib2
import requests
import csv


# key = 1afa2d30-e80a-4ab4-9172-7b6bf2bdabb8
# busline = b38

key = sys.argv[1] # enter the URL
busLine = sys.argv[2] # enter the bus line number
file = sys.argv[3]
url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (key,busLine)
request = requests.get(url)
data = request.json()

buscount = 0
eachbus = data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]
bus = eachbus[4]
test = bus["MonitoredVehicleJourney"]["VehicleLocation"]

for bus in eachbus:
    buscount += 1
    print "Bus #:",buscount, "Bus Latitude:",bus["MonitoredVehicleJourney"]["VehicleLocation"][u"Latitude"], "Bus Longitude:",bus["MonitoredVehicleJourney"]["VehicleLocation"][u"Longitude"]

with open(file,'wb') as csvfile:
    writer = csv.writer(csvfile)
    headers = ['Latitude','Longitude','Stop Name','Stop Status']
    writer.writerow(headers)

    for bus in eachbus:
        if bus["MonitoredVehicleJourney"]["OnwardCalls"]  == {}:
            Latitude = bus["MoitoredVehicleJourney"]["VehicleLocation"][u'Latitude']
            Longitude = bus["MonitoredVehicleJourney"]["VehicleLocation"][u'Longitude']
            stopname = "N/A"
            stopstatus = "N/A"
        else:
            stopname = bus["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"][0]["StopPointName"]
            stopstatus = bus["MonitoredVehicleJourney"]["OnwardCalls"]['OnwardCall'][0]["Extensions"]["Distances"]["PresentableDistance"]
            Latitude = bus["MonitoredVehicleJourney"]["VehicleLocation"][u'Latitude']
            Longitude = bus["MonitoredVehicleJourney"]["VehicleLocation"][u'Longitude']

        writer.writerow([Latitude,Longitude,stopname,stopstatus])

#print "\nCurrent Bus Line:",busLine
print "\nNumber of active buses:",buscount

