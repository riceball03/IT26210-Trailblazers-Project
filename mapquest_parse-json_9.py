import json
import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?" #API used
key = "GiMb7IsG3jegXilEhgmQsYJjqXaBILr1" #key used in using the API

while True:
    orig = input("Starting Location: ") #asks user for starting location
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ") #asks user for destination
    if dest == "quit" or dest == "q":
        break
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    print("URL:" + (url))
    json_data = requests.get(url).json() #retrieves data from json file
    json_status = json_data["info"]["statuscode"] #gets status code
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n") #displays status code when route call is successful
        print("============================================")
        print("Directions from " + (orig) + " to " + (dest)) #displays the start location and distance
        print("Trip Duration:  " + (json_data["route"]["formattedTime"])) #displays trip duration

        select_unit = input("Does the user want to display the information in metric or english system of measurement? ") #asks if metric or english
        if select_unit == "english":
            print("Miles:   " + str("{:.2f}".format(json_data["route"]["distance"]))) #displays distance in miles
            print("Fuel Used (Gallon):" + str("{:.2f}".format(json_data["route"]["fuelUsed"]))) #displays fuel used in gallons
        elif select_unit == "metric":
            print("Kilometers:     " + str("{:.2f}".format((json_data["route"]["distance"])*1.61))) #converts miles to km and displays it
            print("Fuel Used (Ltr):" + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78))) #converts gallon to liter and displays it
            
        print("============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1609.34) + " m)")) #converts distance to meters and displays it
        print("============================================\n")  
    elif json_status == 402:
        print("********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.") #error handling when user input is invalid
        print("********************************************\n")
    elif json_status == 611:
        print("********************************************\n")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.") #error handling when user input is blank
        print("********************************************\n")
    else:
        print("***************************************************************************")
        print("for Status Code: " + str(json_status) + "; Refer to: ")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes") #link to the list of status codes
        print("***************************************************************************\n")