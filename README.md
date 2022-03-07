# Notes From [Course](https://www.youtube.com/watch?v=Mut_u40Sqz4&ab_channel=NicholasRenotte)
## Part 0
- Agent takes an action which interacts with an environment, which results in reward/observations to your agent. Then repeat.
- Limitations
  - Overkill for simple problems
- Assumes the environment is Markovian (future states for environment are based on current states and there are no random acts in the environment)
- Training can take a long time and is not always stable

## Part 1: Environments
- simulated environments can allow you to train your agent in a safe and cost effective way
- OpenAI gym is what you can use to build out environments or use pre-built environments.
  - very well supported; standard in the space