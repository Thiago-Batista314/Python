import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = [k for k, v in kwargs.items() for _ in range(v)]
    
    def draw(self, drawn):
        n = min(drawn, len(self.contents))
        drawn_balls = []

        for _ in range(n):
            pos = random.randint(0, len(self.contents)-1)
            drawn_balls.append(self.contents[pos])
            self.contents.pop(pos)

        return drawn_balls

    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    for _ in range(num_experiments):
        experiment_hat = copy.deepcopy(hat)
        drawn_balls = experiment_hat.draw(num_balls_drawn)
        balls_req = []
        for k, v in expected_balls.items():
            if drawn_balls.count(k) >= v:
                balls_req.append(1)
        balls_req = sum(balls_req)
        if balls_req == len(expected_balls):
            m += 1
    probability = m / num_experiments
    return probability

if __name__ == '__main__':
    hat = Hat(black=6, red=4, green=3)
    probability = experiment(hat=hat,
                  expected_balls={"red": 2, "green": 1},
                  num_balls_drawn=5,
                  num_experiments=2000)
    print(probability)
