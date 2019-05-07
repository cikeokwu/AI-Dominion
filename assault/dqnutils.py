import numpy as np

color = np.array([210, 164, 74]).mean()

def preprocess_observation(obs):
    img = obs[1:176:2, ::2]  # crop and downsize
    img = img.mean(axis=2)  # to greyscale”
    img[img == color] = 0   # improve contrast
    img = (img - 128) / 128 - 1   # normalize from -1. to 1.
    return img.reshape(88, 80, 1)

