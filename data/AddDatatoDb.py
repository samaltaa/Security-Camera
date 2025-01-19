import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

data = {
    #these keys represent every available angle of monitored person
    #for more accurate detection and recognition
    ["44400", "44411", "44422",
     "44433", "44444", "44455",
     "44466", "44477", "44488"
     ]: {
         "Name": "Hassan Nasrallah",
         "Relationship": "Enemy",
         "Allowed_In_Room": False,
         "Number_of_Entrances": "0",
         "Message": "Get the fuck out of my room, NOW!"
     }
}

