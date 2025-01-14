-- Survival rate by gender
SELECT 
    Sex,
    COUNT(*) as total_passengers,
    SUM(Survived) as survivors,
    ROUND(CAST(SUM(Survived) AS FLOAT) / COUNT(*) * 100, 2) as survival_rate
FROM titanic
GROUP BY Sex;

-- Survival rate by passenger class
SELECT 
    Pclass,
    COUNT(*) as total_passengers,
    SUM(Survived) as survivors,
    ROUND(CAST(SUM(Survived) AS FLOAT) / COUNT(*) * 100, 2) as survival_rate
FROM titanic
GROUP BY Pclass
ORDER BY Pclass;

-- Age group analysis
SELECT 
    AgeGroup,
    COUNT(*) as total_passengers,
    SUM(Survived) as survivors,
    ROUND(CAST(SUM(Survived) AS FLOAT) / COUNT(*) * 100, 2) as survival_rate
FROM titanic
GROUP BY AgeGroup
ORDER BY 
    CASE AgeGroup
        WHEN 'Child' THEN 1
        WHEN 'Teen' THEN 2
        WHEN 'Young Adult' THEN 3
        WHEN 'Adult' THEN 4
        WHEN 'Senior' THEN 5
    END;

-- Family size impact on survival
SELECT 
    FamilySize,
    COUNT(*) as total_passengers,
    SUM(Survived) as survivors,
    ROUND(CAST(SUM(Survived) AS FLOAT) / COUNT(*) * 100, 2) as survival_rate
FROM titanic
GROUP BY FamilySize
ORDER BY FamilySize;

-- Embarked port analysis
SELECT 
    Embarked,
    COUNT(*) as total_passengers,
    ROUND(AVG(Fare), 2) as avg_fare,
    SUM(Survived) as survivors,
    ROUND(CAST(SUM(Survived) AS FLOAT) / COUNT(*) * 100, 2) as survival_rate
FROM titanic
WHERE Embarked IS NOT NULL
GROUP BY Embarked;
