import random


def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3
    balls of the same color were drawn in the first 3 draws.
    '''

    success = 0
    for i in range(numTrials):
        bucket = [1, 1, 1, 1, 0, 0, 0, 0]
        result = 0
        for j in range(3):
            choice = random.choice(bucket)
            bucket.remove(choice)
            result += choice
        if result == 3 or result == 0:
            success += 1
    return success/numTrials


print(drawing_without_replacement_sim(100))
