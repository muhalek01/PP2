from racer import RacerApp


def print_controls():
    print("Practice 11 Racer controls:")
    print("  Left / Right arrows move the car.")
    print("  Weighted coins increase the enemy speed after N points.")
    print("  Press Space after game over to restart.")


if __name__ == "__main__":
    print_controls()
    RacerApp().run()
