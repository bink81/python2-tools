SELECT * FROM (
  SELECT docid from frequency where term = 'transactions' INTERSECT SELECT docid from frequency where term = 'world'
) x;