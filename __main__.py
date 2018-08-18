from credentials import Credentials

# testing

user = Credentials.fromJsonFile("credentials.json")

print (user.accountId, user.token)
