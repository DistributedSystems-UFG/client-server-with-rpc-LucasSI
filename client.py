import rpyc
from constRPYC import * #-

class Client:
  conn = rpyc.connect(SERVER, PORT) # Connect to the server
  print (conn.root.exposed_value())
  conn.root.exposed_append(0)       # Call an exposed operation,
  conn.root.exposed_append(4)       # and append 5 elements
  conn.root.exposed_append(3)
  conn.root.exposed_append(1)
  conn.root.exposed_append(2)
  print(conn.root.exposed_value())   # Print the result
  print(conn.root.exposed_sort()) # Print sorted list
  print(conn.root.exposed_search(1)) # Searches for value in the list
  print(conn.root.exposed_search(7))
  conn.root.exposed_insert(2, 5) # Inserts second value into list using first value as index
  print(conn.root.exposed_value())
  print(conn.root.exposed_sort())
  conn.root.exposed_remove(5) # Removes value from the list
  print(conn.root.exposed_sort())
  print(conn.root.exposed_pop(4)) # Removes value from the list and keeps only it
