top_avg = """SELECT *
FROM rm_episodes
INNER JOIN ratings
ON rm_episodes.tconst = ratings.tconst
ORDER BY averageRating
DESC
LIMIT 5
"""
worst_avg = """SELECT *
FROM rm_episodes
INNER JOIN ratings
ON rm_episodes.tconst = ratings.tconst
ORDER BY averageRating
ASC
LIMIT 5
"""

top_vote = """SELECT *
FROM rm_episodes
INNER JOIN ratings
ON rm_episodes.tconst = ratings.tconst
ORDER BY numVotes
DESC
LIMIT 5
"""

worst_vote = """SELECT *
FROM rm_episodes
INNER JOIN ratings
ON rm_episodes.tconst = ratings.tconst
ORDER BY numVotes
ASC
LIMIT 5
"""

seven_b = """SELECT * 
FROM name_basics 
WHERE birthYear > 2000 
AND primaryProfession 
LIKE '%music_department%' 
AND primaryProfession 
LIKE '%actress%' """

seven_c = """select count(*) from four_actress """
