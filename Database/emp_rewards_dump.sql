CREATE TABLE users(pk_user_id INT(100) PRIMARY KEY AUTO_INCREMENT,
user_fname varchar(50) DEFAULT NULL,
user_lname varchar(50) DEFAULT NULL,
phone VARCHAR(100),
email VARCHAR(100) NOT NULL UNIQUE,
password VARCHAR(1000) NOT NULL,
admin_status BOOLEAN,
date_added timestamp);

CREATE TABLE months(
	month_id int(11) PRIMARY KEY AUTO_INCREMENT
);

CREATE TABLE emprewardz_point_holder (
  user_id int(11) NOT NULL,
  totalpoints int(10) NOT NULL DEFAULT 0,
  cpoints int(10) NOT NULL,
  month date,
  month_id0 int(11) NOT NULL,
  PRIMARY KEY (user_id,month_id0)
);

ALTER TABLE emprewardz_point_holder ADD CONSTRAINT fk_points FOREIGN KEY (user_id) REFERENCES users(pk_user_id);
ALTER TABLE emprewardz_point_holder ADD CONSTRAINT fk_month1 FOREIGN KEY (month_id0) REFERENCES months(month_id);

CREATE TABLE emprewardz_transact_points (
  source_user int(11) NOT NULL,
  dest_user int(11) NOT NULL,
  points int(10) NOT NULL,
  transact_date DATE NOT NULL,
  month_id1 int(11) NOT NULL,
  comment varchar(200) Default "Thanks Obama"
);

ALTER TABLE emprewardz_transact_points ADD CONSTRAINT fk_users FOREIGN KEY (source_user) REFERENCES users(pk_user_id);
ALTER TABLE emprewardz_transact_points ADD CONSTRAINT fk_users2 FOREIGN KEY (dest_user) REFERENCES users(pk_user_id);
ALTER TABLE emprewardz_transact_points ADD CONSTRAINT fk_month2 FOREIGN KEY (month_id1) REFERENCES months(month_id);


CREATE TABLE emprewardz_redemption (
  user_id int(11) NOT NULL,
  points_redeemed int(10),
  date_redeemed DATE NOT NULL,
  month_id2 int(11) NOT NULL,
  PRIMARY KEY (user_id,month_id2)
);

ALTER TABLE emprewardz_redemption ADD CONSTRAINT fk_redeem FOREIGN KEY (user_id) REFERENCES users(pk_user_id);
ALTER TABLE emprewardz_redemption ADD CONSTRAINT fk_month3 FOREIGN KEY (month_id2) REFERENCES months(month_id);

CREATE or REPLACE View agg_points AS
Select A.user_id, A.month_id, A.PointsRedeemed, A.PointsGiven, B.PointsReceived from
    (SELECT u.pk_user_id as user_id, m.month_id, red.month_id2, trpo.month_id1, sum(red.points_redeemed) as PointsRedeemed, sum(trpo.points) as PointsGiven
    from emprewardz_redemption as red
    right join emprewardz_transact_points as trpo on red.user_id = trpo.source_user and red.month_id2=trpo.month_id1
    left join users as u on u.pk_user_id=trpo.source_user
    left join months as m on m.month_id=trpo.month_id1
	group by red.month_id2,trpo.month_id1, red.user_id) A
    left Join
    (SELECT dest_user, month_id1, sum(points) as PointsReceived from emprewardz_transact_points as trpo
    left join users as u on u.pk_user_id=trpo.dest_user
	left join months as m on m.month_id=trpo.month_id1
	group by month_id1,dest_user) B on A.user_id=B.dest_user and A.month_id=B.month_id1
    order by B.PointsReceived Desc;

CREATE or REPLACE View agg_points2 AS
SELECT U.pk_user_id as user_id,CONCAT(u.user_fname,' ',u.user_lname) as Name, m.month_id as month_id2, t.PointsGiven, tr.PointsReceived, r.PointsRedeemed
from users U
left outer join
(SELECT trpo.source_user, trpo.month_id1, sum(trpo.points) as PointsGiven
    from emprewardz_transact_points as trpo
	group by trpo.month_id1, trpo.source_user) as t on t.source_user=u.pk_user_id

left outer join
(SELECT trr.dest_user, trr.month_id1, sum(trr.points) as PointsReceived
    from emprewardz_transact_points as trr
	group by trr.month_id1, trr.dest_user) as tr on tr.dest_user=u.pk_user_id

left outer join
(SELECT red.user_id, red.month_id2, sum(red.points_redeemed) as PointsRedeemed
    from emprewardz_redemption as red
	group by red.month_id2, red.user_id) as r on r.user_id=u.pk_user_id and r.month_id2=t.month_id1

join months m on (m.month_id=t.month_id1 or m.month_id=r.month_id2 or m.month_id=tr.month_id1 )
order by tr.PointsReceived desc, t.month_id1 desc, U.pk_user_id
;


DELIMITER //
CREATE PROCEDURE stored_proc(
    IN sources VARCHAR(255),
	IN dest VARCHAR(255),
    IN pointsGR int,
    IN monthId int(11),
    IN comments VARCHAR(255)
)
BEGIN
	Insert into emprewardz_transact_points values(sources,dest,pointsGR,SYSDATE(),monthId,comments);

	UPDATE emprewardz_point_holder
    SET emprewardz_point_holder.totalpoints = emprewardz_point_holder.totalpoints - pointsGR
	WHERE sources = emprewardz_point_holder.user_id
    ORDER BY month_id0 DESC LIMIT 1;

	UPDATE emprewardz_point_holder
    SET emprewardz_point_holder.cpoints = emprewardz_point_holder.cpoints + pointsGR
	WHERE dest = emprewardz_point_holder.user_id
    ORDER BY month_id0 DESC LIMIT 1;
END//
