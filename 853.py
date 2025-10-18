class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        '''
        KEY NOTES:
        A car that is ahead can never be affected by the cars behind it (no passing)

        each car time to reach target must be computed:
            time[i] = (target - position[i]) / speed[i].

        we need to sort cars by closest to target

        if current car's time is greater than that slowest time then 
        it cant catch the car ahead and instead forms a new fleet
        
        Otherwise, it catches up before/at the target -> it joins the existing fleet (no new fleet counted).
        '''

        ''' 
        
        
        
        PSUEDOCODE:

        #find the number of cars
        numofcars = len(position)

        #Initiliazing the number of car fleets int that we will return
        int carFleets

        # make a list to store (position, time)
        for i from 0 to numOfCars - 1:
            time[i] = (target - position[i]) / speed[i]

        # sort cars by position in descending order
        sort position and time together in descending order of position

        # keep track of the slowest time seen so far
        slowestTime = 0


        # loop through cars in sorted order
        for i from 0 to numOfCars - 1:
            # if the current car takes longer to reach the target
            # than the slowest fleet ahead, it forms a new fleet
            if time[i] > slowestTime:
                carFleets = carFleets + 1
                slowestTime = time[i]
            else:
                # otherwise, it joins the fleet ahead
                continue

        # return total fleets
        return carFleets

        '''
        



        # Step 1: find the number of cars
        numOfCars = len(position)

        # Step 2: make a list of (position, time) for each car
        cars = []
        for i in range(numOfCars):
            time = (target - position[i]) / speed[i]   # how long it takes to reach target
            cars.append((position[i], time))

        # Step 3: sort cars by position in descending order (closest to target first)
        cars.sort(reverse=True)

        # Step 4: initialize number of fleets and slowest time seen so far
        carFleets = 0
        slowestTime = 0.0

        # Step 5: loop through cars
        for pos, time in cars:
            # if this car's time is greater than the slowest time so far,
            # it cannot catch up → forms a new fleet
            if time > slowestTime:
                carFleets += 1
                slowestTime = time
            # else: this car catches up and joins the fleet ahead (do nothing)

        # Step 6: return total number of fleets
        return carFleets







        



