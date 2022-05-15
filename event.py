class Event:
    # String
    location = "Home"
    # String
    timestamp = "Today"
    # Boolean
    presence = False
    # Float
    sensor_temperature = 30.0

    def __str__(self):
        return "Location = " + self.location + " | Timestamp = " + self.timestamp + " | Presence = " + str(self.presence) + " | Sensor Temperature equal to: " + str(self.sensor_temperature)


if __name__ == '__main__':
    event1 = Event()
    event2 = Event()
    print(event1)
    print(event2)
    event2.presence = True
    print(event1)
    print(event2)
