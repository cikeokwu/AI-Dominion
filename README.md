# AI-Dominion

Dominion specs:

### Variables

action_space: every valid action List[NumActions, Action1, Action2, ...]
observation_space: the size of how you're representing states e.g in the firefighter example
this would be 5 cause the states were represented as a 5-tuple

### Functions

Step: takes in an action and returns the following things
1) Observation: The new board state ()
2) Reward: the amount of reward achieved by previous action (victory points? idk?)
3) Done: a boolean representing whether or not the game has ended
4) Info[Optional]: a dict of general diagnostic info that y'all think might be useful for debugging
or potentially training

Reset: A function that ends and starts a new game. Should return the start state

Notes: If the agent tries to play a card or an action they can't play. Return a large negative reward
something like float("-inf") or -np.inf up to you.

