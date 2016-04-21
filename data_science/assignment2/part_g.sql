SELECT * FROM (
	--SELECT * FROM A order by A.row_num, A.col_num
	--SELECT * FROM B order by B.row_num, B.col_num
	SELECT A.row_num, B.col_num, sum(A.value * B.value)
	FROM A, B 
	WHERE A.row_num = 2 and B.col_num = 3 and A.col_num = B.row_num order by A.col_num -- group by A.row_num;
) x;