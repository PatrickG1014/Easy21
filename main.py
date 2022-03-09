from env import Env


if __name__ == '__main__':
    e = Env()
    e.reset()
    while not e.is_terminate:
        a = input('player action (0: hit, 1: stick): ')
        s, r, t = e.step(int(a))
    print('--------------------------')
    if r == 1:
        print(f'Win. Player sum: {s.player_sum}')
    elif r == 0:
        print(f'Draw. Player sum: {s.player_sum}')
    else:
        print(f'Lose. Player sum: {s.player_sum}')
    print('--------------------------')