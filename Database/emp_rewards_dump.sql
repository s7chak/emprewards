CREATE TABLE users(pk_user_id INT(100) PRIMARY KEY AUTO_INCREMENT, 
user_fname varchar(50) DEFAULT NULL,
user_lname varchar(50) DEFAULT NULL, 
phone VARCHAR(100), 
email VARCHAR(100) NOT NULL UNIQUE, 
password VARCHAR(7) NOT NULL, 
admin_status BOOLEAN,
date_added timestamp NOT NULL); 

CREATE TABLE months(
	month_id int(11) PRIMARY KEY AUTO_INCREMENT
);

CREATE TABLE emprewardz_point_holder (
  user_id int(11) NOT NULL,
  total int(10) NOT NULL DEFAULT 0,
  points int(10) NOT NULL,
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
Select A.user_id, A.month_id2, A.PointsRedeemed, A.PointsGiven, B.PointsRecieved from
	(SELECT user_id, month_id2,  points_redeemed as PointsRedeemed, points as PointsGiven from emprewardz_redemption as red join emprewardz_transact_points as trpo
	on red.user_id = trpo.source_user
	group by month_id2,user_id) A  Join
	(SELECT dest_user, month_id1, points as PointsRecieved from emprewardz_transact_points
	group by month_id1,dest_user) B
	on A.user_id=B.dest_user and A.month_id2=B.month_id1
    order by B.PointsRecieved Desc;
	
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
    SET emprewardz_point_holder.points = emprewardz_point_holder.points - pointsGR 
	WHERE sources = emprewardz_point_holder.user_id
    ORDER BY month_id0 DESC LIMIT 1; 
	
	UPDATE emprewardz_point_holder
    SET emprewardz_point_holder.total = emprewardz_point_holder.total + pointsGR 
	WHERE dest = emprewardz_point_holder.user_id
    ORDER BY month_id0 DESC LIMIT 1;
END//
