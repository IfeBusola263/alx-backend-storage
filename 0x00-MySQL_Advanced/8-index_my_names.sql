-- Create index for name in the names table
-- Index idx_name_first indexes name and the first letter of name

CREATE INDEX idx_name_first ON names (name, (name(1));
