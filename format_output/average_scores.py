from builtins import input, float


def average():
    num_of_scores = 3
    score1 = input("Enter your first score: ")
    score2 = input("Enter a second score: ")
    score3 = input("Enter a third score: ")
    average_score = (float(score1) + float(score2) + float(score3)) / num_of_scores

    return average_score


if __name__ == '__main__':
    average_scores = average()
