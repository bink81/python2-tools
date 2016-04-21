SELECT count(*) FROM (
  SELECT distinct docid from frequency where term='law' or term='legal' 
) x;