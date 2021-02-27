-- ========= DEMC Database Queries ========= --
-- Author: Mert Cobanov
-- Date: 25.04.2021
-- Description: TBD
-- ========================================= --


SET FOREIGN_KEY_CHECKS = 0;
SET UNIQUE_CHECKS = 0;

LOAD DATA LOCAL INFILE  '/Users/mertcobanoglu/Repos/demc-homework/datasets/title.akas.tsv' IGNORE
INTO TABLE akas
COLUMNS TERMINATED BY '\t'
IGNORE 1 LINES;

SET UNIQUE_CHECKS = 1;
SET FOREIGN_KEY_CHECKS = 1;
