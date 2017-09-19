import gym

env = gym.make('CartPole-v0')
env.reset()


while True:
	env.render()
	action_n = np.random.randint(2) # Randomly perform an action, move either left or right
	observation_n, reward_n, done_n, info = env.step(action_n)



