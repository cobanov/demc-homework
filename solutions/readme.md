# Solutions

## 1) Rick and Morty

## Hazirlik

Sectigim dizi `Rick and Morty` oldugu icin oncelikle `title_basics` tablosundan karsilik gelen keyini bulmam gerekiyor.

```sql
select * from title_basics where originalTitle='Rick and Morty'
```

![](img/rick.png)

```
tconst -> tt2861424
```

Bu sorunun cozumu icin yukarida buldugumuz `tconst`'a sahip tum episodelari bulmamiz gerekiyor. Bu yuzden oncelikler `episodes` tablosuna gidiyorum.

```sql
select * from episodes where parentTconst='tt2861424'
```

![](img/rm_episodes.png)
Goruldugu gibi `parentTconst` ilgili dizinin benzersiz kodunu tutarken, bu kez tconst ilgili bolumun ismini tutuyor. `ratings` tablosuyla eslesen vote ve rate degerlerini join etmemiz gerekiyor.

Bu tabloyu asagidaki cogu yerde kullanacagiz isleri kolay hale getirmek icin bu episodelarin tutuldugu SQL sorgusundan bir VIEW yaratalim.

```sql
CREATE VIEW rm_episodes AS
SELECT *
FROM episodes
WHERE parentTconst='tt2861424'
```

1. Seçtiğiniz dizinin IMDB average rating'i en yüksek olan 5 bölümü

```sql
SELECT *
FROM rm_episodes
LEFT JOIN ratings
ON rm_episodes.tconst = ratings.tconst
ORDER BY averageRating
DESC
LIMIT 5;
```

2. Seçtiğiniz dizinin IMDB average rating'i en düşük olan 5 bölümü

```sql
SELECT *
FROM rm_episodes
LEFT JOIN ratings
ON rm_episodes.tconst = ratings.tconst
ORDER BY averageRating
ASC
LIMIT 5;
```

3. Seçtiğiniz dizinin IMDB'de en çok kişi tarafından oylanmış 5 bölümü

```sql
SELECT *
FROM rm_episodes
LEFT JOIN ratings
ON rm_episodes.tconst = ratings.tconst
ORDER BY numVotes
DESC
LIMIT 5;
```

4. Seçtiğiniz dizinin IMDB'de en az kişi tarafından oylanmış 5 bölümü

```sql
SELECT *
FROM rm_episodes
LEFT JOIN ratings
ON rm_episodes.tconst = ratings.tconst
ORDER BY numVotes
ASC
LIMIT 5;
```

## 2. Genel Sorulari

1. 2000-2010 arasında oyuncularından biri tarafından yönetilmiş filmlerin listesi (Cozulmedi)

```sql
-- Selected Years shows online movies
-- create table selected_years as select tconst, originalTitle from title_basics where titleType='movie' and startYear > 2000 and startYear < 2010

-- Selected only directos and acts
-- create table director_actor as select tconst, nconst, category, characters from principals where category in ('director', 'actor', 'actress')

-- joined together directors and acts with movies
-- create table years_all as select selected_years.tconst, originalTitle, nconst, category, characters from selected_years left join director_actor on selected_years.tconst = director_actor.tconst

-- only directors within selected years
-- create table years_directors as select * from years_all where category='director'

-- only acts within selected years
-- create table years_acts as select * from years_all where category in ('actor', 'actress')

--
-- select * from years_directors inner join years_acts on (years_directors.nconst = years_acts.nconst and years_directors.tconst = years_acts.tconst)
```

2. 2000 yılından günümüze bir filmde müzik departmanında da yer almış
   aktrislerin listesi

```sql
SELECT * FROM name_basics WHERE birthYear > 2000 AND primaryProfession LIKE '%music_department%' AND primaryProfession LIKE '%actress%'
```

3. 4 ya da daha fazla aktris bulunduran filmlerin sayısı

```sql
create table four_actress as select tconst, count('category') as cnt from principals where category='actress' group by tconst having cnt >= 4

select count(*) from four_actress

```
