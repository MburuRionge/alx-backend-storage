#!/usr/bin/env python3
"""MongoDB operations with Python using pymong"""


def top_students(mongo_collection):
    """ Returns all students sorted by average score """
    top_student = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averagescore": {"$avg": "$topics.score"}
                }
            },
        {"$sort": {"averageScore": -1}}
        ])

    return top_student
