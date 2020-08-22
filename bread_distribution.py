import json
import math

def save_data():
    data = {}
    data['baker'] = baker_dict
    data['receiver'] = receiver_dict
    with open(filename, 'w') as fp:
        json.dump(data, fp)

filename = 'stored_data.json'
with open(filename, 'r') as fp:
    data = json.load(fp)

baker_dict = data['baker']
receiver_dict = data['receiver']

while True:
    print("1. input baker info")
    print("2. input receiver info")
    print("3. run food distribution")
    print("4. list current bakers")
    print("5. list current receivers")
    print("6. exit")
    print("7. save records")

    choice = int(input("Please input your choice:"))
    if choice == 1:
        user_name = input("input your baker name:")
        user_long = float(input("input your longtitude:"))
        user_lat = float(input("input your latitude:"))
        user_req = int(input("input your bread available:"))
        if user_name not in baker_dict:
            baker_dict[user_name] = [user_long, user_lat, user_req]
        else:
            print("your record is updated\n")
            baker_dict[user_name] = [user_long, user_lat, user_req]
    elif choice == 2:
        user_name = input("input your receiver name:")
        user_long = float(input("input your longtitude:"))
        user_lat = float(input("input your latitude:"))
        user_req = int(input("input your bread req:"))
        if user_name not in receiver_dict:
            receiver_dict[user_name] = [user_long, user_lat, user_req]
        else:
            print("your record is updated\n")
            receiver_dict[user_name] = [user_long, user_lat, user_req]
    elif choice == 3:
        bakerList = []
        bakerLat = []
        bakerLong = []
        availBread = []
        for key in baker_dict:
            bakerList.append(key)
            bakerLong.append(baker_dict[key][0])
            bakerLat.append(baker_dict[key][1])
            availBread.append(baker_dict[key][2])
        receiverList = []
        receiverLat = []
        receiverLong = []
        requestBread = []
        for key in receiver_dict:
            receiverList.append(key)
            receiverLong.append(receiver_dict[key][0])
            receiverLat.append(receiver_dict[key][1])
            requestBread.append(receiver_dict[key][2])
        nbBakers = len(bakerList)
        nbReceivers = len(receiverList)

        for i in range(nbReceivers):
            d = 1000
            nearest = 0
            for j in range(nbBakers):
                dist = math.sqrt((bakerLong[j]-receiverLong[i])**2+(bakerLat[j]-receiverLat[i])**2)
                if dist < d and availBread[j] > requestBread[i]:
                    nearest = j
                    d = dist
            if d < 1000:
                print('Deliver ',requestBread[i],' loaves of bread from Baker', bakerList[nearest],'(', bakerLong[nearest],bakerLat[nearest],') to Receiver ',receiverList[i],'(',receiverLong[i],receiverLat[i],')')
                availBread[nearest] = availBread[nearest] - requestBread[i]
            else:
                print('No bread to be delivered to Receiver ', receiverList[i])
    elif choice == 4:
        for key in baker_dict:
            print("baker: %s, longtitude: %s, latitude: %s, bread available: %s" % \
                  (key, baker_dict[key][0], baker_dict[key][1], baker_dict[key][2]))
    elif choice ==5:
        for key in receiver_dict:
            print("receiver: %s, longtitude: %s, latitude: %s, bread request: %s" % \
                  (key, receiver_dict[key][0], receiver_dict[key][1], receiver_dict[key][2]))
    elif choice == 6:
        break
    elif choice == 7:
        print("data is saved\n")
        save_data()
print("Thanks for using JEV food services.")
save_data()
