-- Average tea party rating for each tea party
select tp.tea_party_name, avg(r.rating) as average_rating
from tea_party as tp
join tea_party_rating as r USING(tea_party_id)
group by tea_party_name 
order by average_rating DESC;

-- Window function
SELECT
    tp.tea_party_name,
    tr.rating,
    AVG(tr.rating) OVER(partition by tp.tea_party_id) as avg_tea_party_rating
FROM tea_party as tp
JOIN tea_party_rating as tr USING(tea_party_id);

SELECT
    tp.tea_party_name,
    tr.rating,
    RANK() OVER(PARTITION BY tp. ORDER by tr.rating DESC) as avg_tea_party_rating
FROM tea_party as tp
JOIN tea_party_rating as tr USING(tea_party_id);

-- Rank / Dense Rank
-- Rank each planet's party by average party rating
WITH average_party_rating AS(
    SELECT
        tp.tea_party_id,
        tp.tea_party_name,
        tp.tea_party_host_planet,
        AVG(tr.rating) AS avg_rating
    FROM tea_party tp
    JOIN tea_party_rating tr ON tp.tea_party_id = tr.tea_party_id
    GROUP BY tp.tea_party_id, tp.tea_party_name, tp.tea_party_host_planet
)
select 
	ap.tea_party_name, 
	pl.planet_name,
	ap.avg_rating,
    DENSE_RANK() OVER (PARTITION BY ap.tea_party_host_planet ORDER BY ap.avg_rating DESC) AS rank_within_planet
from average_party_rating as ap
JOIN planet pl ON ap.tea_party_host_planet = pl.planet_id
ORDER BY pl.planet_name, rank_within_planet;

-- I want to economize on my tea consumption. 
-- For each planet, I want to know the party that serves the most different types of tea.
-- Additionally, I want to know the average rating of these parties to ensure I'm attending high-quality events.
-- https://mode.com/sql-tutorial/sql-window-functions

WITH TeaBlendCounts AS (
    -- Count the number of unique tea blends served at each party
    SELECT
        tpb.tea_party_id,
        tp.tea_party_name,
        tp.tea_party_host_planet,
        AVG(tpr.rating) as avg_rating,
        COUNT(DISTINCT tpb.tea_blend_id) AS blend_count
    FROM
        tea_party_blend_assignment as tpb
    JOIN
        tea_party tp ON tpb.tea_party_id = tp.tea_party_id
    JOIN    
        tea_party_rating as tpr ON tpr.tea_party_id = tp.tea_party_id
    GROUP BY
        tpb.tea_party_id, tp.tea_party_name, tp.tea_party_host_planet
)
SELECT
    tbc.tea_party_id,
    tbc.tea_party_name,
    pl.planet_name,
    tbc.blend_count,
    tbc.avg_rating,
    RANK() OVER (PARTITION BY tbc.tea_party_host_planet ORDER BY tbc.blend_count DESC) AS blend_rank_within_planet
FROM
    TeaBlendCounts tbc
JOIN
    planet pl ON tbc.tea_party_host_planet = pl.planet_id
ORDER BY
    pl.planet_name, blend_rank_within_planet;