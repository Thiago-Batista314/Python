import copy
import random
# Consider using the modules imported above.

# The commentaries at side of codes are exemplifing what its piece of code does;
class Hat:
    def __init__(self, **kwargs):
        # Builds the list with the color n-times;
        self.contents = [k for k, v in kwargs.items() for _ in range(v)] # Ex: b = ['blue', 'blue', 'red', 'red', 'green', 'green', 'green']
    
    def draw(self, drawn):
        # Switches case drawn > len(self.contents), or does nothing otherwise;
        n = min(drawn, len(self.contents))
        drawn_balls = []

        # Add randomly the balls to the drawn_balls list and
        # remove from self.contents list;
        for _ in range(n):
            pos = random.randint(0, len(self.contents)-1)
            drawn_balls.append(self.contents[pos]) # Ex: ['blue', 'red']
            self.contents.pop(pos) # b ~> ['blue', 'red', 'red', 'green', 'green']

        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    for _ in range(num_experiments):
        # Do a copy of hat class;
        experiment_hat = copy.deepcopy(hat)

        # Build a list with drawn balls of the copied hat;
        drawn_balls = experiment_hat.draw(num_balls_drawn)

        balls_req = []

        # Calculates the probability of drawn_balls;
        for k, v in expected_balls.items(): # Ex: expected_balls = {'green': 2}
            if drawn_balls.count(k) >= v:
                balls_req.append(1) # If green went to the drawn_balls list 2 or more times;
        balls_req = sum(balls_req) # Sum of times green went to that list;
        if balls_req == len(expected_balls): # Add 1 to m variable if the times of ball went == len(expected_balls);
            m += 1                           # So, following the current example in coments, we'll have two possible results:
    probability = m / num_experiments        # 1º: green is in drawn_balls < 1 times. ~> m won't add 1 because len(expected) = 1;
                                             # 2º: green is in drawn_balls >= 1 times. ~> m add 1 because len(expected) = 1;
    return probability                       
