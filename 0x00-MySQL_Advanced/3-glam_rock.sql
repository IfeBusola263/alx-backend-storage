-- Creating a querry for bands with 'Glam rock' as their main style
-- in the metal band database
SELECT band_name,
CASE
WHEN style LIKE '%Glam rock%' AND split IS NOT NULL THEN split - formed
WHEN style LIKE '%Glam rock%' AND split IS NULL THEN 2022 - formed
END AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
