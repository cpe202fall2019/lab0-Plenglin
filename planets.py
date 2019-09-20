def weight_on_planets():
    print("What do you weigh on earth? ")
    weight = float(input())

    print(f"On Mars you would weigh {0.38 * weight} pounds.")
    print(f"On Jupiter you would weigh {2.34 * weight} pounds.")


if __name__ == '__main__':
    weight_on_planets()
