#print nega, prin posi
Age = [-1,2,-3,4,-5]

# if james exist in the array  print james cute or else james none
username = ["juan","pedro","sagaad","fuego"]

#use loop

for dataAge in Age:
    if dataAge < 0:
        print(str(dataAge) + "negative")
    elif dataAge > 0:
        print(str(dataAge) + "positive")

        for datauser in username:
            if datauser == "james":
                print("james cute ")
    else:
                print("james none")
            