select cksum, count(*)
 from item
 group by cksum
 having count(*) > 1;