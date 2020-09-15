"""
Program: average_scores.py
Author: Levi Shepherd
Last date modified: 09/14/2020



The purpose of this program is to accept input of
the user's name, age and test scores and output this
information with a calculated average grade.
"""
from builtins import input, float


def average():
    # Set a variable to hold the number of scores to be input
    num_of_scores = 3

    # Gather input for scores 1-3
    score1 = input("Enter your first score: ")
    score2 = input("Enter a second score: ")
    score3 = input("Enter a third score: ")

    # Calculate the average score from scores 1-3 divided by num of scores
    average_score = (float(score1) + float(score2) + float(score3)) / num_of_scores

    # Return the variable to main
    return average_score


if __name__ == '__main__':
    # Prompt for last name, first name and age.
    last_name = input("Enter your last name: ")
    first_name = input("Enter your first name: ")
    age = input("Enter your age: ")

    # Call method to gather scores and calculate the average
    average_scores = average()

    # Output the results to the user
    print(f'{last_name}, {first_name} age: {age} average grade: {average_scores:.2f}')

    # Testing of input scores
    #      Input        |      Expected Output     |      Actual Output
    # 88.5, 98.5, 66.78 |          84.59           |          84.59
    # 99.999, 90, 88.8  |          92.93           |          92.93
    # 70, 65, 85        |          73.33           |          73.33
