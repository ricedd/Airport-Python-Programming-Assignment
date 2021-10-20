import airline, airport, flight, csv
airline_dict = {}
airport_dict = {}
date_dict = {}
list1 = []
#Process CSV File
with open('flights_info.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['AIRLINE'] not in airline_dict.keys():
            airline_dict[row['AIRLINE']] = airline.Airline(row["AIRLINE"], row['AIRLINE_NAME'])

        if row['ORIGIN_AIRPORT'] not in airport_dict.keys():
            airport_dict[row['ORIGIN_AIRPORT']] = airport.Airport(row['ORIGIN_AIRPORT'], row['ORIGIN_NAME'], row['ORIGIN_CITY'], row['ORIGIN_STATE'])

        if row['DESTINATION_AIRPORT'] not in airport_dict.keys():
            airport_dict[row['DESTINATION_AIRPORT']] = airport.Airport(row['DESTINATION_AIRPORT'], row['DESTINATION_NAME'], row['DESTINATION_CITY'], row['DESTINATION_STATE'])

        flightCap = flight.Flight(int(row['YEAR']), int(row['MONTH']), int(row['DAY']), airline_dict[row['AIRLINE']], int(row['FLIGHT_NUMBER']), airport_dict[row['ORIGIN_AIRPORT']], airport_dict[row['DESTINATION_AIRPORT']], int(row['SCHEDULED_DEPARTURE']), int(row['DEPARTURE_TIME']), int(row['DEPARTURE_DELAY']), int(row['SCHEDULED_ARRIVAL']), int(row['ARRIVAL_TIME']), int(row['ARRIVAL_DELAY']))

        list1.append(flightCap)

        airline_dict[row['AIRLINE']].add_flight(flightCap)
        airport_dict[row['DESTINATION_AIRPORT']].add_dest_flight(flightCap)
        airport_dict[row['ORIGIN_AIRPORT']].add_origin_flight(flightCap)

    for n in list1:
      if n.get_date() not in date_dict.keys():
        list2=[]
        list2.append(n)
        date_dict[n.get_date()] = list2
      else:
        list2.append(n)
    
#Queries
def query1():
    for keys in date_dict:
        most = 0
        print(keys+ ":")
        for x in date_dict[keys]:
            arrivaltime = x.get_arrival_delay()
            if arrivaltime > most:
                most = arrivaltime
                correct = x
        print(correct)

def query2():
    ns = sorted(airport_dict.keys(), key=lambda x: x.lower())
    for keys in ns:
        print(airport_dict[keys])
        ddelay = 0
        odelay = 0
        for x in date_dict:
            for i in date_dict[x]:
                if i.get_departure_delay() > 15 and i.get_origin_airport().get_code() == keys:
                    odelay += 1
                elif i.get_arrival_delay() > 15 and i.get_dest_airport().get_code() == keys:
                    ddelay += 1
        print("origin delays:", odelay)
        print("destination delays:", ddelay)

def query3():
    #Process Query 3 here
    print()

#Input Output Testing - DO NOT MODIFY ANYTHING BELOW THIS LINE
testcase = input()
print(testcase)
if testcase == 'testcase 1':
    #Tests classes are created correctly
    airport1 = airport.Airport('PHX','Phoenix Sky Harbor International Airport','Phoenix','AZ')
    airport2 = airport.Airport('LAS','McCarran International Airport','Las Vegas','NV')
    airline1 = airline.Airline('WN','Southwest Airlines Co.')
    flight1 = flight.Flight(2021,2,16,airline1,'240',airport1, airport2, 1230,1235,5,215,225,10)
    airport1.add_origin_flight(flight1)
    airport2.add_dest_flight(flight1)
    airline1.add_flight(flight1)
    #Repr Functions
    print(airport1, airport2, airline1, flight1, sep='\n')
    #Airline Getter Functions
    print(airline1.get_code(), airline1.get_name(),airline1.get_flights())
    #Airport Getter Functions
    print(airport1.get_code(), airport1.get_name(), airport1.get_city(), airport1.get_state(), airport1.get_origin_flights(), airport1.get_dest_flights())
    #Flight Getter Functions
    print(flight1.get_date(),flight1.get_year(),flight1.get_month(),flight1.get_day(),flight1.get_airline(),flight1.get_flight_num(),flight1.get_origin_airport(),flight1.get_dest_airport(),flight1.get_scheduled_departure(),flight1.get_departure_time(),flight1.get_departure_delay(),flight1.get_scheduled_arrival(),flight1.get_arrival_time(),flight1.get_arrival_delay())
elif testcase == 'testcase 2':
    print(airline_dict)
    print(airport_dict)
    print(date_dict['2015-01-10'])
    if (len(set([f.get_airline() for d in date_dict.keys() for f in date_dict[d]]))) != 3:
            print("DUPLICATE AIRLINE OBJECTS")
    if (len(set([f.get_origin_airport() for d in date_dict.keys() for f in date_dict[d]]))) != 6:
            print("DUPLICATE AIRPORT OBJECTS: origin")
    if (len(set([f.get_dest_airport() for d in date_dict.keys() for f in date_dict[d]]))) != 6:
            print("DUPLICATE AIRPORT OBJECTS: destination")
elif testcase == 'testcase 3':
    query1()
elif testcase == 'testcase 4':
    query2()
elif testcase == 'testcase 5':
    query3()
else:
    fl = date_dict['2015-01-05'][0]
    for t in (fl.get_date(),fl.get_year(),fl.get_month(),fl.get_day(),fl.get_airline(),fl.get_flight_num(),fl.get_origin_airport(),fl.get_dest_airport(),fl.get_scheduled_departure(),fl.get_departure_time(),fl.get_departure_delay(),fl.get_scheduled_arrival(),fl.get_arrival_time(),fl.get_arrival_delay()):
        print(type(t))