INSERT into users (user_fname,user_lname, phone, email, password, admin_status, date_added) values ('Yeggi', 'Lee', '7745787750', 'yleekwon3@gmail.com', 'yl35726', True, SYSDATE());
INSERT into users (user_fname,user_lname, phone, email, password, admin_status, date_added) values ('Dhrov', 'Subramanian', '5127580498', 'dhrov@utexas.edu', 'ds39547', True, SYSDATE());
INSERT into users (user_fname,user_lname, phone, email, password, admin_status, date_added) values ('Subhayu', 'Chakravarty', '7377011233', 'subhayu@utexas.edu', 'sc59695', True, SYSDATE());
​
​
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date) values(1,2,50,'2019-09-01');
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date) values(1,2,50,'2019-09-01');
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date) values(2,1,100,'2019-09-01');
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date) values(3,2,10,'2019-09-02');
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date) values(2,1,25,'2019-09-03');
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date) values(2,3,20,'2019-09-04');
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date) values(2,1,15,'2019-09-05');
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date) values(1,2,10,'2019-09-06');
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date) values(3,1,30,'2019-09-07');
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date) values(3,1,50,'2019-09-08');
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date) values(3,2,100,'2019-09-09');
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date) values(1,3,10,'2019-09-10');
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date) values(2,1,20,'2019-09-20');
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date) values(1,2,35,'2019-09-25');
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date) values(3,1,10,'2019-09-30');
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date) values(3,2,100,'2019-10-01');
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date) values(1,3,10,'2019-10-02');
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date) values(2,1,20,'2019-10-03');
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date) values(1,3,20,'2019-10-04');
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date) values(2,3,20,'2019-10-05');
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date) values(1,3,10,'2019-10-16');
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date) values(2,1,40,'2019-10-17');
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date) values(3,1,20,'2019-10-18');
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date) values(1,2,10,'2019-10-19');
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date) values(2,1,20,'2019-10-20');
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date) values(1,3,50,'2019-10-23');
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date) values(2,1,10,'2019-10-24');
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date) values(1,2,100,'2019-10-25');
Insert into emprewardz_transact_points(source_user,dest_user,points,transact_date) values(3,1,10,'2019-10-26');
​
​
Insert into emprewardz_redemption(user_id,points_redeemed,date_redeemed, month) values(2,50,'2019-09-25','2019-09-25');
Insert into emprewardz_redemption(user_id,points_redeemed,date_redeemed, month) values(1,100,'2019-09-28','2019-09-28');
Insert into emprewardz_redemption(user_id,points_redeemed,date_redeemed, month) values(3,100,'2019-09-29','2019-09-29');
Insert into emprewardz_redemption(user_id,points_redeemed,date_redeemed, month) values(3,80,'2019-10-25','2019-10-25');
Insert into emprewardz_redemption(user_id,points_redeemed,date_redeemed, month) values(2,100,'2019-10-25','2019-10-25');
Insert into emprewardz_redemption(user_id,points_redeemed,date_redeemed, month) values(1,100,'2019-10-26','2019-10-26');
​
Insert into emprewardz_point_holder(user_id,points, month, month_id) values(1,1000,'2019-09-01',1);
Insert into emprewardz_point_holder(user_id,points, month, month_id) values(2,1000,'2019-09-01',1);
Insert into emprewardz_point_holder(user_id,points, month, month_id) values(3,1000,'2019-09-01',1);
Insert into emprewardz_point_holder(user_id,points, month, month_id) values(1,1000,'2019-10-01',2);
Insert into emprewardz_point_holder(user_id,points, month, month_id) values(2,1000,'2019-10-01',2);
Insert into emprewardz_point_holder(user_id,points, month, month_id) values(3,1000,'2019-10-01',2);
