# Hotel management program

This program allows users to manage a hotel by checking the availability of rooms and booking rooms.

## Installation

To use this program, you will need to have Python 3 installed on your computer.

## Usage

To use this program, first create a `Hotel` object with a name and a list of `Room` objects:

### Create a list of rooms for the hotel
room1 = Room("Room 1", True)
room2 = Room("Room 2", True)
room3 = Room("Room 3", False)
rooms = [room1, room2, room3]

### Create a hotel object
hotel = Hotel("My Hotel", rooms)


Then, you can use the `checkAvailability` and `bookRoom` methods to check the availability of a room and book a room, respectively:

### Check the availability of a room
room = input("Enter the name of the room: ")
availability = hotel.checkAvailability(room)
if availability == None:
print("Sorry, this room does not exist in our hotel.")
elif availability:
print("This room is available.")
else:
print("Sorry, this room is not available.")

### Book a room
room = input("Enter the name of the room you would like to book: ")
booking = hotel.bookRoom(room)
if booking == None:
print("Sorry, this room does not exist in our hotel.")
elif booking:
print("Congratulations, your booking was successful!")
else:
print("Sorry, this room is not available.")


## License

This program is licensed under the [MIT License](/LICENSE).
