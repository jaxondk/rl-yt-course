# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.6.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Import Dependencies

# !pip install stable-baselines3[extra]

# !pip install pyglet

# + jupyter={"outputs_hidden": true}
# !apt-get update
# !apt-get -y install python-opengl
# -

import os, gym # gym has environments
from stable_baselines3 import PPO # PPO is one of many algorithms you can use for RL
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.evaluation import evaluate_policy

# # Load Environment

import matplotlib.pyplot as plt
# %matplotlib inline
from IPython import display

environment_name = 'CartPole-v0'
env = gym.make(environment_name)

for e in range(1, 6):
    state = env.reset()
    done = False
    score=0
    
    while not done:
        env.render()
        action = env.action_space.sample()
        n_state, reward, done, info = env.step(action)
        score+=reward
    print(f'Episode: {e} | Score: {score}')

# ### Understanding the Environment

# https://github.com/openai/gym/blob/master/gym/envs/classic_control/cartpole.py
