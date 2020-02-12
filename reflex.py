def decide(track, agent, room):
    print(" ")
    print ("Your current and previous state: ")
    print(track["cur"])
    print(track["pre"])
    print(" ")
    if agent == 1 and room.lower() == "clean": 
        if track["pre"] == "2,clean":
            print("My job is done!")
            return 1
        elif track["pre"] == "none":
            print("Move right!")
            track["pre"]=track["cur"]
        elif track["pre"] != "none":
            print("Move right!")
            track["pre"]=track["cur"]
    elif agent == 1 and room.lower() == "dirty":
        print("Clean Room! ")
        track["pre"]=track["cur"]
    if agent == 2 and room.lower() == "clean": 
        if track["pre"] == "1,clean":
            print("My job is done!")
            return 1
        elif track["pre"] == "none":
            print("Move left!")
            track["pre"]=track["cur"]
        elif track["pre"] != "none":
            print("Move left!")
            track["pre"]=track["cur"]
    elif agent == 2 and room.lower() == "dirty":
        print("Clean Room! ")
        track["pre"]=track["cur"]



track = {
    "cur" : "null",
    "pre" : "none"
}
stop = 0 
while stop != 1:
    agent = int(input("What room am I in? ")) #agent is room number 
    room = raw_input("Is the room clean or dirty? ") #room is clean or dirty 
    if agent == 1:
        if room == "clean" or room == "Clean": 
            track["cur"] = "1,clean"
        elif room == "dirty" or room == "Dirty": 
            track["cur"] = "1,dirty"
    elif agent == 2:
        if room == "Clean" or room == "clean":
            track["cur"] = "2,clean"
        elif room == "Dirty" or room == "dirty":
            track["cur"] = "2,dirty"
    if decide(track,agent,room) == 1:
        stop = 1 

print(track["cur"])
print(track["pre"])
