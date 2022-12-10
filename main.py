# Hotel management program

# Define a class for hotel rooms
class Room:
  # Initialize the room with a name and a status (available or not available)
  def __init__(self, name, available):
    self.name = name
    self.available = available

# Define a class for the hotel
class Hotel:
  # Initialize the hotel with a name and a list of rooms
  def __init__(self, name, rooms):
    self.name = name
    self.rooms = rooms
  
  # Check the availability of a room
  def checkAvailability(self, room_name):
    # Search for the room in the list of rooms
    for room in self.rooms:
      if room.name == room_name:
        # Return the availability of the room
        return room.available
    # If the room is not found, return None
    return None
  
  # Book a room
  def bookRoom(self, room_name):
    # Search for the room in the list of rooms
    for room in self.rooms:
      if room.name == room_name:
        # If the room is available, set its availability to False
        # and return True to indicate that the booking was successful
        if room.available:
          room.available = False
          return True
        else:
          # If the room is not available, return False to indicate
          # that the booking was not successful
          return False
    # If the room is not found, return None
    return None
  
# Create a list of rooms for the hotel
room1 = Room("Room 1", True)
room2 = Room("Room 2", True)
room3 = Room("Room 3", False)
rooms = [room1, room2, room3]
print('ROOMS IN THE HOTEL:\n Room 1\n Room 2\n Room 3')
# Create a hotel object
hotel = Hotel("My Hotel", rooms)

# Check the availability of a room
room = input("Enter the name of the room: ")
availability = hotel.checkAvailability(room)
if availability == None:
  print("Sorry, this room does not exist in our hotel.")
elif availability:
  print("This room is available.")
else:
  print("Sorry, this room is not available.")

# Book a room
room = input("Enter the name of the room you would like to book: ")
booking = hotel.bookRoom(room)
if booking == None:
  print("Sorry, this room does not exist in our hotel.")
elif booking:
  print("Congratulations, your booking was successful!")
else:
  print("Sorry, this room is not available.")
