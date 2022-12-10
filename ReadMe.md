# Hotel management program

This program allows users to manage a hotel by checking the availability of rooms and booking rooms.

## Installation

To use this program, you will need to have Python 3 installed on your computer.

## Usage

To use this program, first create a `Hotel` object with a name and a list of `Room` objects:

### Create a list of rooms for the hotel
room1 = Room("Room 1", True) <br>
room2 = Room("Room 2", True)<br>
room3 = Room("Room 3", False)<br>
rooms = [room1, room2, room3]<br>

### Create a hotel object
hotel = Hotel("My Hotel", rooms)<br>

Then, you can use the `checkAvailability` and `bookRoom` methods to check the availability of a room and book a room, respectively:<br>

### Check the availability of a room
room = input("Enter the name of the room: ")<br>
availability = hotel.checkAvailability(room)<br>
if availability == None:<br>
    print("Sorry, this room does not exist in our hotel.")<br>
elif availability:<br>
    print("This room is available.")<br>
else:<br>
    print("Sorry, this room is not available.")<br>

### Book a room
room = input("Enter the name of the room you would like to book: ")<br>
booking = hotel.bookRoom(room)<br>
if booking == None:<br>
    print("Sorry, this room does not exist in our hotel.")<br>
elif booking:<br>
    print("Congratulations, your booking was successful!")<br>
else:<br>
    print("Sorry, this room is not available.")<br>


## License

This program is licensed under the [MIT License](/LICENSE).
