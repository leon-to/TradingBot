import os
import json

class Credentials:
  def __init__(self, accountId, token):
    self.accountId = accountId
    self.token = token

  # create credentials object from the system(accoutId, token)
  #
  # @param: no argurment
  def fromEnvironment(self):
    accountId = os.environ['accountId']
    token = os.environ['token']
    return Credentials(accountId, token)

  # create credentials object from a json file
  # json file schema:
  # {
  #   accountId: ...
  #   token: ...
  # } 
  #
  # @path: relative or absolute path 
  def fromJsonFile(path):
    with open(path) as json_file:
      credentials = json.load(json_file)
    return Credentials(credentials['accountId'], credentials['token'])
      