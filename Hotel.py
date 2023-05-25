class Room:
    def __init__(self, number, price, amenities):
        self.number = number
        self.price = price
        self.amenities = amenities
        self.reservations = []

    def is_available(self, start_date, end_date):
        for reservation in self.reservations:
            if start_date >= reservation.check_in_date and start_date < reservation.check_out_date:
                return False
            elif end_date > reservation.check_in_date and end_date <= reservation.check_out_date:
                return False
            elif start_date <= reservation.check_in_date and end_date >= reservation.check_out_date:
                return False
        return True


class StandardRoom(Room):
    def __init__(self, number, price):
        super().__init__(number, price, ["TV", "WiFi"])


class DeluxeRoom(Room):
    def __init__(self, number, price):
        super().__init__(number, price, ["TV", "WiFi", "Mini-fridge", "Balcony"])


class ReservationOperation(ABC):

    @abstractmethod
    def search_room(self, start_date, end_date, room_type):
        pass

    @abstractmethod
    def book_room(self, room, guest, start_date, end_date):
        pass

    @abstractmethod
    def view_reservation_history(self, guest):
        pass

    @abstractmethod
    def leave_feedback(self, reservation, feedback):
        pass


class Guest(ReservationOperation):
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact
        self.reservations = []

    def search_room(self, start_date, end_date, room_type):
        available_rooms = []
        for room in all_rooms:
            if isinstance(room, room_type) and room.is_available(start_date, end_date):
                available_rooms.append(room)
        return available_rooms

    def book_room(self, room, guest, start_date, end_date):
        if not room.is_available(start_date, end_date):
            return False
        reservation = Reservation(guest, room, start_date, end_date)
        room.reservations.append(reservation)
        self.reservations.append(reservation)
        return True

    def view_reservation_history(self):
        for reservation in self.reservations:
            print(f"Reservation for room {reservation.room.number} from {reservation.check_in_date} to {reservation.check_out_date}")

    def leave_feedback(self, reservation, feedback):
        if reservation in self.reservations:
            reservation.feedback = feedback
        else:
            print("Invalid reservation")


class Reservation:
    def __init__(self, guest, room, check_in_date, check_out_date):
        self.guest = guest
        self.room = room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.feedback = None


# Example usage:
all_rooms = [StandardRoom(i, 100) for i in range(101, 111)] + [DeluxeRoom(i, 200) for i in range(201, 211)]

guest1 = Guest("John Doe", "johndoe@example.com")
guest2 = Guest("Jane Doe", "janedoe@example.com")

available_rooms = guest1.search_room("2023-04-05", "2023-04-07", DeluxeRoom)
print(f"Available deluxe rooms: {[room.number for room in available_rooms]}")

reservation_made = guest1.book_room(available_rooms[0], guest1, "2023-04-05", "2023-04-07")
if reservation_made:
    print("Reservation made successfully!")
