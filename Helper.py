# Tuples containing elements for naming items, rooms, entities etc

Affinities = ('Chaos', 'Abyss', 'Void', 'Eldritch')
Elements = ('Water', 'Air', 'Earth', 'Fire')
Modifiers_Elemental_T1 = ('Dew', 'Whistles', 'Pebbles', 'Ashes')
Modifiers_Elemental_T2 = ('Splashes', 'Breezes', 'Boulders', 'Smoulders')
Modifiers_Elemental_T3 = ('', '', '', '')   # I ran out of ideas >.<
Modifiers_Bonus = ('Cursed', 'Blessed')
Quality = ('Broken', 'Chipped', 'Mundane', 'Tempered', 'Pristine')

# Defining colors for the 4 elements

Modifiers_Elemental_Colours = ((28, 58, 89), (244, 213, 141), (28, 89, 29), (206, 78, 55))

# Usage: Select element from tuples and parse it to generator

# Order: Quality + WEAPON_NAME + 'OF' +  Modifiers_Elemental + (Modifier_Bonus) 
                                                         # (Modifier_Bonus won't be in name of weapon, will only be seen in item specs screen)
# Example: Chipped Nodachi of Smoulders (Cursed)

# Helper function
