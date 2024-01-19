-- Create index for name in the names table
-- Index idx_name_first indexes name, the first letter of name and score

CREATE INDEX idx_name_first_score ON names (name(1), score);
