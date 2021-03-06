class Airline:
    def __init__(self, c, n):
        self._code = c
        self._name = n
        self._flights = []
    
    def add_flight(self, flight):
         self._flights.append(flight)
     
    def get_code(self):
        return self._code

    def get_name(self):
        return self._name

    def get_flights(self):
        return self._flights

    def __repr__(self):
        return f'({self._code}, {self._name}, {len(self._flights)})'