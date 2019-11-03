CREATE TABLE emprewardz.`transact_points` (
  `source_user` int(11) NOT NULL,
  `dest_user` int(11) NOT NULL,
  `points` int(10) NOT NULL,
  `transact_date` date NOT NULL
);


CREATE TABLE `user` (
  `pk_user_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_fname` varchar(50) DEFAULT NULL,
  `user_lname` varchar(50) DEFAULT NULL,
  `username` varchar(20) NOT NULL,
  `admin_status` varchar(1) NOT NULL,
  `user_status` varchar(1) NOT NULL,
  `user_email` varchar(30) NOT NULL,
  `user_password` varchar(30) NOT NULL,
  `zip_code` int(11) DEFAULT NULL,
  `date_added` timestamp NOT NULL,
  PRIMARY KEY (`pk_user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=110 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE emprewardz.`point_holder` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `points` int(10) NOT NULL,
  `month` date NOT NULL,
  PRIMARY KEY (`user_id`,`month`)
) ENGINE=InnoDB AUTO_INCREMENT=110 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
