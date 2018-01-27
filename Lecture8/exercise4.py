import random


def draw_balls(balls, num_of_draws):
    result = random.sample(balls, num_of_draws)
    return result


def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    balls = [1, 1, 1, 0, 0, 0]
    success = 0
    for i in range(numTrials):
        one_draw = draw_balls(balls, 3)
        result = sum(one_draw)
        #print(one_draw, result)
        if result == 0 or result == 3:
            success += 1
            # print("success")
    return success / numTrials

print(noReplacementSimulation(10))
