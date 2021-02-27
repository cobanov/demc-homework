top_avg = """SELECT *
FROM rm_episodes
LEFT JOIN ratings
ON rm_episodes.tconst = ratings.tconst
ORDER BY averageRating
DESC
LIMIT 5
"""
worst_avg = """SELECT *
FROM rm_episodes
LEFT JOIN ratings
ON rm_episodes.tconst = ratings.tconst
ORDER BY averageRating
ASC
LIMIT 5
"""

top_vote = """SELECT *
FROM rm_episodes
LEFT JOIN ratings
ON rm_episodes.tconst = ratings.tconst
ORDER BY numVotes
DESC
LIMIT 5
"""

worst_vote = """SELECT *
FROM rm_episodes
LEFT JOIN ratings
ON rm_episodes.tconst = ratings.tconst
ORDER BY numVotes
ASC
LIMIT 5
"""
