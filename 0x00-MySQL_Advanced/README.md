## MySQL advanced
* 0-uniq_users.sql
```
a SQL script that creates a table users following these requirements:

With these attributes:
id, integer, never null, auto increment and primary key
email, string (255 characters), never null and unique
name, string (255 characters)
```

* 1-country_users.sql
```
a SQL script that creates a table users following these requirements:

With these attributes:
id, integer, never null, auto increment and primary key
email, string (255 characters), never null and unique
name, string (255 characters)
country, enumeration of countries: US, CO and TN,
never null (= default will be the first element of the enumeration, here US)
```

* 2-fans.sql
```
a SQL script that ranks country origins of bands,
ordered by the number of (non-unique) fans

Requirements:

Import this table dump: metal_bands.sql.zip
Column names must be: origin and nb_fans
```

* 3-glam_rock.sql
```
a SQL script that lists all bands with Glam rock as their main style,
ranked by their longevity

Requirements:

Imports this table dump: metal_bands.sql.zip.
Column names must be: band_name and lifespan
(in years until 2022 - please use 2022 instead of YEAR(CURDATE())).
using attributes formed and split for computing the lifespan.
```

* 4-store.sql
```
a SQL script that creates a trigger that decreases
the quantity of an item after adding a new order.

Quantity in the table items can be negative
```

* 5-valid_email.sql
```
a SQL script that creates a trigger that resets the
attribute valid_email only when the email has been changed.
```

* 6-bonus.sql
```
 a SQL script that creates a stored procedure AddBonus that adds a new correction for a student.

Requirements:

Procedure AddBonus is taking 3 inputs (in this order):
-> user_id, a users.id value (you can assume user_id is
linked to an existing users).
-> project_name, a new or already exists projects - if no projects.name found in the table, you should create it.
-> score, the score value for the correction.
```

* 7-average_score.sql
```
a SQL script that creates a stored procedure ComputeAverageScoreForUser
that computes and store the average score for a student.
Note: An average score can be a decimal

Requirements:

Procedure ComputeAverageScoreForUser is taking 1 input:
user_id, a users.id value (you can assume user_id is
linked to an existing users)
```

* 8-index_my_names.sql
```
a SQL script that creates an index idx_name_first on the
table names and the first letter of name.

Requirements:

Import this table dump: names.sql.zip
Only the first letter of name must be indexed.
```

* 9-index_name_score.sql
```
a SQL script that creates an index idx_name_first_score
on the table names and the first letter of name and the score.

Requirements:

Import this table dump: names.sql.zip
Only the first letter of name AND score must be indexed.
```

* 10-div.sql
```
a SQL script that creates a function SafeDiv that divides
(and returns) the first by the second number or returns 0
if the second number is equal to 0.

Requirements:

-> A function must be created
-> The function SafeDiv takes 2 arguments:
a, INT
b, INT
-> returns a / b or 0 if b == 0
```

* 11-need_meeting.sql
```
a SQL script that creates a view need_meeting that
lists allstudents that have a score under 80 (strict)
and no last_meeting or more than 1 month.

Requirements:

-> The view need_meeting should return all students name when:
-> They score are under (strict) to 80
-> AND no last_meeting date OR more than a month
```

* 100-average_weighted_score.sql
```
a SQL script that creates a stored procedure
ComputeAverageWeightedScoreForUser that computes and store
the average weighted score for a student.

Requirements:

Procedure ComputeAverageScoreForUser is taking 1 input:
user_id, a users.id value (you can assume user_id is linked to an existing users)
```

* 101-average_weighted_score.sql
```
a SQL script that creates a stored procedure
ComputeAverageWeightedScoreForUsers that computes
and store the average weighted score for all students.

Requirements:

Procedure ComputeAverageWeightedScoreForUsers is not taking any input.
```