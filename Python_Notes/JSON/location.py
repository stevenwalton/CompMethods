import urllib2                  
import json
from PIL import Image           # You will have to install PIL, sometimes called pillow
from pprint import pprint       # You will really want this if you are working with json.  Trust me
from cStringIO import StringIO  
# Let's give the users some information about the program
print ""
print "This program will show you a map of a location by typing in the name.  The program runs through Google APIs, so anything that Google accepts, we will accept."
print "Beware that there may be multiple places with the name.  Like 'Embry-Riddle Aeronautical University'.  You will need to add the city to get a reasonable result"
print "For example, if you want the Prescott campus, try 'Embry-Riddle Aeronautical Univerity - Prescott"
print "Do not forget the spaces and dash"
print ""
print ""
# Let's gather the point of interest
# Since we want to be able to run the code multiple times we want to include it in an infinite loop
while True:
    # We do want to only accept values that work, so we are going to use error handling.  We try to do part of code, but if it doesn't work, then we are going to catch the error with the except function and display an error message.
    try:
        name = raw_input("What location would you like to view?: ").lower()
        # Unfortunately we need turn human typing into something the computer can understand.  We want to convert our name into a url address for the Google API
        name = name.split(" ")          # This splits the name into an array of the words
        urlname = ""                    # Initialization of the url
        # We are looping the the second to last word because we don't want a plus at the end of the last word
        for x in range(0,len(name)-1):
            urlname = urlname + name[x] + "+"
        
        urlname = urlname + name[-1]    # Here's where we add that plus
        # We cleverly found the pattern that google uses for its API 
        
        # We need the json response from google to get information about the location.  If the user does not want extra information then they can just use the static map API
        url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + str(urlname)
        googleResponse = urllib2.urlopen(url)               # We need the url response from Google to get the json response
        jsonResponse = json.loads(googleResponse.read())    # Reasonable variable names
        res = 0                                             
        
        # If there is more than one location with the name the user specified we want to output the different places and address of them for the user to find
        if len(jsonResponse['results']) > 1:
            print "There are " + str(len(jsonResponse['results'])) + " locations with that name"
            # We want to make sure that the user is still doing what they are suppose to, so let's check for errors here
            try:
                response = raw_input("Would you like to display them all?(y/n): ").lower()
                if response == 'y':
                    print "The Locations are: "
                    # We want to display the locations so that the user can know what locations have the same name
                    for x in range(0,len(jsonResponse['results'])):
                            pprint(str(x) + "     " + str(jsonResponse['results'][x]['formatted_address']))
                    try:
                        res = input("Pick the numerical value of the location you'd like: ")
                    except SyntaxError:
                        # In a professional program you might not want to be sassy and give better error messages
                        print "My tiny brain can't understand what you're trying to do"

                else:
                    # If the user isn't going to choose a location, the program will be sassy
                    print "If you're not going to choose, I'm just going to pick the first location.  What are you going to do about it? That's right, nothing."
            
            except UnicodeEncodeError:
                # If you type "Google" into "Google" you can break the internet.  This is no laughing matter.  Don't even try it as a joke.
                print "JEN!!! DID YOU TYPE GOOGLE INTO GOOGLE?!  We told you that you can break the internet doing that!!!"

        # Read below why we do this
        lat = jsonResponse['results'][res]['geometry']['location']['lat']
        lng = jsonResponse['results'][res]['geometry']['location']['lng']
            
        # Since we have all this json data, we might as well give the user access to it, right?    
        response = raw_input("Would you like more information about the location?(y/n): ").lower()
        if response == 'y':   
            print "We can display: Address, Coordinates, Type, Name"
            response = raw_input("What would you like to display? (Q to quit): ").lower()
            while response != 'q':
                if response == 'q':
                    break
                # The user may want to know the address of the location they are looking at
                elif response == 'address':
                    pprint(str(jsonResponse['results'][res]['formatted_address']))
                elif response == 'coordinates':
                    pprint("The latitude is " + str(lat) + " and the longitude is " + str(lng))
                # User might be interested in HOW GOOGLE classifies the place of interest 
                elif response == 'type':
                    types = ""
        
                    for x in range(0,len(jsonResponse['results'][res]['types'])-1):
                        types = types +  str(jsonResponse['results'][res]['types'][x])
                    types = types + "," + " and " + jsonResponse['results'][res]['types'][-1]
                    pprint("This location is classified as: " + str(types))
                # Just in case the user didn't access the map location by name
                elif response == 'name':
                    pprint(str(jsonResponse['results'][res]['address_components'][0]['long_name']))
                response = raw_input("What would you like to display? (Q to quit): ").lower()
# We'll also give the user some control over the map.  Like defining the size of the image and how far to zoom        
        response = raw_input("Would you like to define the map size? Default is 800x800. (y/n): ").lower()
        if response == 'y':
            size = raw_input("Please enter size in format num1xnum2.  EX 800x800: ")
        
        else:
            size = "800x800"
        
        response = raw_input("Would you like to define zoom?  Default is 14.  (y/n): ").lower()
        if response == 'y':
            zoom = input("How much would you like to zoom.  And enhance.: ")
        
        else:
            zoom = 14
        
        # The reason we are using the latitude and longitude of the location is that we want to account for multiple locations
        mapurl = "https://maps.googleapis.com/maps/api/staticmap?center=" + str(lat) + "%2C" + str(lng) + "&size="+ str(size) +"&zoom=" + str(zoom) + "&sensor=false"
        buffer = StringIO(urllib2.urlopen(mapurl).read())
        image = Image.open(buffer)
        image.show()

    except IndexError:
        print "OH NOES!!! The tiny people in the internet wires can't find your location!!!!"

    response = raw_input("Would you like to try another location?(y/n): ").lower()
    if response == 'n':
        break 

print "Thank you, come again."
