"""
Chapter Six - Math and Logic Puzzles
"""


# 6.1
# Given 20 bottles of pills, where 19 have pills of 1.0g each, and 1 has pills
# of 1.1g each. Find the heavy bottle with one usage of a scale that provides exact weights.

def six_one():
    
    """
    Take N pills from bottle N for bottles (1 from 1, 2 from 2, etc.).
    We can use the decimal place to find the bottle number.
    
    e.g., if bottle 13 is the heavy bottle, then the right side of the scale should show
    XXX.3 grams. The .3 tells us that it's either the 3rd or 13th bottle. We can figure out
    which one it is by adding the expected weight if all pills are 1.0g (210g). If our current
    weight is 0.3g above that (210.3g), it is bottle #3; otherwise if the weight is 1.3g above
    expected (211.3g), then it is bottle #13.
    """
    
    pass


# 6.2
# Given two games, find the shot probability that determines the boundary decision
# between the two games that gives the greatest chance at winning.
# Game One: you get one shot to make the hoop.
# Game Two: you get three shots and you have to make two of the three.

def six_two():
    
    """
    At first glance, we would want to choose G1 if we have a high p since we
    have one shot, and G2 for a low p since we have three shots.
    
    The G1 probability is simple:
    P1 = p
    
    In G2, I have 4 ways of making 2 baskets. Since these events are
    independent, here are the probabilities of each:
    p(1 and 2) = p*p*(1-p)  (missing 3)
    p(1 and 3) = p*(1-p)*p  (missing 2)
    p(2 and 3) = (1-p)*p*p  (missing 1)
    P(1 and 2 and 3) = p^3
    
    So the G2 probability is:
    P2 = 3(1-p)^2*p^2 + p^3
    P2 = 3p^2 - 2p^3
    
    Now we need to find the value of p so that:
    P1 = P2, or
    p = 3p^2 - 2p^3
    
    Simplifying:
    p * (-2p^2 + 3p - 1) = 0
    2p^2 - 3p + 1 = 0
    (2p-1)*(p-1) = 0
    So, p = 0, 0.5, and 1
    
    The probabilities are the same at 0 or 1, so our solution is the remaining point:
    p = 0.5
    
    For p>0.5, we should choose game 1.
    For p<0.5, we should choose game 2.
    """
    
    pass


# 6.3
# Given an 8x8 chessboard with two opposing corners cut off (so there are 62 spaces),
# show if it's possible to cover the board with 31 dominoes such at each domino
# covers two spaces.

def six_three():
    
    """
    Basically, we need to determine if there are 31 pairs of joined spaces on the board.
    Each pair of joined spaces has to include one white square and one black square.
    So, each domino has to cover one black square and one white square.
    
    If we cover any two opposing corners on the board, then we are covering two
    white squares, or two black squares.
    This means that we cannot cover the board with the dominoes, since the number of white
    squares and the number of black squares are not the same.
    """
    
    pass


# 6.4
# Given a triangle and three ants who are initially on the triangle's vertices, find the 
# probability that there will be a collision if each ant randomly picks a direction to 
# walk around the triangle.
# Assume each direction has the same chance of being chosen and that 
# the ants move at the same speed.

def six_four():
    
    """
    1 = P(collision) + P(no collision), so 
    P(collision) = 1 - P(no collision)
    
    The only way that the ants will not collide is if they all pick the same direction.
    P(no collision) = P(1-left and 2-left and 3-left) or P(1-right and 2-right and 3-right)
    
    If each direction has the same probability of being chosen, then:
    P(no collision) = 0.5*0.5*0.5 + 0.5*0.5*0.5 = 2 * 0.5^3 = 0.25
    
    So,
    P(collision) = 1 - P(no collision) = 1 - 0.25, so
    P(collision) = 0.75 for a triangle.
    
    For the N-sided polygon case, we generalize to the following:
    P(collision) = 1 - P(no collision) = 1 - (2 * 0.5^N), or
    P(collision) = 1 - 0.5^(N-1)
    
    For example, ants on a 10-sided polygon would have a
    (1 - 0.5^9) = 0.00195 = 0.195% chance of not colliding.
    """
    
    pass


# 6.5
# Given a 5-quart jug and a 3-quart jug, how can I get 4-quarts of water?
# Assume if I have an unlimited supply of water, and I cannot fill the jugs to 
# any amount less than the full value.

def six_five():
    
    """
    1. Fill the 5Q jug and pour into the 3Q jug. This leaves 2Q in the 5Q.
    2. Dump the 3Q jug and pour the 5Q jug into the 3Q jug. This leaves 2Q in the 3Q jug.
    3. Fill the 5Q jug and pour the 5Q jug into the 3Q jug. This leaves 4Q in the 5Q jug.
    
    Note: this can be done with any two jugs of prime number value and
    the sum of the jug sizes.
    """
    
    pass


# 6.6
# The blue-eyed people problem.
# 
# If a large number of people live on an island, how many days would it take
# everyone with blue eyes to leave given the following:
# 
# 1. There is one flight off the island per day, 
# 2. no one knows if they have blue eyes,
# 3. no one can tell anyone else they have blue eyes, 
# 4. no one knows how many people have blue eyes, and
# 5. everyone knows that at least one person has blue eyes.
# 
# In other words, NumBE >= 1.

