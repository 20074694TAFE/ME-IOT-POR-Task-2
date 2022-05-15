from event import Event 

class LocationEvents:
    # String
    #location = ""

    #eventList = []

    def __init__(self, location : str, eventList : list[Event] = []):
        self.location = location
        self.eventList = eventList


if __name__ == '__main__':
    event1 = Event()
    event2 = Event()
    print(event1)
    print(event2)
    event2.presence = True
    print(event1)
    print(event2)
    locationEvent = LocationEvents("Kitchen",[event1,event2])
    print(locationEvent.location)
    print(locationEvent.eventList[1])
