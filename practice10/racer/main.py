from racer import RacerApp


def print_controls():
    print("Practice 10 Racer controls:")
    print("  Left / Right arrows move the car.")
    print("  Collect randomly generated coins.")
    print("  Press Space after game over to restart.")


if __name__ == "__main__":
    print_controls()
    RacerApp().run()
