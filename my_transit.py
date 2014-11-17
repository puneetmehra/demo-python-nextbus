import argparse
import requests
import sys
import re

parser = argparse.ArgumentParser()

parser.add_argument('--route', dest='route', help='AC Transit route that should be queried', required=True)
args = parser.parse_args()

agency = 'actransit'
route = args.route

r = requests.get('http://webservices.nextbus.com/service/publicXMLFeed?command=routeConfig&a=%s&r=%s' % (agency, route))

if r.status_code != requests.codes.ok:
    print 'Call to get Route: %s for Agency: %s Failed. Error code %s ' % (route, agency, r.status_code)
    sys.exit(-1)

output = r.text

# all the stops for the route
stops = {}

for line in output.split('\n'):
    if 'title=' in line:
        entry = {}
        entry['route'] = route
        attrs = re.findall(r'\s?(\S+)="([^"]+)"', line)
        for attr in attrs:
            if attr[0] == 'title' or attr[0] == 'lat' or attr[0] == 'lon' or attr[0] == 'tag':
                print '%s ==> %s' % (attr[0], attr[1])
                entry[attr[0]] = attr[1]

            elif attr[0] == 'stopId':
                entry[attr[0]] = attr[1]
                stops[attr[1]] = entry


print "Done collecting stops on route: %s" % route

# dump routes
for stop_id in sorted(stops.keys()):
    stop = stops[stop_id]
    print "Route: %s | Stop ID: %s | Stop Tag: %s | Title: %s | Lat: %s | Lon: %s" % (stop['route'], stop_id, stop['tag'], stop['title'], stop['lat'], stop['lon'])
            
    
