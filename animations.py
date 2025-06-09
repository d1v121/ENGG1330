
import time

def welcomeanimation():
    gamename =    [ "______     _               _____                _     _ _ _ ",
                    "| ___ \   | |             /  __ \              | |   | | | |",
                    "| |_/ /__ | | _____ _ __  | /  \/_ __ _   _ ___| |__ | | | |",
                    "|  __/ _ \| |/ / _ \ '__| | |   | '__| | | / __| '_ \| | | |",
                    "| | | (_) |   <  __/ |    | \__/\ |  | |_| \__ \ | | |_|_|_|",
                    "\_|  \___/|_|\_\___|_|     \____/_|   \__,_|___/_| |_(_|_|_)" ]


    gameisloading = ["Your game is loading.", "Your game is loading..", "Your game is loading..."]
    welcomelist = ["Welcome To", "Welcome To.", "Welcome To. .", "Welcome To. . ."]


    animation = [
        "[            ]",
        "[=           ]",
        "[==          ]",
        "[===         ]",
        "[====        ]",
        "[=====       ]",
        "[======      ]",
        "[=======     ]",
        "[========    ]",
        "[=========   ]",
        "[==========  ]",
        "[=========== ]",
        "[============]",

    ]



    i = 0
    for j in range(13):
        if i%len(gameisloading) == 2:
            print(" "*24, end = "\r")
            print(gameisloading[0], end = "\r")
        print(gameisloading[i%len(gameisloading)], end = "\r")
        print(gameisloading[i%len(gameisloading)] + (4-i%len(gameisloading))*" " + "Progress:" + animation[i%(len(animation))], end = "\r")
        time.sleep(0.35)
        i+=1

    print(" "*50)
    fullyloaded = "Fully Loaded! Thanks for Waiting!"
    print(f"{fullyloaded:^55}")

    time.sleep(1.5)

    for i in welcomelist:
        print(" "*20 + i, end = "\r") 
        time.sleep(0.4)

    print()


    for element in gamename:
        print(element)
        time.sleep(0.15)




    





