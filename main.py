# Course: CS 30
# Period: 1
# Date Created: 21/02/27
# Date Last Modified: 21/02/27
# Name: Jack Anderson
# Description: Nesting items, charaters, and loctions into dictionaries


chara = {'celine': {
          'description': 'the sister of damien',
          'how_to_save': 'bring her to damien'
        },
        'damien': {
          'description': 'the brother of celine',
          'how_to_save': 'bring celine to him'
        },
        'the hacker': {
          'description': 'a rude hacker who is good with computers',
          'how_to_save': 'give him the dented camera'
        },
        'the business man': {
          'description': 'a well-dressed business man',
          'how_to_save': 'give him the pretty cane'
        },
        'the crying spirit': {
          'description': 'a spirit with permanent tear streaks and a knack ' +
          'for music',
          'how_to_save': 'give him the pretty music box'
        }}


inv_items = {'dented camera': {
              'description': 'a dented video camera,' +
              ' looks like it has been through a lot of use',
              'owner': 'the hacker'
            },
            'pretty cane': {
              'description': 'an ornate pretty cane with a claw ' +
              'holding a glass ball on the top',
              'owner': 'the business man'
            },
            'pretty music box': {
              'description': 'a small white box with ' +
              'a red stripe going up each side and' +
              'small metal crank on the one side',
              'owner': 'the crying spirit'
            }}


locations = {'security office': {
              'description': 'a dark office with a desk, ' +
              '9 computer monitors sat on the desk in a ' +
              '3x3 stack showing static'
            },
            'empty room': {
              'description': 'an empty room with nothing in it ' +
              'but dust and two doors'
            },
            'library': {
              'description': 'all the bookshelves had been push to the walls' +
              ' to make room for a small pentagram in the middle'
            },
            'music room': {
              'description': 'a room with a couple of chairs and ' +
              'filled with multiple different kinds of instruments'
            },
            'office': {
              'description': 'an office with a nice desk and ' +
              'a couple of bookshelves and filing cabinets'
            },
            'classroom': {
              'description': 'a room with one large desk and ' +
              'multiple smaller desks facing a chalk board and covered in dust'
            },
            'gym': {
              'description': 'a large gym with multiple dust-covered bleachers'
            },
            'cafeteria': {
              'description': 'a broken-down cafeteria with ' +
              'rotting tables and chairs'},
            'science lab': {
              'description': 'an old lab with rotting tables and ' +
              'shelves full of broken empty bottles'
            }}


# Print statements
for characters, chara_info in chara.items():
    print(f"\n{characters.title()} is {chara_info['description']}.")
    save = f"{chara_info['how_to_save']}"
    print(f"\t{save.title()} to save them")

for item_name, item_info in inv_items.items():
    print(f"\nInventory Item: {item_name.title()}")
    print(f"\tDescription: {item_info['description']}")
    print(f"\tOwner: {item_info['owner']}")

for loc_name, loc_info in locations.items():
    print(f"\nThe {loc_name.title()} is {loc_info['description']}.")

