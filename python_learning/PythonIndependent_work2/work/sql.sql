SELECT ships.ship, captains.captain,
navigators.navigator, year, benefit
FROM ships
INNER JOIN captains ON ships.id_cap = captains.id_cap
INNER JOIN navigators ON ships.id_navigator = navigators.id_navigator
WHERE (captains.captain = 'Billy Bons'
OR navigators.navigator = 'Billy Bons')
AND year BETWEEN ? AND ?
ORDER BY ships.id