def six_six():
    
    """
    Let's assume only one person has blue eyes.
    The blue eyed person would leave on the first day because he/she saw
    no one else with blue eyes and knew that NumBE >= 1. Since there is at least
    one person with blue eyes, he/she would assume it is him/herself, and would
    leave. The others would not assume they have blue eyes since they see the other
    with blue eyes, and they don't know if they have blue eyes, which
    would make NumBE > 1 and would take more than one day to check.
    
    Let's assume two people have blue eyes.
    The first day, neither would leave, since they have both seen one other
    person with blue eyes, and they know that NumBE could be more than 1.
    On the second day, since no one left the first day, each would assume that 
    the other blue-eyed person saw at least one other person with blue eyes. Since he/she
    did not see that other person, it must be them, so NumBE must be 2, and they would both leave.
    
    Let's assume three people have blue eyes.
    The first day, no one would leave since the blue eyed people see two others with blue eyes.
    The second day, no one would leave. All three of them see two others with blue eyes, and if 
    NumBE was 2, then the other two would have left the second day.
    The third day, all three leave, since NumBE > 2, but no more than 3, since each of them saw
    two other people with blue eyes, but no one left the second day.
    
    So, it will take N days for N people with blue eyes to leave the island, assuming
    that everyone on the island has seen enough of the others to have guaranteed
    to see everyone with blue eyes, if there are others.
    """
    
    pass


# 6.7
# The world ruler makes a law that all couples must have at least one female child.
# What will the gender ratio be, given the following:
# 1. Each couple stops having children after their first girl, and
# 2. each baby has an equal chance of being a boy or girl.

def six_seven():
    
    """
    We expect the ratio to be male-dominated, since each family will have only
    one girl, but can have any number of boys. This would not be the case if the
    probability of each gender was not the same.
    
    For any baby:
    P(boy) = P(girl) = 0.5
    
    Probability of having 0 boys before girl: P(girl) = 0.5
    Probability of having 1 boys before girl: P(boy) and P(girl) = 0.5^2
    Probability of having 2 boys before girl: P(boy) and P(boy) and P(girl) = 0.5^3
    Probability of having N boys before girl: [P(boy)]^(N) and P(girl) = 0.5^N+1
    
    ...apparently the answer is 50:50. I imagine that is because the number of
    couples is very large. For smaller numbers of couples, I expect that the ratio
    will be more heavily favored toward boys.
    """
    
    pass


# 6.8
# Given a building with 100 floors and 2 eggs, find the lowest floor N where dropping
# an egg will break it. Minimize the worst case number of drops.

def six_eight():
    
    """
    We can use the first egg to get close to the correct floor, and use the
    second egg to find the exact floor. We start by testing every 10th floor (10,
    20, 30, etc.). When the egg breaks on the ith floor, we know the floor is
    between floors i and i-1. We go back to floor i-1 and increment testing
    every floor upwards with our second egg until it breaks. That floor is N.
    In the general case, the most efficient number to skip is sqrt(# floors),
    which gives 2*sqrt(# floors)-1 worst case drops.
    
    However, the book solution is much more efficient. It begins by skipping X floors
    with the first egg, then (X-1) floors, then (X-2) floors, etc. This way, the number
    of total egg drops from egg one and egg two are the same. In the case of 100 floors,
    X is 14, and there are only 14 steps in the worst case.
    """
    
    pass


# 6.9
# Given 100 closed lockers, a man toggles (open if closed, close if opened) every ith
# locker for i = 1 to 100. How many lockers are left open after the 100th pass?

def six_nine():
    
    """
    For all lockers, they should be open and shut an even number of times leaving all
    lockers closed (except for a few). Since each locker will be toggled once for each
    of its factors up to the square root, and again for each factor after the square
    root, the number of toggles will always be even and all lockers will be shut.

    Except when we have a square number. Since a square number has an “extra” root, that
    root will only be toggled once and will not have a corresponding number to “undo” its
    toggle. This will leave all the square numbers open, and no others. So, that becomes
    the number of square numbers less than or equal to 100, which is 10 lockers.
    """
    
    pass


# 6.10
# Given 1000 bottles of soda, where one is poisoned, find the poisoned bottle. You are given
# 10 test strips that change color if the poison contacts it, but the test takes seven days
# and you can only run tests once per day. You can run as many tests as you like each day, and
# you can place as much liquid as you want on the test strips, as they will only change color
# in the presence of the poison.

def six_ten():
    
    """
    This (book) solution is the best solution possible. My solution was the 28 day solution,
    which is the next best solution if you assume that you only have 10 strips. The book's
    non-optimal solutions assume that you get 10 per day, even though the prompt does not say that.

    We take each (numbered) bottle and change its number to a binary representation. Since
    we have 10 strips, we can store up to 2^10 = 1024 bottles. We label each test strip as
    a binary location 1-10. Then, we place drops for the binary representation for each bottle
    on the numbered strips. For example, 1000 in binary is 1111101000. So, we would place drops
    from bottle #1000 on strips 4, 6, 7, 8, 9, and 10. We then send all 10 strips for testing.
    When we receive the results, we can rebuild our binary number with the numbered strips, and
    find our bottle number. This search always takes 7 days in any case for any number of bottles,
    assuming that we always have enough strips so that 2^(# strips) >= (# bottles).
    """
    
    pass
