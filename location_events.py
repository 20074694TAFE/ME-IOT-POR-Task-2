from event import Event 

class LocationEvents:

    def __init__(self, location : str):
        self.location = location
        self.eventList = []

    def tryAddEvent(self, event : Event) -> bool:
        if self.location != "" and event.location == self.location:
            if len(self.eventList) != 0:
                lastEventPresence = self.eventList[len(self.eventList)-1].presence
                if lastEventPresence != event.presence:
                    self.eventList.append(event)
                    return True
            else:
                self.eventList.append(event)
                return True
        return False


if __name__ == '__main__':
    event1 = Event()
    event2 = Event()
    print(event1)
    print(event2)
    event2.presence = True
    print(event1)
    print(event2)
    locationEvent = LocationEvents("Home")
    print(locationEvent.location)
    print(len(locationEvent.eventList))
    locationEvent.tryAddEvent(event1)
    locationEvent.tryAddEvent(event2)
    print(len(locationEvent.eventList))
    print(locationEvent.eventList[0].presence)
    print(locationEvent.eventList[1].presence)
