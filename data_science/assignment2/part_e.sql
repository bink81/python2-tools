SELECT count(*) FROM (
  SELECT c from (SELECT count(term) as c from frequency group by docid) as c
  where c > 300
) x;