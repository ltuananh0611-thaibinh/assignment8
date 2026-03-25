class Building:
    def __init__(self, bottom, top, num_elevators):
        self.elevators = []
        for i in range(num_elevators):
            self.elevators.append(Elevator(bottom, top))

    def run_elevator(self, elevator_number, destination):
        print(f"\nRunning elevator {elevator_number} to floor {destination}")
        self.elevators[elevator_number].go_to_floor(destination)