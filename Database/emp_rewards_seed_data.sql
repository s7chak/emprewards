INSERT into months(month_id) values(1);
INSERT into months(month_id) values(2);

INSERT into users (user_fname,user_lname, phone, email, password, admin_status, date_added) values ('Yeggi', 'Lee', '7745787750', 'yleekwon3@gmail.com', 'yl35726', True, SYSDATE());
INSERT into users (user_fname,user_lname, phone, email, password, admin_status, date_added) values ('Dhrov', 'Subramanian', '5127580498', 'dhrov@utexas.edu', 'ds39547', True, SYSDATE());
INSERT into users (user_fname,user_lname, phone, email, password, admin_status, date_added) values ('Subhayu', 'Chakravarty', '7377011233', 'subhayu@utexas.edu', 'sc59695', True, SYSDATE());

Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date,month_id1) values(1,2,50,'2019-09-01',1);
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date,month_id1) values(1,2,50,'2019-09-01',1);
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date,month_id1) values(2,1,100,'2019-09-01',1);
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date,month_id1) values(3,2,10,'2019-09-02',1);
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date,month_id1) values(2,1,25,'2019-09-03',1);
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date,month_id1) values(2,3,20,'2019-09-04',1);
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date,month_id1) values(2,1,15,'2019-09-05',1);
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date,month_id1) values(1,2,10,'2019-09-06',1);
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date,month_id1) values(3,1,30,'2019-09-07',1);
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date,month_id1) values(3,1,50,'2019-09-08',1);
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date,month_id1) values(3,2,100,'2019-09-09',1);
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date,month_id1) values(1,3,10,'2019-09-10',1);
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date,month_id1) values(2,1,20,'2019-09-20',1);
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date,month_id1) values(1,2,35,'2019-09-25',1);
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date,month_id1) values(3,1,10,'2019-09-30',1);
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date,month_id1) values(3,2,100,'2019-10-01',2);
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date,month_id1) values(1,3,10,'2019-10-02',2);
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date,month_id1) values(2,1,20,'2019-10-03',2);
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date,month_id1) values(1,3,20,'2019-10-04',2);
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date,month_id1) values(2,3,20,'2019-10-05',2);
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date,month_id1) values(1,3,10,'2019-10-16',2);
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date,month_id1) values(2,1,40,'2019-10-17',2);
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date,month_id1) values(3,1,20,'2019-10-18',2);
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date,month_id1) values(1,2,10,'2019-10-19',2);
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date,month_id1) values(2,1,20,'2019-10-20',2);
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date,month_id1) values(1,3,50,'2019-10-23',2);
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date,month_id1) values(2,1,10,'2019-10-24',2);
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date,month_id1) values(1,2,100,'2019-10-25',2);
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date,month_id1) values(3,1,10,'2019-10-26',2);


Insert into emprewardz_point_holder(user_id,totalpoints,cpoints, month, month_id0) values(1,1000,0,'2019-09-01',1);
Insert into emprewardz_point_holder(user_id,totalpoints,cpoints, month, month_id0) values(2,1000,0,'2019-09-01',1);
Insert into emprewardz_point_holder(user_id,totalpoints,cpoints, month, month_id0) values(3,1000,0,'2019-09-01',1);
Insert into emprewardz_point_holder(user_id,totalpoints,cpoints, month, month_id0) values(1,1000,0,'2019-10-01',2);
Insert into emprewardz_point_holder(user_id,totalpoints,cpoints, month, month_id0) values(2,1000,0,'2019-10-01',2);
Insert into emprewardz_point_holder(user_id,totalpoints,cpoints, month, month_id0) values(3,1000,0,'2019-10-01',2);


Insert into emprewardz_redemption(user_id,points_redeemed,date_redeemed, month_id2) values(2,50,'2019-09-25',1);
Insert into emprewardz_redemption(user_id,points_redeemed,date_redeemed, month_id2) values(1,100,'2019-09-28',1);
Insert into emprewardz_redemption(user_id,points_redeemed,date_redeemed, month_id2) values(3,100,'2019-09-29',1);
Insert into emprewardz_redemption(user_id,points_redeemed,date_redeemed, month_id2) values(3,80,'2019-10-25',2);
Insert into emprewardz_redemption(user_id,points_redeemed,date_redeemed, month_id2) values(2,100,'2019-10-25',2);
Insert into emprewardz_redemption(user_id,points_redeemed,date_redeemed, month_id2) values(1,100,'2019-10-26',2);
