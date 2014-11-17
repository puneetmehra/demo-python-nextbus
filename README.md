demo-python-nextbus
===================

Trivial python script that gets AC Transit route info via the NextBus API

## Overview

Python script that uses the Requests HTTP lib to query the NextBus API to get a list
of stops for a given AC Transit route

## Usage

1. clone the repo
2. python my_transit.py --route <AC_TRANSIT_ROUTE_NUMBER>
3. See all of the stops for the route dumped to stdout

All the stops for the route are available in the stops dictionary and can be used in a more
meaningful script as desired.

## Requirements

1. Requires python 2.6+
2. Requires [Requests](http://docs.python-requests.org/en/latest/)

