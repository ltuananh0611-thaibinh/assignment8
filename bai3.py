def fire_alarm(self):
    print("\nFIRE ALARM! All elevators go to bottom floor!")
    for elevator in self.elevators:
        elevator.go_to_floor(elevator.bottom)
            