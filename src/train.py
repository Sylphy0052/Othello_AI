from environment import Environment
from player import AI
import setting


def main():
    env = Environment(AI(1), AI(2))
    env.init()
    for episode in range(setting.EPISODE_NUM):
        env.train(episode)


if __name__ == '__main__':
    main()
