from room import Room
kitchen = Room ("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")


dining_hall = Room ("Dining Hall.")
dining_hall.set_description("A classy hall. With a long table in the center.")


ballroom = Room ("Ballroom")
ballroom.set_description("relaxing ball room styled with marble floor.")

kitchen.link_room(dining_hall, "south")

dining_hall.link_room(ballroom,"west")

ballroom.link_room(dining_hall, "east")

dining_hall.link_room(kitchen,"north")

dining_hall.get_details()

kitchen.get_details()

ballroom.get_details()
