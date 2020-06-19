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

    def sort(self):
        """
        Sort the robot's list.
        """
        # Fill this out

        # check if robot can move right (there is more than 1 list element)
        if self.can_move_right() == True:
            
            # get the number at position 0
            self.swap_item()

            # move to position 1
            self.move_right()
        
        else: 
            print(" RIP ")
            return 


        for i in range(1, len(self._list)):
            print('Loop num\t', i)
            self._position = i
            print("Item ", self._item)
            
            print("Compare: ", self._item, self._list[self._position])
            while i > 0 and self.compare_item() == -1:
                self.swap_item()
                print("Swap made. Item is", self._item, ". Position is", self._position)
                self._position -= 1

    def insertion_sort(self):

        for i in range(1, len(self._list)):
            
            curr_book = self._list[i]

            curr_index = i

            # while i > 0 and current book is smaller than the previous
                # move the current book to the left
            while curr_index > 0 and curr_book < self._list[curr_index - 1]:

                # swap them 
                self._list[curr_index], self._list[curr_index - 1] = self._list[curr_index - 1], self._list[curr_index] 

                # we need to keep track of our current book's changing index 
                curr_index -= 1

        return self._list


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    #l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]
    #l = [1, 3, 2, 5, 4]
    l = [2, 4, 3, 6, 1, 5]
    print("\nInput")
    print(l)

    robot = SortingRobot(l)

    #robot.sort()
    #print(robot._list)

    """
    # test item swap

    #print(robot._position)
    robot.swap_item()

    print("Item", robot._item)
    print("List", robot._list)
    """

    #print(5 > None)

    #robot.insertion_sort()
    print("\nSort")
    robot.sort()
    print("\nList")
    print(robot._list)


    l = [1,3,2,5, 0, 4]
    robot = SortingRobot(l)
    print(robot.insertion_sort())