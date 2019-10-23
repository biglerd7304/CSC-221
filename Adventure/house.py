# house.py
# a House contains Rooms

from room import Room
from roomnode import RoomNode


class House:
    ''' a House contains multiple Room objects '''
    
    def __init__(self):
        ''' create the house '''
        start = Room("The Void", "You should never see this room...")
        kitchen = Room("Kitchen",".")
        bedRoom = Room("bedroom",".")
        bathRoom = Room("bathroom",".")
        livingRoom = Room("livingroom",".")
        basement = Room("basement",".")
        attic = Room("attic",".")
        
        self.rooms = [start, kitchen, bedRoom, bathRoom, livingRoom, basement, attic]
        kitchenNode = RoomNode(kitchen)
        bedRoomNode = RoomNode(bedRoom)
        bathRoomNode = RoomNode(bathRoom)
        livingRoomNode = RoomNode(livingRoom)
        basementNode = RoomNode(basement)
        atticNode = RoomNode(attic)
        
        #kitchen connection nodes
        kitchenNode.north = basementNode
        kitchenNode.south = bedRoomNode
        kitchenNode.east = bathRoomNode
        kitchenNode.southWest = livingRoomNode
        
        #bedroom connection nodes
        bedRoomNode.north = kitchenNode
        bedRoomNode.northEast = bathRoomNode
        
        #bathroom connection nodes
        bathRoomNode.west = kitchenNode
        bathRoomNode.southEast = bedRoomNode
        
        #livingroom connection nodes
        livingRoomNode.northWest = kitchenNode
        livingRoomNode.north = atticNode
        
        #basement connection nodes
        basementNode.north = kitchenNode
        
        #attic connection nodes
        atticNode.south = livingRoomNode
        
def main():
    """ test scaffold for House """
    house = House()
    for room in house:
        print(room)
        
if __name__ == "__main__":
    main()
