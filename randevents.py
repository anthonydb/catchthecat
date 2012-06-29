general_events = [
    'The cat is on the loose!',
    'The phone\'s ringing! It\'s mom\'s sister!',
    'Can someone bring down all the laundry?!',
    'A thunderstorm is coming! Bring in the furniture!',
    'We are out of toilet paper again!',
    'The AC is broken! Call the repairman!',
    'You and me? I don\'t think we\'re on the same page!',
    'Who left the toilet seat up?!'
    ]

locations_list = ['foyer', 'study', 'kitchen', 
    'living room', 'dining room', 'stairs', 
    'green living room', 'stairs', 'office', 'bedroom']

run_choices = {
	'foyer': ['kitchen','study','green living room','stairs'],
	'kitchen': ['foyer','dining room','living room','study'],
	'study': ['foyer','kitchen'],
	'green living room': ['foyer','dining room'],
	'dining room': ['kitchen', 'green living room'],
	'living room': ['kitchen'],
	'stairs': ['office','foyer','bedroom'],
	'office': ['stairs'],
	'bedroom': ['stairs']
    }
