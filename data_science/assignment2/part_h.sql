SELECT * FROM (
  SELECT sum(a.count * b.count) from frequency a, frequency b where a.docid='17035_txt_earn' and b.docid='10080_txt_crude' and a.term = b.term
) x;