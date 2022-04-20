class Event:
    # String
    location = "Home"
    # String
    timestamp = "Today"
    # Boolean
    presence = False
    # Float List
    sensor_values = [1.0, 2.0, 1.1]

    def __str__(self):
        return "Location = " + self.location + " | Timestamp = " + self.timestamp + " | Presence = " + str(self.presence) + " | Sensor Values are equal to: " + str(self.sensor_values)


if __name__ == '__main__':
    event1 = Event()
    event2 = Event()
    print(event1)
    print(event2)
    event2.presence = True
    print(event1)
    print(event2)
