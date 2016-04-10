import statevalidation

i = raw_input('Enter state abbreviation:')
print statevalidation.fromUSPS(i)

i = raw_input('Enter state name:')
print statevalidation.toUSPS(i)

i = raw_input('Enter county:')
print statevalidation.countyToState(i)

i = raw_input('Enter state abbreviation:')
print statevalidation.countiesInState(i)
