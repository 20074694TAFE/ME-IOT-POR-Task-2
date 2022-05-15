````mermaid
classDiagram
    class Event
    Event : +string location
    Event : +string timestamp
    Event : +bool presence
    Event : +float temperature
    Event : +__str__()
    class LocationEvents
    LocationEvents : +string location
    LocationEvents : +list~Event~ eventList
    LocationEvents : +__init__(location, eventList = [])
    LocationEvents o-- Event
```