nameOfUser = input("What is your first name?")
lengthOfUserName = len(nameOfUser)

while (lengthOfUserName < 1):
    nameOfUser = input("What is your first name?")
    lengthOfUserName = len(nameOfUser)

lastnameOfUser = input("What is your last name?")
lengthOfUserLastName = len(lastnameOfUser)

while (lengthOfUserLastName < 1):
    lastnameOfUser = input("What is your last name?")
    lengthOfUserLastName = len(lastnameOfUser)

print("The users name is %s %s" % (nameOfUser, lastnameOfUser))

friendsFirstName = input("What is your friends name?")
lengthOfFriendsFristName = len(friendsFirstName)

while (lengthOfFriendsFristName < 1):
    friendsFirstName = input("What is your friends name?")
    lengthOfFriendsFristName = len(friendsFirstName)

friendsLastName = input("What is your friends last name?")
lengthOfFriendsLastName = len(friendsLastName)

while (lengthOfFriendsFristName < 1):
    friendsLastName = input("What is your friends last name?")
    lengthOfFriendsLastName = len(friendsLastName)

print("The users name is %s %s friends name is %s %s" %
      (nameOfUser, lastnameOfUser, friendsFirstName, friendsLastName))
