class SinglyLinked:
    # a node class for the doubly linked list
    class Node:
      # a node class constructor that takes in data, next and sets them to the node data, next respectively
      # with next set to None by default
      def __init__(self, data, next = None):
        self.data = data
        self.next = next

      # this function returns data stored in node
      def get_data(self):
        return self.data

      # this function returns reference to next node in DoublyLinked
      def get_next(self):
        return self.next

    # initializes a doubly linked list, with front and back set to None
    def __init__(self, data = None):
      self.front = None
      self.back = None

    # returns a reference to the first data node in the list. If list is empty, function returns None
    def get_front(self):
        return self.front

    # returns a reference to the last data node in the list. If list is empty, function returns None
    def get_back(self):
        return self.back

    # adds data to the front of the list
    def push_front(self, data):
        # create a new node
        current = self.Node(data, None, None)
        # if the list is empty, set the back to the new node
        if self.front is None:
          self.back = current
        # if the list is not empty, set the front of the list to the new node
        else:
          current.next = self.front
        self.front = current

    # adds data to the back of the list
    def push_back(self,data):
        # create a new node
        current = self.Node(data, None, None)
        # if the list is empty, set the front to the new node
        if self.back is None:
          self.front = current
        # if the list is not empty, set the back of the list to the new node
        else:
          self.back.next = current
        self.back = current

    # this function removes the first data node from the list. Function returns value stored in that node
    def pop_front(self):
      # check if the list is empty
      if self.front is None:
        # raise an error if the list is empty
        raise IndexError('pop_front() used on empty list')
      else:
        # set current to the front of the list
        current = self.front
        # save the data stored in the front of the list
        data = current.get_data()
        # set the front of the list to the next node
        self.front = self.front.next
        # if the front of the list is empty, set the back to empty
        if self.front is None:
          self.back = None
        # delete the current node
        del current
        # return the data stored in the front of the list
        return data

    # this function checks if the list is empty. Function returns True if list is empty, False otherwise
    def is_empty(self):
        if self.front is None and self.back is None:
          return True
        else:
          return False

    
    # This function is passed a piece of data and a reference to a node within the list. 
    # Function will add data into the list positioned after node. If node == None, function 
    # inserts data at the front of the list. function returns nothing
    def insert_after(self, data, node):
      # assign the new node to current
      current = self.Node(data, None, None)
      # if the provided node is None add to front
      if node is None:
        self.push_front(data)
      # if node is at the back of the list, push to back of list
      elif node.next is None:
        self.push_back(data)
      # else insert node after the node passed in
      else:
        # set new node next to the node next passed in
        current.next = node.get_next()
        # set node passed in next to the new node
        node.next = current

    # This function searches the list for a node containing data. Function returns a reference to the first node containing data.
    def search(self, data):
      # Makes the first node in the linked list as current 
      current = self.front
      # Iterates through the linked list if the list is not empty
      while current is not None:
        # Checks if the data in the current node matches the data.
        if current.data == data:
          # Returns the current node if data is found
          return current      
        # Moves to the next node 
        current = current.next
      # Returns None if data is not found
      return None

    # this funtion returns the number of pieces of data stored in the list
    def __len__(self):
      # set current to the front of the list
      current = self.get_front()
      # set count to 0
      count = 0
      # while current is not empty
      while current is not None:
        # increment count
        count += 1
        # set current to the next node
        current = current.get_next()
      # return count
      return count