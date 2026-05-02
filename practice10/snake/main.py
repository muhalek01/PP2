from game import SnakeGame


def print_controls():
    print("Practice 10 Snake controls:")
    print("  Arrow keys change direction.")
    print("  Eat food, raise level every 4 foods, avoid walls and body.")
    print("  Press Space after game over to restart.")


if __name__ == "__main__":
    print_controls()
    SnakeGame().run()
