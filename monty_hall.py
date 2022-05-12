from random import choice, randint

class MontyHall:
    def __init__(self) -> None:
        self.doors = [1,2,3]
    
    def _assign_doors_(self) -> list:
        '''
        Function assigns door to participant, winning door, and host.
        Returns
            List of integers in the order of participant, winning door, and host door.
            
            [participant_door, winning_door, host_door]
        '''
        #copy of list attribute
        doors = self.doors.copy()
        
        participant_door = randint(1,3)
        winning_door = randint(1,3)
        
        doors.remove(participant_door)
        if participant_door != winning_door:
            doors.remove(winning_door)
            host_door = doors[0]
        else:
            host_door = choice(doors)
        
        return [participant_door, winning_door, host_door]
    
    def _switch_door_(self, assigned_doors: list) -> tuple:
        '''
        Function will switch the participant door.
        Args
            assigned_doors - list of integers containing participant, winning door, and host door. In that order.
        Returns
            returns a tuple with the new participant door assigned to index 1 and winning door at index 2
        '''
        #copy of list attribute
        doors = self.doors.copy()
        
        participant_door, winning_door, host_door = assigned_doors
        
        doors.remove(participant_door)
        doors.remove(host_door)
        
        return (doors[0], winning_door)
    
    def run_simulation(self, num_sims: int) -> int:
        '''
        Function runs simulations.
        args
            num_sims - The number of simulations to run 
        returns
            Integer that represents how many times the partipant won by changing doors
        '''
        times_won = 0
        
        for i in range(num_sims):
            assigned_doors = self._assign_doors_()
            participant, winning_door = self._switch_door_(assigned_doors)
            
            if participant == winning_door:
                times_won += 1

        return times_won
