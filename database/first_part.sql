
-- select tconst from title_basics2 where primaryTitle='Rick and Morty';
-- tt2861424

-- CREATE VIEW rm_episodes AS SELECT * FROM episodes where parentTconst='tt2861424';
-- CREATE VIEW rm_ratings AS SELECT * FROM ratings WHERE tconst IN (SELECT tconst from rm_episodes);

-- CREATE VIEW rm_top_avg AS select * from rm_ratings order by averageRating DESC limit 5;
-- CREATE VIEW rm_worst_avg AS select * from rm_ratings order by averageRating ASC limit 5;
-- CREATE VIEW rm_top_vote AS select * from rm_ratings order by numVotes DESC limit 5;
-- CREATE VIEW rm_worst_vote AS select * from rm_ratings order by numVotes ASC limit 5;

-- select averageRating, numVotes, originalTitle from rm_top_avg left join title_basics2 on rm_top_avg.tconst = title_basics2.tconst
-- select averageRating, numVotes, originalTitle from rm_worst_avg left join title_basics2 on rm_worst_avg = title_basics2.tconst
-- select averageRating, numVotes, originalTitle from rm_top_vote left join title_basics2 on rm_top_vote = title_basics2.tconst
-- select averageRating, numVotes, originalTitle from rm_worst_vote left join title_basics2 on rm_worst_vote = title_basics2.tconst