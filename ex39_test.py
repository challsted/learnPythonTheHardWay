#!/usr/bin/env python

import hashmap

# Create a mapping of state to abbreviations
states = hashmap.new()
hashmap.set(states, 'Oregon', 'OR')
hashmap.set(states, 'Florida', 'FL')
hashmap.set(states, 'California', 'CA')
hashmap.set(states, 'New York', 'NY')
hashmap.set(states, 'Michigan', 'MI')

cities = hashmap.new()
hashmap.set(cities, 'CA', 'San Francisco')
hashmap.set(cities, 'MI', 'Detroit')
hashmap.set(cities, 'FL', 'Jacksonville')
hashmap.set(cities, 'NY', 'New York')
hashmap.set(cities, 'OR', 'Portland')

print "=" * 10
print "NY State has: %s" % hashmap.get(cities, 'NY')
print "OR State has: %s" % hashmap.get(cities, 'OR')

print "=" * 10
print "Michigan is: %s" % hashmap.get(states, 'Michigan')
print "Florida is:  %s" % hashmap.get(states, 'Florida')

print "=" * 10
print "Michigan has: %s" % hashmap.get(cities, hashmap.get(states, 'Michigan'))
print "Florida has:  %s" % hashmap.get(cities, hashmap.get(states, 'Florida'))

print "=" * 10
hashmap.list(cities)

print "=" * 10
state = hashmap.get(states, "Texas")

if not state:
    print "Sorry, no Texas."

# default values useing ||= with the nil result
# can you do  this on one lin?
city = hashmap.get(cities, "TX", "Does Not Exist")
print "The City for the stete 'TX' is: %s" % city
