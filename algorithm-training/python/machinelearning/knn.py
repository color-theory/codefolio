"""
knn.py
This module contains an implementation of the k-nearest neighbors algorithm
"""
from typing import List, Tuple
from math import sqrt


class Rating:
    """
    A class to represent a rating in the k-nearest neighbors algorithm
    """

    def __init__(self, title, rating):
        self.title = title
        self.rating = rating

    def __repr__(self):
        return f"Rating({self.title}, {self.rating})"

    def validate(self):
        """
        Validate the rating
        """
        if self.rating < 1 or self.rating > 5:
            raise ValueError("Rating must be between 1 and 5")


class User:
    """
    A class to represent a user in the k-nearest neighbors algorithm
    """

    def __init__(self, name, ratings):
        self.name = name
        self.ratings = ratings

    def __repr__(self):
        return f"User({self.name}, {self.ratings})"

    def validate(self):
        """
        Validate the user's ratings
        """
        for rating in self.ratings:
            if rating < 1 or rating > 5:
                raise ValueError("Ratings must be between 1 and 5")


def euclidean_distance(ratings1: List[Rating], ratings2: List[Rating]) -> float:
    """
    Calculate the Euclidean distance between two lists of ratings

    Parameters:
    ratings1: List[Rating]: The first list of ratings
    ratings2: List[Rating]: The second list of ratings

    Returns:
    float: The Euclidean distance between the two lists of ratings
    """
    if len(ratings1) != len(ratings2):
        raise ValueError("Ratings lists must be the same length")

    rating_dict2 = {rating.title: rating.rating for rating in ratings2}

    distance = 0
    for rating1 in ratings1:
        if rating1.title in rating_dict2:
            rating2 = rating_dict2[rating1.title]
            distance += (rating1.rating - rating2) ** 2

    return sqrt(distance)


def knn(users: List[User], target_user: User, k: int, distance_func) -> List[Tuple[User, float]]:
    """
    Find the k-nearest neighbors of a target user

    Parameters:
    users: List[User]: The list of users
    target_user: User: The target user
    k: int: The number of neighbors to find

    Returns:
    List[Tuple[User, float]]: The k-nearest
    """
    distances = []
    for user in users:
        distance = distance_func(target_user.ratings, user.ratings)
        distances.append((user, distance))

    distances.sort(key=lambda x: x[1])
    return distances[:k]


def predict_scarface_rating(users: List[User], target_user: User, distance_func) -> float:
    """
    Predict the rating of Scarface for a target user

    Parameters:
    users: List[User]: The list of users
    target_user: User: The target user

    Returns:
    float: The predicted rating of Scarface for the target user
    """
    neighbors = knn(users, target_user, 3, distance_func)
    total = 0
    count = 0
    for neighbor, _ in neighbors:
        for rating in neighbor.ratings:
            if rating.title == "Scarface":
                total += rating.rating
                count += 1
    return total / count


past_users = [
    User("Alice", [Rating("Home Alone", 5), Rating(
        "The Matrix", 4), Rating("Scarface", 5)]),
    User("Bob", [Rating("Home Alone", 1), Rating(
        "The Matrix", 4), Rating("Scarface", 3)]),
    User("Charlie", [Rating("Home Alone", 5), Rating(
        "The Matrix", 3), Rating("Scarface", 5)]),
    User("David", [Rating("Home Alone", 5), Rating(
        "The Matrix", 5), Rating("Toy Story", 4)]),
    User("Eve", [Rating("Home Alone", 1), Rating(
        "The Matrix", 3), Rating("Scarface", 3)]),
    User("Frank", [Rating("Home Alone", 1), Rating(
        "The Matrix", 1), Rating("Scarface", 5)]),
    User("Grace", [Rating("Home Alone", 5), Rating(
        "Homeward Bound", 5), Rating("Scarface", 5)]),
]

smiley = User("smiley", [Rating("Home Alone", 5), Rating(
    "The Matrix", 5), Rating("Homeward Bound", 5)])
print("Smiley:")
print(knn(past_users, smiley, 3, euclidean_distance))
print(f"{predict_scarface_rating(past_users, smiley, euclidean_distance):.2f}")

plimpman = User("plimpman", [Rating("Home Alone", 1), Rating(
    "The Matrix", 1), Rating("Toy Story", 1)])
print("\nplimpman:")
print(knn(past_users, plimpman, 3, euclidean_distance))
print(f"{predict_scarface_rating(past_users, plimpman, euclidean_distance):.2f}")
