```mermaid
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
    LocationEvents "0..*" o-- Event
    LocationEvents : +tryAddEvent(Event) boolean
```

```mermaid
sequenceDiagram
    actor U as user
    participant L as LocationEvents
    participant E as Event
    U-->>L: creates LocationEvents
    activate U
    U-->>E: creates Event
    U-->>L: runs tryAddEvent() with new Event as parameter
    activate L
    L->>E: checks if valid Event
    activate E
    E->>L: added to LocationEvents via tryAddEvent()
    deactivate E
    L->>U: tryAddEvent() returns true to indicate success
    deactivate L
    deactivate U
```