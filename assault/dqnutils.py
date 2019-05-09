import numpy as np
from PIL import Image
INPUT_SHAPE = (84, 84)
from rl.core import Processor

from collections import deque


class AtariProcessor(Processor):
    def __init__(self, n_observations_per_state=4):
        self.preprocessed_observations = deque([], maxlen=n_observations_per_state)

    def combine_observations_singlechannel(self, dim_factor=0.5):
        dimmed_observations = [obs * dim_factor ** index
                               for index, obs in enumerate(reversed(self.preprocessed_observations))]
        return np.max(np.array(dimmed_observations), axis=0)

    # def process_observation(self, obs):
    #     img = obs[34:194:2, ::2]  # crop and downsize
    #     processed_observation = np.mean(img, axis=2).reshape(INPUT_SHAPE) / 255.0
    #     assert processed_observation.shape == INPUT_SHAPE
    #     self.preprocessed_observations.append(processed_observation)
    #     processed_observation = self.combine_observations_singlechannel()
    #     assert processed_observation.shape == INPUT_SHAPE
    #     return processed_observation.astype('uint8')  # saves storage in experience memory

    def process_observation(self, observation):
        img = observation[34:194:2, ::2]  # crop and downsize
        processed_observation = np.mean(img, axis=2).reshape(4,84, 84) / 255.0
        #assert processed_observation.shape == INPUT_SHAPE
        self.preprocessed_observations.append(processed_observation)
        processed_observation = self.combine_observations_singlechannel()
        return processed_observation.astype('uint8')  # saves storage in experience memory

    def process_state_batch(self, batch):
        # We could perform this processing step in `process_observation`. In this case, however,
        # we would need to store a `float32` array instead, which is 4x more memory intensive than
        # an `uint8` array. This matters if we store 1M observations.
        processed_batch = batch.astype('float32') / 255.
        return processed_batch

    def process_reward(self, reward):
        return np.clip(reward, -1., 1.)