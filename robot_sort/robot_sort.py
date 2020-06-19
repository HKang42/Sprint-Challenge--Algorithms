class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def set_position(self, i):
        """
        Set position to index i in the list.
        """
        while self.can_move_left() == True:
            self.move_left()
        
        for _ in range(0, i):
            self.move_right()

    def right_switch(self):
        """
        Swaps the list element at current position with the next element. 
        Position remains unchanged.

        The state of the list after each step is visualized using an example of [4, 2].
        The ^ refers to the current position of the robot.
        """
        # starting state

        # [4, N]  holding 2
        #  ^   

        self.swap_item()        
        # [2, N]  holding 4
        #  ^

        self.move_right()
        # [2, N]  holding 4
        #     ^

        self.swap_item()
        # [2, 4]  holding N
        #     ^

        self.move_left()
        # [2, 4]  holding 4
        #  ^   

        self.swap_item()
        # [N, 4]  holding 2
        #  ^   

    def sort(self):
        """
        Sort the robot's list.
        Uses a modified version of insertion sort. 
        The added set_position() and right_switch() helper functions handle most of the changes.
        """
        
        # check if robot can move right (there is more than 1 list element)
        if self.can_move_right() == False:
            return 

        # iterate through list and compare each element to the previous
        for i in range(1, len(self._list)):
            
            # Move to position i and get item. Replaces the value at i with None.
            self.set_position(i)
            self.swap_item()

            #print('\nLoop num', self._position)
            #print("Item ", self._item)            
            #print("Compare: ", self._item, "<", self._list[self._position], "=", self.compare_item())
            

            # iterate backwards from i to 0
            while self.can_move_left() == True:

                self.move_left()

                #print(self._list)
                #print("Compare: ", self._item, "<", self._list[self._position])

                if self.compare_item() == -1:
                    
                    # Move number at current position to the right. 
                    # Position remains unchanged.
                    self.right_switch()
                    
                    #print("Swap made. Item is", self._item, ". New Position is", self._position)
                    #print(self._list)
                    #print("New list", self._list)
                    
                else:
                    self.move_right()
                    break
            
            self.swap_item()
            #print(self._list)

    def insertion_sort(self):
        """
        Insertion sort reference code.
        The above solution is a modified version that 
        """
        for i in range(1, len(self._list)):
            
            curr_val = self._list[i]

            curr_index = i

            # while i > 0 and current value is smaller than the previous
            #       move the current book to the left
            while curr_index > 0 and curr_val < self._list[curr_index - 1]:

                self._list[curr_index], self._list[curr_index - 1] = self._list[curr_index - 1], self._list[curr_index] 

                curr_index -= 1

        return self._list


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]
    #l = [1, 3, 2, 5, 4]
    #l = [2, 4, 3, 6]
    #l = [4,2,0]
    print("\nInput")
    print(l)

    robot = SortingRobot(l)

    print("\nSorted List")
    robot.sort()
    print(robot._list)


    """
    # Test the set_position method

    l = [1,3,2,5,0,4]
    robot = SortingRobot(l)
    print('\n\n')
    print("Pos", robot._position)
    robot.set_position(5)
    print("Pos", robot._position)
    robot.swap_item()
    print("item", robot._item)
    """