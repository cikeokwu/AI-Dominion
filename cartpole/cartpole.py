import gym
from dqnagent import DQNAgent
import numpy as np

EPISODES = 1000
RENDER = True


if __name__ == "__main__":
    env = gym.make('CartPole-v1')
    state_size = env.observation_space.shape[0]
    action_size = env.action_space.n
    agent = DQNAgent(state_size, action_size)
    #agent.load("cartpole-dqn.h5")
    done = False
    batch_size = 32

    for e in range(EPISODES):
        state = env.reset()
        state = np.reshape(state, [1, 4])

        for time_t in range(500):
            if RENDER:
                env.render()
            action = agent.act(state)
            next_state, reward, done, _ = env.step(action)
            reward = reward if not done else -10 #penalize for taking actions when done
            next_state = np.reshape(next_state, [1, 4])
            agent.remember(state, action, reward, next_state, done)
            state = next_state

            if done:
                print("episode: {}/{}, score: {}".format(e, EPISODES, time_t))
                break
            if len(agent.memory) > batch_size:
                agent.replay(batch_size)

        if e % 10 == 0:
            agent.save("./cartpole-dqn.h5")