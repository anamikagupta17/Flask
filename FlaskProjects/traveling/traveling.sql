/*
SQLyog Ultimate v12.09 (64 bit)
MySQL - 5.7.19 : Database - traveling
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`traveling` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `traveling`;

/*Table structure for table `m00_site` */

DROP TABLE IF EXISTS `m00_site`;

CREATE TABLE `m00_site` (
  `m00_id` int(11) NOT NULL AUTO_INCREMENT,
  `m00_site_name` varchar(300) DEFAULT NULL,
  `m00_website` varchar(300) DEFAULT NULL,
  `m00_description` varchar(300) DEFAULT NULL,
  `m00_email` varchar(200) DEFAULT NULL,
  `m00_username` varchar(200) DEFAULT NULL,
  `m00_password` varchar(20) DEFAULT NULL,
  `m00_contact_person` varchar(200) DEFAULT NULL,
  `m00_status` int(2) DEFAULT '1',
  PRIMARY KEY (`m00_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `m00_site` */

insert  into `m00_site`(`m00_id`,`m00_site_name`,`m00_website`,`m00_description`,`m00_email`,`m00_username`,`m00_password`,`m00_contact_person`,`m00_status`) values (1,'Tour','tour.com','Tour','admin@gmail.com','admin@gmail.com','123','Anamika',1);

/*Table structure for table `m01_menu` */

DROP TABLE IF EXISTS `m01_menu`;

CREATE TABLE `m01_menu` (
  `m_menu_id` int(11) NOT NULL AUTO_INCREMENT,
  `m_menu_name` varchar(200) DEFAULT NULL,
  `m_menu_description` varchar(200) DEFAULT NULL,
  `m_sub_menu` int(2) DEFAULT NULL,
  `m_menu_url` varchar(300) DEFAULT NULL,
  `m_menu_parentid` int(11) DEFAULT NULL,
  `m_menu_status` int(2) DEFAULT '1',
  PRIMARY KEY (`m_menu_id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `m01_menu` */

insert  into `m01_menu`(`m_menu_id`,`m_menu_name`,`m_menu_description`,`m_sub_menu`,`m_menu_url`,`m_menu_parentid`,`m_menu_status`) values (1,'Home','Home',0,'home',0,1),(2,'Tours','Tours',1,'tour',0,1),(3,'Hotels','Hotels',0,'hotels',0,1),(4,'Services','Services',0,'services',0,1),(5,'Blog','Blog',0,'blog',0,1),(6,'About','About',0,'about',0,1),(7,'Contact','Contact',0,'contact',0,1),(8,'Login','Login',0,'login',0,1),(9,'Destination','Destination',0,'javascript:;',2,1),(10,'Cruises','Cruises',0,'javascript:;',2,1),(11,'Hotels','Hotels',0,'javascript:;',2,1),(12,'Booking','Booking',0,'javascript:;',2,1);

/*Table structure for table `m02_menu` */

DROP TABLE IF EXISTS `m02_menu`;

CREATE TABLE `m02_menu` (
  `m_menu_id` int(11) NOT NULL AUTO_INCREMENT,
  `m_menu_name` varchar(200) DEFAULT NULL,
  `m_menu_description` varchar(200) DEFAULT NULL,
  `m_sub_menu` int(2) DEFAULT NULL,
  `m_menu_url` varchar(300) DEFAULT NULL,
  `m_menu_parentid` int(11) DEFAULT NULL,
  `m_menu_icon` varchar(1000) DEFAULT NULL,
  `m_menu_status` int(2) DEFAULT '1',
  PRIMARY KEY (`m_menu_id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `m02_menu` */

insert  into `m02_menu`(`m_menu_id`,`m_menu_name`,`m_menu_description`,`m_sub_menu`,`m_menu_url`,`m_menu_parentid`,`m_menu_icon`,`m_menu_status`) values (1,'Dashboard','Dashboard',0,'dashboard',0,'fa fa-home',1),(2,'Member','Member',1,'javascript:',0,'fa fa-user',1),(3,'','',0,'',0,NULL,0),(4,'','',0,'',0,NULL,0),(5,'','',0,'',0,NULL,0),(6,'','',0,'',0,NULL,0),(7,'Add Member','Add Member',0,'view_add_member',2,NULL,1),(8,'Member Detail','Member Detail',0,'member_detail',2,NULL,1);

/*Table structure for table `m03_member_details` */

DROP TABLE IF EXISTS `m03_member_details`;

CREATE TABLE `m03_member_details` (
  `m03_memid` int(11) NOT NULL AUTO_INCREMENT,
  `m03_mem_name` varchar(200) DEFAULT NULL,
  `m03_fname` varchar(200) DEFAULT NULL,
  `m_phone_no` varchar(12) DEFAULT NULL,
  `m_dob` date DEFAULT NULL,
  `m_address` text,
  `m_gender` varchar(1000) DEFAULT NULL,
  `m_email` varchar(200) DEFAULT NULL,
  `m_qualification` varchar(100) DEFAULT NULL,
  `m_current_status` text,
  `m_status` int(2) DEFAULT '1',
  PRIMARY KEY (`m03_memid`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `m03_member_details` */

insert  into `m03_member_details`(`m03_memid`,`m03_mem_name`,`m03_fname`,`m_phone_no`,`m_dob`,`m_address`,`m_gender`,`m_email`,`m_qualification`,`m_current_status`,`m_status`) values (1,'2','SAB KUCHH','1234567890','2018-10-10','HGSGSS','Other','SXHASAS@GMAIL.COM','Graduation','GRFE',1),(2,'2','DFCFBGH','DFBHH','2018-10-30','ASDTJUJCF','Female','CFB@GMAIL.COM','High School','DFGH',0),(3,'Anamika Gupta','Dinesh Kumar Gupta','8181047095','1996-05-17','Gola','Female','anamikag594@gmail.com','Graduation','job',1);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
