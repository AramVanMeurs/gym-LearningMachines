from gym.envs.registration import register

register(
    id='foo-v0',
    entry_point='gym-Learning_Machines.envs:LearningMachinesEnv',
)
register(
    id='foo-extrahard-v0',
    entry_point='gym-Learning_Machines.envs:FooExtraHardEnv',
)