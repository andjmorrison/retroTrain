import numpy as np
import retro
import tensorflow as tf
from tensorflow.keras import layers
import tqdm

def main():
    env = retro.make(game='SuperMarioWorld-Snes', state='YoshiIsland1')
    obs = env.reset()
    while True:
        action = env.action_space.sample()
        obs, reward, done, info = env.step(action)

        print('Action: ', action)
        print('Reward: ', reward)
        print('Info: ', info)
        env.render()

        if done:
            obs = env.reset()
    env.close()

if __name__ == "__main__":
    try:
         main()
    except Exception as err:
        print(err)