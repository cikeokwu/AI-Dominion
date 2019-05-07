import gym
from ddqnagent import DQNAgent
from dqnutils import preprocess_observation
import numpy as np
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'
EPISODES = 4000
RENDER = False


if __name__ == "__main__":
    env = gym.make('Assault-v0')
    state_size = env.observation_space.shape[0]
    action_size = env.action_space.n
    agent = DQNAgent(state_size, action_size)
    done = False
    batch_size = 50

    for e in range(EPISODES):
        state = env.reset()
        state = preprocess_observation(state)
        for time in range(500):
            if RENDER:
                env.render()
            action = agent.act(state)
            next_state, reward, done, _ = env.step(action)
            reward = reward if not done else -10
            next_state = preprocess_observation(next_state)
            agent.remember(state, action, reward, next_state, done)
            state = next_state
            if done:
                agent.update_target_model()
                print("episode: {}/{}, score: {}, e: {:.2}"
                      .format(e, EPISODES, time, agent.epsilon))
                break
            if len(agent.memory) > batch_size:
                agent.replay(batch_size)
        #if e % 10 == 0:
         #   agent.save("./save/assault-ddqn.h5")

