from game import SnakeGame


def print_controls():
    print("Practice 11 Snake controls:")
    print("  Arrow keys change direction.")
    print("  Food has weight and disappears after a timer.")
    print("  Press Space after game over to restart.")


if __name__ == "__main__":
    print_controls()
    SnakeGame().run()
