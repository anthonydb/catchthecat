general_events = [
    'The cat is on the loose!',
    'The phone\'s ringing! It\'s mom\'s sister!',
    'Can someone bring down all the laundry?!',
    'A thunderstorm is coming! Bring in the furniture!',
    'Quiet! Dad fell asleep on the couch!',
    'Ack! We are out of toilet paper again!',
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

book_quotes = [
    {'title': 'The Love Song of J. Alfred Prufrock by T.S. Eliot', 'quote': 'In the room the women come and go talking of Michelangelo.'},
    {'title': 'Pride and Prejudice by Jane Austen', 'quote': 'Angry people are not always wise.'},
    {'title': '1984 by George Orwell', 'quote': 'He who controls the past controls the future.'},
    {'title': 'The Bible', 'quote': 'Love your neighbor as yourself.'},
    {'title': 'The Great Gatsby by F. Scott Fitzgerald', 'quote': 'There is no confusion like the confusion of a simple mind.'},
    {'title': 'To Kill a Mockingbird by Harper Lee', 'quote': 'People generally see what they look for, and hear what they listen for.'}
]
