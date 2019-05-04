# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: localhost (MySQL 5.7.21)
# Database: epkl3
# Generation Time: 2019-05-04 13:29:47 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table master_siswa
# ------------------------------------------------------------

LOCK TABLES `master_siswa` WRITE;
/*!40000 ALTER TABLE `master_siswa` DISABLE KEYS */;

INSERT INTO `master_siswa` (`id`, `NIS`, `nama`, `kelas`, `program_ahli`, `pkl`, `status_judul`, `pembimbing`)
VALUES
	(1,'171810145','Aar Arti H','XI.RPL-1','Rekayasa Perangkat Lunak',0,0,0),
	(2,'171810146','Ahmad Luki R','XI.RPL-1','Rekayasa Perangkat Lunak',0,0,0),
	(3,'171810147','Ai Rahmawati','XI.RPL-1','Rekayasa Perangkat Lunak',0,0,0),
	(4,'171810148','Alawiyah Nuraeni','XI.RPL-1','Rekayasa Perangkat Lunak',0,0,0),
	(5,'171810149','Almalia Maulida Nurazwa','XI.RPL-1','Rekayasa Perangkat Lunak',0,0,0),
	(6,'171810150','Alsa Nurfadilah','XI.RPL-1','Rekayasa Perangkat Lunak',0,0,0),
	(7,'171810151','Dini Sintia','XI.RPL-1','Rekayasa Perangkat Lunak',0,0,0),
	(8,'171810152','Fahmi Nurul Azis','XI.RPL-1','Rekayasa Perangkat Lunak',0,0,0),
	(9,'171810153','Fitri Aulia N','XI.RPL-1','Rekayasa Perangkat Lunak',0,0,0),
	(10,'171810154','Hamdan Yanmufahir','XI.RPL-1','Rekayasa Perangkat Lunak',0,0,0),
	(11,'171810155','Hana Mustafiana','XI.RPL-1','Rekayasa Perangkat Lunak',0,0,0),
	(12,'171810156','Ineu Nuraeni','XI.RPL-1','Rekayasa Perangkat Lunak',0,0,0),
	(13,'171810157','Irma Asmaul Husna','XI.RPL-1','Rekayasa Perangkat Lunak',0,0,0),
	(14,'171810158','Janwar Nurahman','XI.RPL-1','Rekayasa Perangkat Lunak',0,0,0),
	(15,'171810159','Leni Aprianti','XI.RPL-1','Rekayasa Perangkat Lunak',0,0,0),
	(16,'171810160','Lyghar Nor Ilmhi','XI.RPL-1','Rekayasa Perangkat Lunak',0,0,0),
	(17,'171810161','Natasya Putri Pebriani','XI.RPL-1','Rekayasa Perangkat Lunak',0,0,0),
	(18,'171810162','Neng Dena Denia A.','XI.RPL-1','Rekayasa Perangkat Lunak',0,0,0),
	(19,'171810163','Nova Novita','XI.RPL-1','Rekayasa Perangkat Lunak',0,0,0),
	(20,'171810164','Nurul Fatimah','XI.RPL-1','Rekayasa Perangkat Lunak',0,0,0),
	(21,'171810165','Risdan Alifiqri','XI.RPL-1','Rekayasa Perangkat Lunak',0,0,0),
	(22,'171810166','Riyanto Junaedi','XI.RPL-1','Rekayasa Perangkat Lunak',0,0,0),
	(23,'171810167','Riza Surya H.','XI.RPL-1','Rekayasa Perangkat Lunak',0,0,0),
	(24,'171810168','Rizki Raksa Negara','XI.RPL-1','Rekayasa Perangkat Lunak',0,0,0),
	(25,'171810169','Rulla Meilani','XI.RPL-1','Rekayasa Perangkat Lunak',0,0,0),
	(26,'171810170','Sendra Anwar','XI.RPL-1','Rekayasa Perangkat Lunak',0,0,0),
	(27,'171810171','Silpiani','XI.RPL-1','Rekayasa Perangkat Lunak',0,0,0),
	(28,'171810172','Sinta Nurul Aulia','XI.RPL-1','Rekayasa Perangkat Lunak',0,0,0),
	(29,'171810173','Sopy Tasfiyatunnafsi','XI.RPL-1','Rekayasa Perangkat Lunak',0,0,0),
	(30,'171810174','Tina Gustiana','XI.RPL-1','Rekayasa Perangkat Lunak',0,0,0),
	(31,'171810175','Vera Veronica','XI.RPL-1','Rekayasa Perangkat Lunak',0,0,0),
	(32,'171810176','Wina Widyawati','XI.RPL-1','Rekayasa Perangkat Lunak',0,0,0),
	(33,'171810177','Yani Haryani','XI.RPL-1','Rekayasa Perangkat Lunak',0,0,0),
	(34,'171810178','Yola Yolanda','XI.RPL-1','Rekayasa Perangkat Lunak',0,0,0),
	(35,'171810180','AI RENI ANDRIYANI','XI.RPL-2','Rekayasa Perangkat Lunak',0,0,0),
	(36,'171810181','AI WANDA FITRIA','XI.RPL-2','Rekayasa Perangkat Lunak',0,0,0),
	(37,'171810182','AKMAL MUHAMAD RIZAL','XI.RPL-2','Rekayasa Perangkat Lunak',0,0,0),
	(38,'171810183','ARIK SYAHRIR ROMDONI','XI.RPL-2','Rekayasa Perangkat Lunak',0,0,0),
	(39,'171810184','ASRI NAFILAH','XI.RPL-2','Rekayasa Perangkat Lunak',0,0,0),
	(40,'171810185','CICI CAHRANI','XI.RPL-2','Rekayasa Perangkat Lunak',0,0,0),
	(41,'171810186','DEVI SEFIA SAFITRI','XI.RPL-2','Rekayasa Perangkat Lunak',0,0,0),
	(42,'171810187','ELSA RAHMAWATI','XI.RPL-2','Rekayasa Perangkat Lunak',0,0,0),
	(43,'171810188','HENDRA LESMANA','XI.RPL-2','Rekayasa Perangkat Lunak',0,0,0),
	(44,'171810189','IDA KUSFU LAILA','XI.RPL-2','Rekayasa Perangkat Lunak',0,0,0),
	(45,'171810190','IRHAN MUHAMAD RAIHAN','XI.RPL-2','Rekayasa Perangkat Lunak',0,0,0),
	(46,'171810191','KHAERUL IKRAM FADHLIKA','XI.RPL-2','Rekayasa Perangkat Lunak',0,0,0),
	(47,'171810192','M. URFAN FADILLAH','XI.RPL-2','Rekayasa Perangkat Lunak',0,0,0),
	(48,'171810193','MEILANI DAMAYANTI','XI.RPL-2','Rekayasa Perangkat Lunak',0,0,0),
	(49,'171810194','MILDA PRIKRULIAHTI','XI.RPL-2','Rekayasa Perangkat Lunak',0,0,0),
	(50,'171810195','NISA SEPTIANI','XI.RPL-2','Rekayasa Perangkat Lunak',0,0,0),
	(51,'171810196','PENA MELINDA SEPTIANI','XI.RPL-2','Rekayasa Perangkat Lunak',0,0,0),
	(52,'171810197','PENTI SULASTRI IRAWAN','XI.RPL-2','Rekayasa Perangkat Lunak',0,0,0),
	(53,'171810198','PUTRI NURSUCI','XI.RPL-2','Rekayasa Perangkat Lunak',0,0,0),
	(54,'171810199','RAVIKA AULIA','XI.RPL-2','Rekayasa Perangkat Lunak',0,0,0),
	(55,'171810200','RENDI NURUL HIDAYATULLOH','XI.RPL-2','Rekayasa Perangkat Lunak',0,0,0),
	(56,'171810201','RESA AMANDA SEPTIANTI','XI.RPL-2','Rekayasa Perangkat Lunak',0,0,0),
	(57,'171810202','RIDWAN NURSALAM','XI.RPL-2','Rekayasa Perangkat Lunak',0,0,0),
	(58,'171810203','RIKA HARNITA','XI.RPL-2','Rekayasa Perangkat Lunak',0,0,0),
	(59,'171810204','RINA ROSTANTIANA','XI.RPL-2','Rekayasa Perangkat Lunak',0,0,0),
	(60,'171810205','RINA SEPTIANI','XI.RPL-2','Rekayasa Perangkat Lunak',0,0,0),
	(61,'171810206','RIZKI FAJAR','XI.RPL-2','Rekayasa Perangkat Lunak',0,0,0),
	(62,'171810207','ROCHMAT SURYA PERMANA','XI.RPL-2','Rekayasa Perangkat Lunak',0,0,0),
	(63,'171810208','SEFIA OKTAFIANI','XI.RPL-2','Rekayasa Perangkat Lunak',0,0,0),
	(64,'171810209','TESA NURLAILA DWI KOMALASARI','XI.RPL-2','Rekayasa Perangkat Lunak',0,0,0),
	(65,'171810210','VIRA SEPTIANDI','XI.RPL-2','Rekayasa Perangkat Lunak',0,0,0),
	(66,'171810211','WINDA WINDIANI','XI.RPL-2','Rekayasa Perangkat Lunak',0,0,0),
	(67,'171810212','YUNI YUHANI','XI.RPL-2','Rekayasa Perangkat Lunak',0,0,0),
	(68,'171810213','YUSI RISNAWATI','XI.RPL-2','Rekayasa Perangkat Lunak',0,0,0),
	(69,'171810214','ANGGI NURHASANAH','XI.RPL-3','Rekayasa Perangkat Lunak',1,0,0),
	(70,'171810215','ATIN NURHAYATIN','XI.RPL-3','Rekayasa Perangkat Lunak',0,0,0),
	(71,'171810216','AYU KARINA','XI.RPL-3','Rekayasa Perangkat Lunak',0,0,0),
	(72,'171810217','AZMI HAMAS HAMDANI','XI.RPL-3','Rekayasa Perangkat Lunak',0,0,0),
	(73,'171810218','ENDANG NUR LESTARI','XI.RPL-3','Rekayasa Perangkat Lunak',0,0,0),
	(74,'171810219','INDRI SRI AISYAH AWALIA','XI.RPL-3','Rekayasa Perangkat Lunak',0,0,0),
	(75,'171810220','INDRIYANI NURWULANDARI','XI.RPL-3','Rekayasa Perangkat Lunak',0,0,0),
	(76,'171810221','JAKIAH NURUL PITROH','XI.RPL-3','Rekayasa Perangkat Lunak',1,0,0),
	(77,'171810222','KHILDA MARDIYYAH','XI.RPL-3','Rekayasa Perangkat Lunak',1,0,0),
	(78,'171810223','MOCHAMMAD FAUZAN MEIDY HIDAYAT','XI.RPL-3','Rekayasa Perangkat Lunak',1,0,1),
	(79,'171810224','MUHAMMAD RIVKY RINALDY FUTRA','XI.RPL-3','Rekayasa Perangkat Lunak',0,0,0),
	(80,'171810225','NISA NURMALASARI','XI.RPL-3','Rekayasa Perangkat Lunak',0,0,0),
	(81,'171810226','NURUL WAHDAH','XI.RPL-3','Rekayasa Perangkat Lunak',0,0,0),
	(82,'171810227','PANI PEBRIANI','XI.RPL-3','Rekayasa Perangkat Lunak',0,0,0),
	(83,'171810228','PEDI MUHAMMAD FAKHRUDIN','XI.RPL-3','Rekayasa Perangkat Lunak',0,0,0),
	(84,'171810229','PRIMA LESMANA','XI.RPL-3','Rekayasa Perangkat Lunak',0,0,0),
	(85,'171810230','RATNA NINGSIH','XI.RPL-3','Rekayasa Perangkat Lunak',0,0,0),
	(86,'171810231','REZA DIKA PRATAMA','XI.RPL-3','Rekayasa Perangkat Lunak',0,0,0),
	(87,'171810232','RIANI SITI NURAENI','XI.RPL-3','Rekayasa Perangkat Lunak',1,0,0),
	(88,'171810233','RIFA FAHIRA','XI.RPL-3','Rekayasa Perangkat Lunak',0,0,0),
	(89,'171810234','RIKI GUNAWAN','XI.RPL-3','Rekayasa Perangkat Lunak',0,0,0),
	(90,'171810235','RINA NURAGNI','XI.RPL-3','Rekayasa Perangkat Lunak',0,0,0),
	(91,'171810236','RIRI PARIHATUL HAYATI','XI.RPL-3','Rekayasa Perangkat Lunak',0,0,0),
	(92,'171810237','RISMA RAHMAWATI','XI.RPL-3','Rekayasa Perangkat Lunak',0,0,0),
	(93,'171810238','RISMA TRI JULIANA','XI.RPL-3','Rekayasa Perangkat Lunak',0,0,0),
	(94,'171810239','RIYAN ANDRIYANA','XI.RPL-3','Rekayasa Perangkat Lunak',0,0,0),
	(95,'171810240','SELPI SRI MULYANI','XI.RPL-3','Rekayasa Perangkat Lunak',0,0,0),
	(96,'171810241','SHERLY YULIASTRY','XI.RPL-3','Rekayasa Perangkat Lunak',0,0,0),
	(97,'171810242','SRI MULYANI','XI.RPL-3','Rekayasa Perangkat Lunak',0,0,0),
	(98,'171810243','TASYA AMELIA PUTRI','XI.RPL-3','Rekayasa Perangkat Lunak',0,0,0),
	(99,'171810244','TRESKA WARIDAH MULYANI','XI.RPL-3','Rekayasa Perangkat Lunak',0,0,0),
	(100,'171810245','WINI ANGGRAENI','XI.RPL-3','Rekayasa Perangkat Lunak',0,0,0),
	(101,'171810246','WULAN DWIYANTI','XI.RPL-3','Rekayasa Perangkat Lunak',0,0,0),
	(102,'171810247','YUDISTIRA MOHAMMAD RIZKI','XI.RPL-3','Rekayasa Perangkat Lunak',1,1,1),
	(103,'171810001','ABDUL AZIZ','XI.TKJ-1','Teknik Komputer dan Jaringan',0,0,0),
	(104,'171810002','AI RIKA KARTIKA ','XI.TKJ-1','Teknik Komputer dan Jaringan',0,0,0),
	(105,'171810003','ANISA AMELIA','XI.TKJ-1','Teknik Komputer dan Jaringan',0,0,0),
	(106,'171810004','ARJUN ZULFIKAR','XI.TKJ-1','Teknik Komputer dan Jaringan',0,0,0),
	(107,'171810005','ASEP IRSYAN','XI.TKJ-1','Teknik Komputer dan Jaringan',0,0,0),
	(108,'171810006','DEA PEBRIYANI','XI.TKJ-1','Teknik Komputer dan Jaringan',0,0,0),
	(109,'171810007','DEDE NURHALIMAH','XI.TKJ-1','Teknik Komputer dan Jaringan',0,0,0),
	(110,'171810008','DENDEN SEFTTIAN','XI.TKJ-1','Teknik Komputer dan Jaringan',0,0,0),
	(111,'171810009','DIANA PERTIWI ','XI.TKJ-1','Teknik Komputer dan Jaringan',0,0,0),
	(112,'171810010','DINDA DEA YULIANINGSIH ','XI.TKJ-1','Teknik Komputer dan Jaringan',0,0,0),
	(113,'171810011','FAHMI FIRMANSYAH','XI.TKJ-1','Teknik Komputer dan Jaringan',0,0,0),
	(114,'171810012','FAKHRIZ MAULANA ','XI.TKJ-1','Teknik Komputer dan Jaringan',0,0,0),
	(115,'171810013','FEBY ANGGRAINI PUTRI MAHENDRA','XI.TKJ-1','Teknik Komputer dan Jaringan',0,0,0),
	(116,'171810015','HANIFAH KHOERUNNISA','XI.TKJ-1','Teknik Komputer dan Jaringan',0,0,0),
	(117,'171810016','IRSAN MUHAMMAD FARID','XI.TKJ-1','Teknik Komputer dan Jaringan',0,0,0),
	(118,'171810017','JAENAL HAMDAN','XI.TKJ-1','Teknik Komputer dan Jaringan',0,0,0),
	(119,'171810018','MARWAH MAWARNI ','XI.TKJ-1','Teknik Komputer dan Jaringan',0,0,0),
	(120,'171810019','MELA SOFA','XI.TKJ-1','Teknik Komputer dan Jaringan',0,0,0),
	(121,'171810020','MUAMAR MUHAMAD SIDIQ','XI.TKJ-1','Teknik Komputer dan Jaringan',0,0,0),
	(122,'171810021','MUHAMMAD LADEN ROJBI NUR','XI.TKJ-1','Teknik Komputer dan Jaringan',0,0,0),
	(123,'171810022','NATASYA FITRIYANI ','XI.TKJ-1','Teknik Komputer dan Jaringan',0,0,0),
	(124,'171810023','NUREKSA KARMINI','XI.TKJ-1','Teknik Komputer dan Jaringan',0,0,0),
	(125,'171810024','NURRISA AWALLUNA ','XI.TKJ-1','Teknik Komputer dan Jaringan',0,0,0),
	(126,'171810025','RISA SEPTIANI ','XI.TKJ-1','Teknik Komputer dan Jaringan',0,0,0),
	(127,'171810026','RISA TRIVANI ','XI.TKJ-1','Teknik Komputer dan Jaringan',0,0,0),
	(128,'171810027','RISWAN SAEPUL ROHMAN','XI.TKJ-1','Teknik Komputer dan Jaringan',0,0,0),
	(129,'171810028','SALIS BILLY NASRULLOH','XI.TKJ-1','Teknik Komputer dan Jaringan',1,0,1),
	(130,'171810029','SALSA PADILA ','XI.TKJ-1','Teknik Komputer dan Jaringan',0,0,0),
	(131,'171810031','SOPI NUR APIPAH ','XI.TKJ-1','Teknik Komputer dan Jaringan',0,0,0),
	(132,'171810032','SRI WIDAYANTI ','XI.TKJ-1','Teknik Komputer dan Jaringan',0,0,0),
	(133,'171810033','SUKMA CAHYA SUMIRAT','XI.TKJ-1','Teknik Komputer dan Jaringan',0,0,0),
	(134,'171810034','TAUPAN ROMDONI','XI.TKJ-1','Teknik Komputer dan Jaringan',0,0,0),
	(135,'171810035','YOSEP ABDUL MUHAEMIN','XI.TKJ-1','Teknik Komputer dan Jaringan',0,0,0),
	(136,'171810036','ZIDNI RAHMATIKA ABADAN','XI.TKJ-1','Teknik Komputer dan Jaringan',1,0,0),
	(137,'171810001','ABDULLAH AZAM NURZAMAN','XI.TKJ-2','Teknik Komputer dan Jaringan',0,0,0),
	(138,'171810002','AFWAN TIZANI','XI.TKJ-2','Teknik Komputer dan Jaringan',0,0,0),
	(139,'171810003','ANA AMELIA ','XI.TKJ-2','Teknik Komputer dan Jaringan',0,0,0),
	(140,'171810004','ANDHITA DHEA WIDYASANI','XI.TKJ-2','Teknik Komputer dan Jaringan',0,0,0),
	(141,'171810005','ANSI FEBRIATI ZULHIZAH','XI.TKJ-2','Teknik Komputer dan Jaringan',0,0,0),
	(142,'171810006','ASHAP MAULANA','XI.TKJ-2','Teknik Komputer dan Jaringan',0,0,0),
	(143,'171810007','CHELSA DWI CAHYANTI UTAMI','XI.TKJ-2','Teknik Komputer dan Jaringan',0,0,0),
	(144,'171810008','DINI NURHAETI ','XI.TKJ-2','Teknik Komputer dan Jaringan',0,0,0),
	(145,'171810009','DINI RAHMAWATI ','XI.TKJ-2','Teknik Komputer dan Jaringan',0,0,0),
	(146,'171810010','GILANG SYIRO DZUDIN','XI.TKJ-2','Teknik Komputer dan Jaringan',0,0,0),
	(147,'171810011','GUNTUR RIZKY FAUZI','XI.TKJ-2','Teknik Komputer dan Jaringan',0,0,0),
	(148,'171810012','HANI YULISTIANI','XI.TKJ-2','Teknik Komputer dan Jaringan',0,0,0),
	(149,'171810013','HEMI NURAENI ','XI.TKJ-2','Teknik Komputer dan Jaringan',0,0,0),
	(150,'171810015','INA SABRINA ADHANI','XI.TKJ-2','Teknik Komputer dan Jaringan',0,0,0),
	(151,'171810016','JAUHARUDDIEN SOFARI','XI.TKJ-2','Teknik Komputer dan Jaringan',0,0,0),
	(152,'171810017','MIRNA MINARTI ','XI.TKJ-2','Teknik Komputer dan Jaringan',0,0,0),
	(153,'171810018','MOHAMAD RIDHO HAPID','XI.TKJ-2','Teknik Komputer dan Jaringan',0,0,0),
	(154,'171810019','MUHAMMAD AKBAR KASYFURRAHMAN','XI.TKJ-2','Teknik Komputer dan Jaringan',0,0,0),
	(155,'171810020','MUHAMMAD FAJAR SIDIQ','XI.TKJ-2','Teknik Komputer dan Jaringan',0,0,0),
	(156,'171810021','NIRA NURAENI','XI.TKJ-2','Teknik Komputer dan Jaringan',0,0,0),
	(157,'171810022','NOVI FITRIANI ','XI.TKJ-2','Teknik Komputer dan Jaringan',0,0,0),
	(158,'171810023','RHEPA RISMAYA ','XI.TKJ-2','Teknik Komputer dan Jaringan',0,0,0),
	(159,'171810024','RIFA FAUZIAH','XI.TKJ-2','Teknik Komputer dan Jaringan',0,0,0),
	(160,'171810025','RIJAL FAUJI','XI.TKJ-2','Teknik Komputer dan Jaringan',0,0,0),
	(161,'171810026','RIVKI RISTAYU','XI.TKJ-2','Teknik Komputer dan Jaringan',0,0,0),
	(162,'171810027','RIZAL RAMLI','XI.TKJ-2','Teknik Komputer dan Jaringan',0,0,0),
	(163,'171810028','ROIHAN MUKTI MUKAROM','XI.TKJ-2','Teknik Komputer dan Jaringan',0,0,0),
	(164,'171810029','SALSABILA AZRA LESTARI','XI.TKJ-2','Teknik Komputer dan Jaringan',0,0,0),
	(165,'171810030','SANTI ','XI.TKJ-2','Teknik Komputer dan Jaringan',0,0,0),
	(166,'171810031','SELA SELVIYANA','XI.TKJ-2','Teknik Komputer dan Jaringan',0,0,0),
	(167,'171810032','SHELIA MEYLANI','XI.TKJ-2','Teknik Komputer dan Jaringan',0,0,0),
	(168,'171810033','WIDA NURAENI','XI.TKJ-2','Teknik Komputer dan Jaringan',0,0,0),
	(169,'171810034','YESI FITRIANI ','XI.TKJ-2','Teknik Komputer dan Jaringan',0,0,0),
	(170,'171810035','YOGAS PRATAMA FEBRIAWAN ','XI.TKJ-2','Teknik Komputer dan Jaringan',0,0,0),
	(171,'171810036','ZAENAL ARIPIN','XI.TKJ-2','Teknik Komputer dan Jaringan',0,0,0),
	(172,'171810073','AANG PAHMI RIJAL','XI.TKJ-3','Teknik Komputer dan Jaringan',0,0,0),
	(173,'171810074','ALI RAMDANI','XI.TKJ-3','Teknik Komputer dan Jaringan',0,0,0),
	(174,'171810075','ANISA APRIANI ','XI.TKJ-3','Teknik Komputer dan Jaringan',0,0,0),
	(175,'171810076','ARI SETIAWAN','XI.TKJ-3','Teknik Komputer dan Jaringan',0,0,0),
	(176,'171810077','CHANDRA SUKMA ADHI SAPUTRA','XI.TKJ-3','Teknik Komputer dan Jaringan',0,0,0),
	(177,'171810078','DEDE ALMAS ','XI.TKJ-3','Teknik Komputer dan Jaringan',0,0,0),
	(178,'171810079','DITA SELVIANA ','XI.TKJ-3','Teknik Komputer dan Jaringan',0,0,0),
	(179,'171810080','ELI LAILATUL AZIZAH','XI.TKJ-3','Teknik Komputer dan Jaringan',0,0,0),
	(180,'171810081','FITRIYAH ','XI.TKJ-3','Teknik Komputer dan Jaringan',0,0,0),
	(181,'171810082','HILMA LUTFIA','XI.TKJ-3','Teknik Komputer dan Jaringan',0,0,0),
	(182,'171810083','INDAH SITI NURJANAH ','XI.TKJ-3','Teknik Komputer dan Jaringan',0,0,0),
	(183,'171810084','JULFANI HIDAYAT','XI.TKJ-3','Teknik Komputer dan Jaringan',0,0,0),
	(184,'171810085','MUHAMAD RAMDAN ','XI.TKJ-3','Teknik Komputer dan Jaringan',0,0,0),
	(185,'171810086','MUHAMAD ZIDAN DARUL ILMI','XI.TKJ-3','Teknik Komputer dan Jaringan',0,0,0),
	(186,'171810087','MUHAMMAD NOVADIAN ALFAIZHA','XI.TKJ-3','Teknik Komputer dan Jaringan',0,0,0),
	(187,'171810088','MUHAMMAD SIDIK PERMANA AGUNG','XI.TKJ-3','Teknik Komputer dan Jaringan',0,0,0),
	(188,'171810089','NISA AVIFAH','XI.TKJ-3','Teknik Komputer dan Jaringan',0,0,0),
	(189,'171810090','NIZAR SALAM','XI.TKJ-3','Teknik Komputer dan Jaringan',0,0,0),
	(190,'171810091','NURUL INDAH','XI.TKJ-3','Teknik Komputer dan Jaringan',0,0,0),
	(191,'171810092','PINO TASBIT RAHMAN ','XI.TKJ-3','Teknik Komputer dan Jaringan',0,0,0),
	(192,'171810093','PUTRI MEGA UTAMI','XI.TKJ-3','Teknik Komputer dan Jaringan',0,0,0),
	(193,'171810094','PUTRIANY DEWI','XI.TKJ-3','Teknik Komputer dan Jaringan',0,0,0),
	(194,'171810095','RETNO GUNAWAN','XI.TKJ-3','Teknik Komputer dan Jaringan',0,0,0),
	(195,'171810096','RIDHO NAUFAL FERRAR','XI.TKJ-3','Teknik Komputer dan Jaringan',0,0,0),
	(196,'171810097','RINI NURAENI ','XI.TKJ-3','Teknik Komputer dan Jaringan',0,0,0),
	(197,'171810098','RISDA NURHASANAH ','XI.TKJ-3','Teknik Komputer dan Jaringan',0,0,0),
	(198,'171810099','RIVAN RIZKIA MAULANA','XI.TKJ-3','Teknik Komputer dan Jaringan',0,0,0),
	(199,'171810100','RYFKY HENDRY FIRDAUS','XI.TKJ-3','Teknik Komputer dan Jaringan',0,0,0),
	(200,'171810101','SANI BUDIAWAN','XI.TKJ-3','Teknik Komputer dan Jaringan',0,0,0),
	(201,'171810102','SHANTI RAHMAWATI','XI.TKJ-3','Teknik Komputer dan Jaringan',0,0,0),
	(202,'171810103','SHINTIA GUSTIAN ','XI.TKJ-3','Teknik Komputer dan Jaringan',0,0,0),
	(203,'171810104','SITI ARDIYANINGSIH','XI.TKJ-3','Teknik Komputer dan Jaringan',0,0,0),
	(204,'171810105','SYAHRIEL AKBAR FATHIA','XI.TKJ-3','Teknik Komputer dan Jaringan',0,0,0),
	(205,'171810106','WINDI','XI.TKJ-3','Teknik Komputer dan Jaringan',0,0,0),
	(206,'171810107','WINDI HERDIYANTI','XI.TKJ-3','Teknik Komputer dan Jaringan',0,0,0),
	(207,'171810108','ZAIDAN NAUFAL','XI.TKJ-3','Teknik Komputer dan Jaringan',0,0,0),
	(208,'171810109','ADITYA SANI FIRDAUS','XI.TKJ-4','Teknik Komputer dan Jaringan',0,0,0),
	(209,'171810111','AGUSTIN EKA PUTRA SIAHAAN','XI.TKJ-4','Teknik Komputer dan Jaringan',0,0,0),
	(210,'171810112','AYU SYIFA UTAMI ','XI.TKJ-4','Teknik Komputer dan Jaringan',0,0,0),
	(211,'171810113','CHELSY SRI PEBRIANTI UTAMI','XI.TKJ-4','Teknik Komputer dan Jaringan',0,0,0),
	(212,'171810114','DENISA FITRI SARI','XI.TKJ-4','Teknik Komputer dan Jaringan',0,0,0),
	(213,'171810115','DEWI NURFITRI ','XI.TKJ-4','Teknik Komputer dan Jaringan',0,0,0),
	(214,'171810116','DIKA RAKA PAMUNGKAS','XI.TKJ-4','Teknik Komputer dan Jaringan',0,0,0),
	(215,'171810117','DZIKRI DZIKRULILLAH','XI.TKJ-4','Teknik Komputer dan Jaringan',0,0,0),
	(216,'171810118','EDWIN MULYANA NAPITUPULU ','XI.TKJ-4','Teknik Komputer dan Jaringan',0,0,0),
	(217,'171810119','FAHRUL RIFANKHOIR','XI.TKJ-4','Teknik Komputer dan Jaringan',0,0,0),
	(218,'171810120','FAJAR SIDIK','XI.TKJ-4','Teknik Komputer dan Jaringan',0,0,0),
	(219,'171810121','HERDIS HERDIANSAH ','XI.TKJ-4','Teknik Komputer dan Jaringan',0,0,0),
	(220,'171810122','HUSNI AL GOZALI PUTRA','XI.TKJ-4','Teknik Komputer dan Jaringan',0,0,0),
	(221,'171810123','IKMAL MAULANA','XI.TKJ-4','Teknik Komputer dan Jaringan',0,0,0),
	(222,'171810124','INDRIYATUL ASYIAH ','XI.TKJ-4','Teknik Komputer dan Jaringan',0,0,0),
	(223,'171810126','MUHAMMAD ABDUL JABBAR','XI.TKJ-4','Teknik Komputer dan Jaringan',0,0,0),
	(224,'171810127','MUHAMMAD SILDAN RISWANDA GUNAWAN ','XI.TKJ-4','Teknik Komputer dan Jaringan',0,0,0),
	(225,'171810128','NENG DETI ROPIANI DIANSAH','XI.TKJ-4','Teknik Komputer dan Jaringan',0,0,0),
	(226,'171810129','NUR HIDAYATULLOH','XI.TKJ-4','Teknik Komputer dan Jaringan',0,0,0),
	(227,'171810130','RIAN HARIANTO','XI.TKJ-4','Teknik Komputer dan Jaringan',0,0,0),
	(228,'171810131','RIFAN JAELANI ','XI.TKJ-4','Teknik Komputer dan Jaringan',0,0,0),
	(229,'171810133','RIVA AWALIA PUTRIANI','XI.TKJ-4','Teknik Komputer dan Jaringan',0,0,0),
	(230,'171810134','RIVAL MIDARUL PALAH ','XI.TKJ-4','Teknik Komputer dan Jaringan',0,0,0),
	(231,'171810135','RIZWAR RAIS FAISAL','XI.TKJ-4','Teknik Komputer dan Jaringan',0,0,0),
	(232,'171810136','ROSA ROSMAWATI','XI.TKJ-4','Teknik Komputer dan Jaringan',0,0,0),
	(233,'171810137','SERLI SAHRIJA ','XI.TKJ-4','Teknik Komputer dan Jaringan',0,0,0),
	(234,'171810138','SITI ROBIAH ADAWIYAH','XI.TKJ-4','Teknik Komputer dan Jaringan',0,0,0),
	(235,'171810139','SOFI FITRIYANI','XI.TKJ-4','Teknik Komputer dan Jaringan',0,0,0),
	(236,'171810140','SOPIAH ','XI.TKJ-4','Teknik Komputer dan Jaringan',0,0,0),
	(237,'171810141','SULIS FITRIANI','XI.TKJ-4','Teknik Komputer dan Jaringan',0,0,0),
	(238,'171810143','WINI WINDARTI','XI.TKJ-4','Teknik Komputer dan Jaringan',0,0,0),
	(239,'171810144','YOGI','XI.TKJ-4','Teknik Komputer dan Jaringan',0,0,0);

/*!40000 ALTER TABLE `master_siswa` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
