-- ========= DEMC Database Queries ========= --
-- Author: Mert Cobanov
-- Date: 25.04.2021
-- Description: TBD
-- ========================================= --

-- ======= 1. Akas ======= -- 
CREATE TABLE `akas` (
  `titleId` varchar(255) DEFAULT NULL,
  `ordering` int(11) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `region` varchar(255) DEFAULT NULL,
  `language` varchar(255) DEFAULT NULL,
  `types` varchar(255) DEFAULT NULL,
  `attributes` varchar(255) DEFAULT NULL,
  `isOriginalTitle` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 0;
SET UNIQUE_CHECKS = 0;

LOAD DATA LOCAL INFILE  '/Users/mertcobanoglu/Repos/demc-homework/datasets/title.akas.tsv' IGNORE
INTO TABLE akas
COLUMNS TERMINATED BY '\t'
IGNORE 1 LINES;

SET UNIQUE_CHECKS = 1;
SET FOREIGN_KEY_CHECKS = 1;


-- ======= 2. Ratings ======= -- 
CREATE TABLE Title_ratings (
  title_id 			  VARCHAR(255) NOT NULL, -- not null bc PK
  average_rating	FLOAT,
  num_votes			  INTEGER
);


LOAD DATA LOCAL INFILE  '/Users/mertcobanoglu/Repos/demc-homework/datasets/title.ratings.tsv'
INTO TABLE Title_ratings
COLUMNS TERMINATED BY '\t'
IGNORE 1 LINES;



-- ======= 3. Name Basics ======= -- 
CREATE TABLE `basics` (
  `tconst` varchar(255) DEFAULT NULL,
  `titleType` varchar(255) DEFAULT NULL,
  `primaryTitle` varchar(255) DEFAULT NULL,
  `originalTitle` varchar(255) DEFAULT NULL,
  `isAdult` int(11) DEFAULT NULL,
  `startYear` int(11) DEFAULT NULL,
  `endYear` int(11) DEFAULT NULL,
  `runtimeMinutes` int(11) DEFAULT NULL,
  `genres` varchar(255) DEFAULT NULL
)

SET FOREIGN_KEY_CHECKS = 0;
SET UNIQUE_CHECKS = 0;

LOAD DATA LOCAL INFILE  '/Users/mertcobanoglu/Repos/demc-homework/datasets/name.basics.tsv' IGNORE
INTO TABLE basics
COLUMNS TERMINATED BY '\t'
IGNORE 1 LINES;

SET UNIQUE_CHECKS = 1;
SET FOREIGN_KEY_CHECKS = 1;


-- ======= 4. Crew ======= -- 

CREATE TABLE `crew` (
  `tconst` varchar(255) DEFAULT NULL,
  `directors` varchar(255) DEFAULT NULL,
  `writers` varchar(255) DEFAULT NULL
)

SET FOREIGN_KEY_CHECKS = 0;
SET UNIQUE_CHECKS = 0;

LOAD DATA LOCAL INFILE  '/Users/mertcobanoglu/Repos/demc-homework/datasets/title.crew.tsv' IGNORE
INTO TABLE crew
COLUMNS TERMINATED BY '\t'
IGNORE 1 LINES;

SET UNIQUE_CHECKS = 1;
SET FOREIGN_KEY_CHECKS = 1;


-- ======= 5. Principals ======= -- 

CREATE TABLE `principals` (
  `tconst` varchar(255) DEFAULT NULL,
  `ordering` int(11) DEFAULT NULL,
  `nconst` varchar(255) DEFAULT NULL,
  `category` varchar(255) DEFAULT NULL,
  `job` varchar(255) DEFAULT NULL,
  `characters` varchar(255) DEFAULT NULL
) 

SET FOREIGN_KEY_CHECKS = 0;
SET UNIQUE_CHECKS = 0;

LOAD DATA LOCAL INFILE  '/Users/mertcobanoglu/Repos/demc-homework/datasets/title.principals.tsv' IGNORE
INTO TABLE principals
COLUMNS TERMINATED BY '\t'
IGNORE 1 LINES;

SET UNIQUE_CHECKS = 1;
SET FOREIGN_KEY_CHECKS = 1;