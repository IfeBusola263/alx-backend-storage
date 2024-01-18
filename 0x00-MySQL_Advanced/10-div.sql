-- Implementing a function that divides and returns the division
-- of the first by the second number and returns 0 if the second is 0

DELIMITER $$
-- CREATE function
CREATE FUNCTION SafeDiv(a INT, b INT)

-- DEclare return type
RETURNS FLOAT
BEGIN
DECLARE div_result FLOAT;

-- Check inputs
IF b = 0 THEN
SET div_result = 0;
ELSE
SET div_result = a / b;
END IF;

-- Return result
RETURN div_result;
END $$

DELIMITER ;
