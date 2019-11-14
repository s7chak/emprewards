CREATE TABLE users(pk_user_id INT(100) PRIMARY KEY AUTO_INCREMENT, 
user_fname varchar(50) DEFAULT NULL,
user_lname varchar(50) DEFAULT NULL, 
username varchar(20) NOT NULL,
phone VARCHAR(100), 
email VARCHAR(100), 
password VARCHAR(7) NOT NULL, 
admin_status BOOLEAN,
date_added timestamp NOT NULL); 
 

CREATE TABLE emprewardz_transact_points (
  source_user int(11) NOT NULL,
  dest_user int(11) NOT NULL,
  points int(10) NOT NULL,
  transact_date date NOT NULL
);

ALTER TABLE emprewardz_transact_points ADD CONSTRAINT fk_users FOREIGN KEY (source_user) REFERENCES users(pk_user_id);
ALTER TABLE emprewardz_transact_points ADD CONSTRAINT fk_users2 FOREIGN KEY (dest_user) REFERENCES users(pk_user_id);


CREATE TABLE emprewardz_point_holder (
  user_id int(11) NOT NULL,
  points int(10) NOT NULL,
  month date NOT NULL,
  month_id int(11) NOT NULL,
  PRIMARY KEY (user_id,month_id)
);

ALTER TABLE emprewardz_point_holder ADD CONSTRAINT fk_points FOREIGN KEY (user_id) REFERENCES users(pk_user_id);


CREATE TABLE emprewardz_redemption (
  user_id int(11) NOT NULL,
  points_redeemed int(10),
  date_redeemed timestamp NOT NULL,
  month date NOT NULL,
  PRIMARY KEY (user_id,month)
);

ALTER TABLE emprewardz_redemption ADD CONSTRAINT fk_redeem FOREIGN KEY (user_id) REFERENCES users(pk_user_id);


INSERT into users (user_fname,user_lname,username, phone, email, password, admin_status) values ('Yeggi', 'Lee', 'yeggi', '7745787750', 'yleekwon3@gmail.com', 'yl35726', True);

INSERT into users (user_fname,user_lname,username, phone, email, password, admin_status) values ('Dhrov', 'Subramanian', 'DhrovS', '5127580498', 'dhrov@utexas.edu', 'ds39547', True);


CREATE or REPLACE View agg_points AS
Select A.user_id, A.PointsRedeemed, A.PointsGiven, B.PointsRecieved from
	(SELECT user_id, points_redeemed as PointsRedeemed, points as PointsGiven from emprewardz_redemption as red join emprewardz_transact_points as trpo
	on red.user_id = trpo.source_user
	group by user_id) AS A Join
	(SELECT user_id, points_redeemed as PointsRedeemed, points as PointsRecieved from emprewardz_redemption as red join emprewardz_transact_points as trpo
	on red.user_id = trpo.source_user
	group by user_id) AS B
	on A.user_id=B.user_id;