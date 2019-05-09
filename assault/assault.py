import gym
from ddqnagent import DQNAgent
from dqnutils import AtariProcessor
import matplotlib.pyplot as plt
import numpy as np
import random
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'
EPISODES = 4000
RENDER = True
TRAIN = True


if __name__ == "__main__":
    env = gym.make("PongDeterministic-v4")
    state_size = env.observation_space.shape[0]
    action_size = env.action_space.n
    agent = DQNAgent(state_size, action_size)
    done = False
    batch_size = 50
    p = AtariProcessor(10)

    while True:
        state = env.reset()
        for time in range(100):
            env.render()
            action = 1
            next_state, reward, done, info = env.step(action)

    # if TRAIN:
    #     while True:
    #         state = env.reset()
    #         state = p.process_observation(state)
    #         for time in range(1000):
    #             if RENDER:
    #                 env.render()
    #             agent.load("dqn0_BreakoutDeterministic-v4_weights.h5f")
    #             action = agent.act(state)
    #             next_state, reward, done, info = env.step(action)
    #             next_state = p.process_observation(next_state)
    #             agent.remember(state, action, reward, next_state, done)
    #             state = next_state
    #             print(info)
    #             if done:
    #                 agent.update_target_model()
    #                 print("episode: {}/{}, score: {}, e: {:.2}"
    #                       .format(e, EPISODES, reward, agent.epsilon))
    #                 break
    #             if len(agent.memory) > batch_size:
    #                 agent.replay(batch_size)
    # else:
    #     plt.rcParams['axes.labelsize'] = 14
    #     plt.rcParams['xtick.labelsize'] = 12
    #     plt.rcParams['ytick.labelsize'] = 12
    #
    #     # Where to save the figures
    #     PROJECT_ROOT_DIR = "."
    #     CHAPTER_ID = "rl"
    #
    #
    #     def save_fig(fig_id, tight_layout=True):
    #         path = os.path.join(PROJECT_ROOT_DIR, "images", CHAPTER_ID, fig_id + ".png")
    #         print("Saving figure", fig_id)
    #         if tight_layout:
    #             plt.tight_layout()
    #         plt.savefig(path, format='png', dpi=300)
    #
    #
    #     state = env.reset()
    #     img = p.process_observation(state)
    #     plt.figure(figsize=(11, 7))
    #     plt.subplot(121)
    #     plt.title("Original observation (160×210 RGB)")
    #     plt.imshow(state)
    #     plt.axis("off")
    #     plt.subplot(122)
    #     plt.title("Preprocessed observation (88×80 greyscale)")
    #     plt.imshow(img.reshape(80, 80), interpolation="nearest", cmap="gray")
    #     plt.axis("off")
    #     save_fig("preprocessing_plot")
    #     plt.show()
    #
    #     for e in range(EPISODES):
    #         state = env.reset()
    #         img = p.process_observation(state)
    #         plt.figure(figsize=(11, 7))
    #         plt.subplot(121)
    #         plt.title("Original observation (160×210 RGB)")
    #         plt.imshow(state)
    #         plt.axis("off")
    #         plt.subplot(122)
    #         plt.title("Preprocessed observation (88×80 greyscale)")
    #         plt.imshow(img.reshape(80, 80), interpolation="nearest", cmap="gray")
    #         plt.axis("off")
    #         save_fig("preprocessing_plot")
    #         plt.show()
    #         for time in range(1000):
    #             if RENDER:
    #                 env.render()
    #             action = random.sample([n for n in range(action_size)], 1)
    #             next_state, reward, done, _ = env.step(action)
    #             next_state = p.process_observation(next_state)
    #             state = next_state
    #             if done:
    #                 print("episode: {}/{}, score: {}"
    #                       .format(e, EPISODES, reward))
    #                 break
    #             if len(agent.memory) > batch_size:
    #                 agent.replay(batch_size)
    #
    #
