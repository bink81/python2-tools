SELECT * FROM (
	SELECT docid, count from frequency where term = 'washington' or term = 'taxes' or term = 'treasury' group by docid
) x order by x.count;