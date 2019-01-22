import gym
from gym import error, spaces, utils
from gym.utils import seeding

class LearningMachinesEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
    print "poep"
  def step(self, action):
    print "kak"
  def reset(self):
    print "poepie"
  def render(self, mode='human', close=False):
    print "kakkie"