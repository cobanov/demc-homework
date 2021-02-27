-- ========= DEMC Database Queries ========= --
-- Author: Mert Cobanov
-- Date: 25.04.2021
-- Description: TBD
-- ========================================= --

DROP DATABASE IF EXISTS imdb2;
CREATE DATABASE imdb2;
USE imdb2;

-- ======= 1. Akas ======= -- 
CREATE TABLE `akas` (
  `titleId` VARCHAR(255) NOT NULL,
  `ordering` INTEGER NOT NULL,
  `title` TEXT NOT NULL,
  `region` CHAR(4),
  `language` CHAR(4),
  `types` VARCHAR(255) NOT NULL,
  `attributes` VARCHAR(255) NOT NULL,
  `isOriginalTitle` BOOLEAN
);

-- ======= 2. Ratings ======= -- 
CREATE TABLE `ratings` (
  `tconst` 			  VARCHAR(255) NOT NULL, -- not null bc PK
  `averageRating`	FLOAT,
  `numVotes`		  INTEGER
);

-- ======= 3. Title Basics ======= -- 
CREATE TABLE `title_basics` (
  `tconst` VARCHAR(255) NOT NULL,
  `titleType` VARCHAR(50),
  `primaryTitle` TEXT,
  `originalTitle` TEXT,
  `isAdult` BOOLEAN,
  `startYear` INTEGER,
  `endYear` INTEGER,
  `runtimeMinutes` INTEGER,
  `genres` VARCHAR(255) NOT NULL
);

-- ======= 4. Crew ======= -- 
CREATE TABLE `crew` (
  `tconst` VARCHAR(255) NOT NULL,
  `directors` VARCHAR(255) NOT NULL,
  `writers` VARCHAR(255) NOT NULL
);

-- ======= 5. Principals ======= -- 
CREATE TABLE `principals` (
  `tconst` VARCHAR(255) NOT NULL,
  `ordering` TINYINT NOT NULL,
  `nconst` VARCHAR(255) NOT NULL,
  `category` VARCHAR(255),
  `job` TEXT,
  `characters` TEXT
);

-- ======= 6. Episodes ======= -- 
CREATE TABLE episodes (
  `tconst` VARCHAR(255) NOT NULL,
  `parentTconst` VARCHAR(255) NOT NULL,
  `seasonNumber` INTEGER,
  `episodeNumber` INTEGER
);

-- ======= 6. Name basics ======= -- 

CREATE TABLE name_basics (
  `nconst`      VARCHAR(255) NOT NULL,
  `primaryName` VARCHAR(255) NOT NULL,
  `birthYear`  SMALLINT,
  `deathYear`   SMALLINT,
  `primaryProfession` VARCHAR(255) NOT NULL,
  `knownForTitles`    VARCHAR(255) NOT NULL
)
