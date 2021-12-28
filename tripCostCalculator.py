def hawkID():
    return("lldeng")

def computeTripData(distanceK, vehSpeedMPS, vehKPL, gasCostPerLiter, breakfastCostPerDay, lunchCostPerDay, dinnerCostPerDay, hotelCostPerNight):
    vehSpeedKPH = (float(vehSpeedMPS)/1000) * 3600 #converts the vehicle's speed to kilometers per hour

    tripLengthHours = float(distanceK) / vehSpeedKPH #calculates how many hours the trip will take based on distance and speed in KPH

    gasCost = (float(distanceK) / float(vehKPL)) * float(gasCostPerLiter) #calculates the total cost of gas with the number of liters the trip will take times the cost per liter

    totalDays = int(tripLengthHours / 8) #calculates the number of days the trip will take, but truncates the last day if it is not a full day of driving. Also does not account for rest days

    if tripLengthHours % 8 != 0: #adds the last day if it was not a full 8 hour day of driving
        totalDays = totalDays + 1

    if tripLengthHours > 40 and tripLengthHours % 40 != 0:
        restDays = int(tripLengthHours / 40) #if the trip length is greater than 40 hours and does not end on a 40th hour, the number of rest days equals the integer of the trip length divided by 40.
        totalDays = totalDays + restDays #adds rest days to the total day count
    elif tripLengthHours > 40 and tripLengthHours % 40 == 0:
        restDays = int((tripLengthHours / 40) - 1) #if the trip length is greater than 40 hours and ends on a 40th hour, nubmer of rest days is reduced by one to account for the trip finishing.
        totalDays = totalDays + restDays 

    if totalDays == 0: #if the trip is 0 days, there is no breakfast
        breakfastCount = 0
    else:
        breakfastCount = totalDays - 1 #if there is an actual trip, sets breakfast equal to the number of days the trip is minus 1 for the first day

    breakfastCostTotal = breakfastCount * float(breakfastCostPerDay) #calculates the total cost of breakfasts with the number of breakfasts and the cost per day. Does not take rest days into account

    if tripLengthHours % 8 != 0:
        lastDayHours = tripLengthHours % 8 #calculates how many hours are in the last day of driving
    elif tripLengthHours % 8 == 0 and tripLengthHours >= 8:
        lastDayHours = 8 #when the last day of driving is a full 8 hours, set lastDayHours to 8
    elif tripLengthHours % 8 == 0 and tripLengthHours < 8:
        lastDayHours = 0 #when the trip has no driving, set lastDayHours to 0

    if lastDayHours > 4 or totalDays == 0: #if there are more than 4 hours in the last day of driving or the trip has 0 days of driving, count 1 lunch for every day of the trip
        lunchCount = totalDays 
    else:
        lunchCount = totalDays - 1 #otherwise, do not count the last day for lunch

    lunchCostTotal = lunchCount * float(lunchCostPerDay) #calculates the total cost of lunch
    
    if totalDays != 0:
        dinnerCount = totalDays - 1 #You eat dinner everyday except the last day
    else:
        dinnerCount = 0

    dinnerCostTotal = dinnerCount * float(dinnerCostPerDay) #calculates the total cost of dinner

    if totalDays != 0:
        hotelNights = totalDays - 1 #total hotel stays for every day of driving except the last
    else:
        hotelNights = 0

    hotelCostTotal = hotelNights * float(hotelCostPerNight) #calculates total cost of hotel stays

    totalCost = gasCost + breakfastCostTotal + lunchCostTotal + dinnerCostTotal + hotelCostTotal #adds up the cost of all expenses
    
    return tripLengthHours, gasCost, totalCost, breakfastCount, lunchCount, dinnerCount, hotelNights #returns desired values

def printTripSummary(vehName, distanceM, vehSpeedMPH, vehMPG, gasCostPerGallon, breakfastCostPerDay, lunchCostPerDay, dinnerCostPerDay, hotelCostPerNight):
    distanceK = float(distanceM) * 1.609344 #converts distance from miles to kilometers

    vehSpeedKPH = float(vehSpeedMPH) * 1.609344 #converts miles per hour to kilometers per hour
    vehSpeedMPS = (vehSpeedKPH * 1000) / 3600 #converts kilometers per hour to meters per second

    vehKPL = (float(vehMPG) * 1.609344) / 3.78541178 #converts miles per gallon to kilometers per liter

    gasCostPerLiter = float(gasCostPerGallon) / 3.78541178 #converts cost per gallon to cost per liter
    
    tripLengthHours, gasCost, totalCost, breakfastCount, lunchCount, dinnerCount, hotelNights = computeTripData(distanceK, vehSpeedMPS, vehKPL, gasCostPerLiter, breakfastCostPerDay, lunchCostPerDay, dinnerCostPerDay, hotelCostPerNight)

    tripSummaryString = f"{vehName} trip of {distanceM} miles. Hotel nights: {hotelNights}, Total cost: ${totalCost:.2f}" #creates output string
    
    print(tripSummaryString) #prints output string
    return tripSummaryString #returns output string

def testQ1():
    print(computeTripData(5700, 20, 40, 2.50, 12, 15, 20, 200))
    print(computeTripData(5760, 20, 40, 2.50, 12, 15, 20, 200))
    print(computeTripData(5800, 20, 40, 2.50, 12, 15, 20, 200))
    print(computeTripData(8640, 20, 40, 2.50, 12, 15, 20, 200))
    print(computeTripData(8700, 20, 40, 2.50, 12, 15, 20, 200))
    print(computeTripData(2880, 20, 40, 2.50, 12, 15, 20, 200))
    print(computeTripData(3000, 20, 40, 2.50, 12, 15, 20, 200))
    print(computeTripData(600, 20, 40, 2.50, 12, 15, 20, 200))
    print(computeTripData(576, 20, 40, 2.50, 12, 15, 20, 200))
    print(computeTripData(300, 20, 40, 2.50, 12, 15, 20, 200))
    print(computeTripData(288, 20, 40, 2.50, 12, 15, 20, 200))
    print(computeTripData(600, 20, 40, 2.50, 0, 15, 0, 200))
    print(computeTripData(0, 20, 40, 2.50, 12, 15, 20, 200))

def testQ2():
    printTripSummary("Bugatti", 1400.0, 100.0, 20.0, 5.0, 8.0, 12.5, 24.0, 150.0)
    printTripSummary("Camry", 2000.0, 100.0, 20.0, 5.0, 8.0, 12.5, 24.0, 150.0)
    printTripSummary("Bugatti", 1400.0, 100.0, 20.0, 5.0, 8.0, 15.5, 30.0, 150.0)
