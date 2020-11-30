"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
def scores(score):
    if score < 0:
        score = ("Invalid score")
        return score
    elif score > 100:
            score = print("Invalid score")

            return score

    elif score > 50:
        if score > 90:
            score = print("Excellent")

            return score

        else:
            score = print("Passable")

            return score

    else:
        score = print("Bad")

    return score


# TODO: Fix this!
def main():
    score = float(input("Enter score: "))
    score = scores(score)
    print(score)

if __name__ == '__main__':
    main()