#!/usr/bin/env python3
from brain_games.scripts.engine import play_engine
from brain_games.scripts.games.calc import calc_game, task_text


def main():
    play_engine(calc_game, task_text)


if __name__ == "__main__":
    main()
