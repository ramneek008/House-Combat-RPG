from room import Room

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with a table and ornate golden decorations on each wall.");


ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.")

kitchen.link_room(dining_hall, 'South')
dining_hall.link_room(kitchen, 'North')
dining_hall.link_room(ballroom, 'West')
ballroom.link_room(dining_hall, 'East')

dining_hall.get_details()