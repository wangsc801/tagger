DROP DATABASE IF EXISTS `tagger`;

CREATE DATABASE `tagger`;

USE `tagger`;

CREATE TABLE `user`(
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(32),
    password VARCHAR(40),
    role TINYINT DEFAULT 3
);

INSERT INTO `user` (username,password,role) VALUES ("admin","4e57e93aa2d8a878a7fc56cf2a71754c8e86c665",1);

CREATE TABLE `role`(
    id TINYINT PRIMARY KEY AUTO_INCREMENT,
    description VARCHAR(16)
);

INSERT INTO `role` VALUES (1,"admin");
INSERT INTO `role` VALUES (2,"vip");
INSERT INTO `role` VALUES (3,"plain");
INSERT INTO `role` VALUES (4,"banned");

CREATE TABLE `upload_file`(
    id INT PRIMARY KEY AUTO_INCREMENT,
    file_path VARCHAR(32),
    filename VARCHAR(48),
    uploader_id INT,
    tag VARCHAR(1024),
    upload_time DATETIME
);