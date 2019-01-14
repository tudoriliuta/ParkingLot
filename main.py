class ParkingLot(object):

    def __init__(self, commands: str, first_ticket_number: int = 5000, parking_lot_size: int = 10):
        # Counter set to 5k by default.
        self.counter = first_ticket_number
        self.parking_lot_size = parking_lot_size

        # Save as a dictionary. Keys will serve as the parking space number, from 0 to 9.
        # Alternatively, could have used two lists, one for the car name and one for the ticket number.
        # Or a dictionary with insertions to the beginning.
        self.parking_lot = {i: '' for i in range(0, self.parking_lot_size)}

        # Command list cleaning and split.
        self.commands = [c for c in commands.replace(' ', '').split(';') if c != '']
        self.cars = []

    def __new__(cls, commands: str, first_ticket_number: int = 5000, parking_lot_size: int = 10):
        """
        Returns an instance of its own class, ParkingLot
        """

        instance = super(ParkingLot, cls).__new__(cls)
        instance.__init__(commands, first_ticket_number, parking_lot_size)

        instance.process_commands()

        parked_cars = instance.return_cars()

        return parked_cars

    def process_commands(self):
        # Processes sequence of commands.
        for c in self.commands:
            if c[0] == 'p':
                # Parks the car in the closest place to the exit.
                self.park(c[1:])

            elif c[0] == 'u':
                # Removes the car name from the parking lot.
                self.unpark(c[1:])

            elif c[0] == 'c':
                # Checks command purity.
                try:
                    assert len(c) == 1
                except AssertionError:
                    raise ValueError(f"ERROR: Given command for compacting the parking lot is not correct. Should be 'c' not '{c}'")

                # Compacts parking lot.
                self.compact()

            else:
                raise NotImplementedError('ERROR: Command not recognised.')

    def return_cars(self):
        # Returns parked cars sorted by proximity to exit.
        return ', '.join([c['car'] if isinstance(c, dict) else '' for c in self.parking_lot.values()])

    def park(self, car_name: str):
        # Adds a car to the position in the parking lot closer to 0.
        if car_name in self.cars:
            print(f'WARNING: Car {car_name} already parked at position {duplicates[0]}. Skipping command')
        else:
            # Park the car.
            for key, value in self.parking_lot.items():
                if value == '':
                    self.parking_lot[key] = {'car': car_name, 'ticket': self.counter}
                    self.counter += 1
                    # Keep track of parked car names.
                    self.cars.append(car_name)
                    break

    def unpark(self, ticket_number: str):
        # remove car from parking lot
        try:
            int(ticket_number)
        except ValueError:
            raise ValueError('ERROR: Ticket number is not a number')

        if len(self.cars) == 0:
            raise ValueError('ERROR: No cars to unpark.')
        else:
            for key, value in self.parking_lot.items():
                if isinstance(value, dict):
                    if value['ticket'] == int(ticket_number):
                        # Clear the space
                        self.parking_lot[key] = ''
                        # Remove car from the list of parked cars.
                        self.cars.remove(value['car'])
                        break

    def compact(self):
        # Move all cars closer to the exit.
        parked_cars = [car for i, car in self.parking_lot.items() if isinstance(car, dict)]

        # Returns the parking lot dictionary of size 'size'
        self.parking_lot = {i: '' for i in range(0, self.parking_lot_size)}

        for i, car in enumerate(parked_cars):
            # Recreate parking lot.
            self.parking_lot[i] = car
