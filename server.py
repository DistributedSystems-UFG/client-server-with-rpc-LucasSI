import rpyc
from constRPYC import *
from rpyc.utils.server import ThreadedServer

class DBList(rpyc.Service):
  def __init__(self):
    self.value = []

  def exposed_append(self, data): #appends variable data into list
    self.value = self.value + [data]
    return self.value

  def exposed_value(self): #shows list 
    return self.value

  def exposed_sort(self): #sorts list
    self.value.sort()
    return self.value

  def exposed_search(self, data): #searchs for item in list and returns boolean results
    if data in self.value:
      return True
    else:
      return False

  def exposed_insert(self, position, data): #inserts item into list
    self.value.insert(position, data)
    return self.value

  def exposed_remove(self, data): #removes item from list
    self.value.remove(data)
    return self.value

  def exposed_pop(self, data): #removes item from list and returns only it
    return self.value.pop(data)
  

if __name__ == "__main__":
  server = ThreadedServer(DBList(), port = PORT)
  server.start()
