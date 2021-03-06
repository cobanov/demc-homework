-- ========= DEMC Database Queries ========= --
-- Author: Mert Cobanov
-- Date: 25.04.2021
-- Description: TBD
-- ========================================= --


LOAD DATA LOCAL INFILE  '/Users/mertcobanoglu/Repos/demc-homework/datasets/title.akas.tsv' IGNORE
INTO TABLE akas
COLUMNS TERMINATED BY '\t'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE  '/Users/mertcobanoglu/Repos/demc-homework/datasets/title.basics.tsv' IGNORE
INTO TABLE akas
COLUMNS TERMINATED BY '\t'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE  '/Users/mertcobanoglu/Repos/demc-homework/datasets/title.crew.tsv' IGNORE
INTO TABLE akas
COLUMNS TERMINATED BY '\t'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE  '/Users/mertcobanoglu/Repos/demc-homework/datasets/title.episode.tsv' IGNORE
INTO TABLE akas
COLUMNS TERMINATED BY '\t'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE  '/Users/mertcobanoglu/Repos/demc-homework/datasets/title.principals.tsv' IGNORE
INTO TABLE akas
COLUMNS TERMINATED BY '\t'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE  '/Users/mertcobanoglu/Repos/demc-homework/datasets/title.ratings.tsv' IGNORE
INTO TABLE akas
COLUMNS TERMINATED BY '\t'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE  '/Users/mertcobanoglu/Repos/demc-homework/datasets/name.basics.tsv' IGNORE
INTO TABLE akas
COLUMNS TERMINATED BY '\t'
IGNORE 1 LINES;


