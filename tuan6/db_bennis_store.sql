-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 12, 2024 at 08:08 PM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `db_bennis_store`
--

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `customer_id` int(11) NOT NULL,
  `first_name` varchar(255) default NULL,
  `last_name` varchar(255) default NULL,
  `email` varchar(255) default NULL,
  `phone_number` varchar(20) default NULL,
  PRIMARY KEY  (`customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`customer_id`, `first_name`, `last_name`, `email`, `phone_number`) VALUES
(1, 'John', 'Doe', 'johndoe@example.com', '1234567890'),
(2, 'Jane', 'Smith', 'janesmith@example.com', '9876543210'),
(3, 'Michael', 'Johnson', 'michaeljohnson@example.com', '5555555555'),
(4, 'Emily', 'Davis', 'emilydavis@example.com', '7777777777'),
(5, 'David', 'Wilson', 'davidwilson@example.com', '9999999999'),
(6, 'Sarah', 'Anderson', 'sarahanderson@example.com', '4444444444'),
(7, 'Jessica', 'Thomas', 'jessicathomas@example.com', '2222222222'),
(8, 'Christopher', 'Martinez', 'christophermartinez@example.com', '6666666666'),
(9, 'Michelle', 'Harris', 'michelleharris@example.com', '1111111111'),
(10, 'Daniel', 'Taylor', 'danieltaylor@example.com', '8888888888');

-- --------------------------------------------------------

--
-- Table structure for table `employees`
--

CREATE TABLE `employees` (
  `employee_id` int(11) NOT NULL auto_increment,
  `full_name` varchar(255) default NULL,
  `home_town` varchar(255) default NULL,
  `email` varchar(255) default NULL,
  `phone_number` varchar(20) default NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY  (`employee_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=15 ;

--
-- Dumping data for table `employees`
--

INSERT INTO `employees` (`employee_id`, `full_name`, `home_town`, `email`, `phone_number`, `password`) VALUES
(1, 'Mark', 'Johnson', 'markjohnson@example.com', '1111111111', 'ae94be3cd532ce4a025884819eb08c98'),
(2, 'Lisa', 'Smith', 'lisasmith@example.com', '2222222222', '5eb407a8eb9aca31c083cf05550fa62c'),
(3, 'David', 'Anderson', 'davidanderson@example.com', '3333333333', '5eb407a8eb9aca31c083cf05550fa62c'),
(4, 'Emily', 'Davis', 'emilydavis@example.com', '4444444444', '810d6ddb908203a73841bed95f79691c'),
(5, 'Daniel', 'Wilson', 'danielwilson@example.com', '5555555555', '810d6ddb908203a73841bed95f79691c'),
(6, 'Sarah', 'Taylor', 'sarahtaylor@example.com', '6666666666', '5eb407a8eb9aca31c083cf05550fa62c'),
(7, 'Michael', 'Thomas', 'michaelthomas@example.com', '7777777777', 'ae94be3cd532ce4a025884819eb08c98'),
(8, 'Jessica', 'Martinez', 'jessicamartinez@example.com', '8888888888', '5eb407a8eb9aca31c083cf05550fa62c'),
(9, 'Christopher', 'Harris', 'christopherharris@example.com', '9999999999', '810d6ddb908203a73841bed95f79691c'),
(13, 'Võ Nguyễn Hoành Hợp', 'Đà Nẵng', 'hopboy553@gmail.com', '0911576456', '202cb962ac59075b964b07152d234b70'),
(14, 'Võ Nguyễn Hoành Hợp', 'Thành phố Hồ Chí Minh', 'hopboy2003@gmail.com', '0911576456', '2cfd4560539f887a5e420412b370b361');

-- --------------------------------------------------------

--
-- Table structure for table `inventory`
--

CREATE TABLE `inventory` (
  `inventory_id` int(11) NOT NULL,
  `car_id` int(11) default NULL,
  `quantity` int(11) default NULL,
  `location` varchar(255) default NULL,
  PRIMARY KEY  (`inventory_id`),
  KEY `car_id` (`car_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `inventory`
--

INSERT INTO `inventory` (`inventory_id`, `car_id`, `quantity`, `location`) VALUES
(1, 1, 2, 'Los Angeles'),
(2, 2, 1, 'New York'),
(3, 3, 3, 'Chicago'),
(4, 4, 1, 'Miami'),
(5, 5, 2, 'San Francisco'),
(6, 6, 1, 'Dallas'),
(7, 7, 2, 'Houston'),
(8, 8, 1, 'Seattle'),
(9, 9, 3, 'Atlanta'),
(10, 10, 2, 'Boston');

-- --------------------------------------------------------

--
-- Table structure for table `sales`
--

CREATE TABLE `sales` (
  `sale_id` int(11) NOT NULL,
  `car_id` int(11) default NULL,
  `customer_id` int(11) default NULL,
  `employee_id` int(11) default NULL,
  `sale_date` date default NULL,
  `commission` decimal(10,2) default NULL,
  PRIMARY KEY  (`sale_id`),
  KEY `car_id` (`car_id`),
  KEY `customer_id` (`customer_id`),
  KEY `employee_id` (`employee_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `sales`
--

INSERT INTO `sales` (`sale_id`, `car_id`, `customer_id`, `employee_id`, `sale_date`, `commission`) VALUES
(1, 1, 1, 1, '2023-01-15', '100000.00'),
(2, 2, 2, 3, '2023-02-20', '90000.00'),
(3, 3, 3, 2, '2023-03-10', '120000.00'),
(4, 4, 4, 1, '2023-04-05', '75000.00'),
(5, 5, 5, 4, '2023-05-12', '110000.00'),
(6, 6, 6, 2, '2023-06-18', '160000.00'),
(7, 7, 7, 3, '2023-07-22', '180000.00'),
(8, 8, 8, 1, '2023-08-08', '150000.00'),
(9, 9, 9, 4, '2023-09-03', '80000.00'),
(10, 10, 10, 2, '2023-10-30', '100000.00');

-- --------------------------------------------------------

--
-- Table structure for table `servicehistory`
--

CREATE TABLE `servicehistory` (
  `service_id` int(11) NOT NULL,
  `car_id` int(11) default NULL,
  `service_date` date default NULL,
  `service_type` varchar(255) default NULL,
  `service_cost` decimal(10,2) default NULL,
  PRIMARY KEY  (`service_id`),
  KEY `car_id` (`car_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `servicehistory`
--

INSERT INTO `servicehistory` (`service_id`, `car_id`, `service_date`, `service_type`, `service_cost`) VALUES
(1, 1, '2023-02-05', 'Oil Change', '200.00'),
(2, 2, '2023-03-12', 'Tire Rotation', '150.00'),
(3, 3, '2023-04-10', 'Brake Replacement', '500.00'),
(4, 4, '2023-05-20', 'Engine Tune-up', '300.00'),
(5, 5, '2023-06-18', 'Wheel Alignment', '200.00'),
(6, 6, '2023-07-25', 'Air Conditioning Repair', '400.00'),
(7, 7, '2023-08-12', 'Electrical Repair', '350.00'),
(8, 8, '2023-09-05', 'Transmission Fluid Change', '250.00'),
(9, 9, '2023-10-15', 'Battery Replacement', '150.00'),
(10, 10, '2023-11-20', 'Suspension Repair', '600.00');

-- --------------------------------------------------------

--
-- Table structure for table `supercars`
--

CREATE TABLE `supercars` (
  `car_id` int(11) NOT NULL auto_increment,
  `brand` varchar(255) default NULL,
  `model` varchar(255) default NULL,
  `price` decimal(10,2) default NULL,
  `year` int(11) default NULL,
  `img` varchar(50) default NULL,
  PRIMARY KEY  (`car_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=26 ;

--
-- Dumping data for table `supercars`
--

INSERT INTO `supercars` (`car_id`, `brand`, `model`, `price`, `year`, `img`) VALUES
(1, 'Ferrari', 'LaFerrari', '3000000.00', 2022, 'LaFerrari.jpg'),
(2, 'Lamborghini', 'Aventador SVJ 2023', '2800000.00', 2023, 'Aventador SVJ.jpg'),
(3, 'Bugatti', 'Chiron', '4000000.00', 2022, 'Chiron.jpg'),
(4, 'Porsche', '911 GT2 RS', '1500000.00', 2022, '911 GT2 RS.jpg'),
(5, 'McLaren', 'P1', '2000000.00', 2022, 'P1.jpg'),
(6, 'Aston Martin', 'Valkyrie 2023', '3500000.00', 2023, 'Valkyrie.jpg'),
(7, 'Koenigsegg', 'Jesko', '4500000.00', 2022, 'Jesko.jpg'),
(8, 'Pagani', 'Huayra BC', '3800000.00', 2022, 'Huayra BC.avif'),
(9, 'Ferrari', '812 Superfast', '1000000.00', 2023, '812 Superfast.jpg'),
(10, 'Lamborghini', 'Huracan Performante', '2500000.00', 2022, 'Huracan Performante.jpg'),
(11, 'Lamborghini', 'Aventador SVJ 2024', '517700.00', 2024, 'Aventador SVJ 2024.jpg'),
(12, 'Lamborghini', 'Aventador S Coupe', '425000.00', 2024, 'Aventador S Coupe.jpg'),
(14, 'Lamborghini', 'Huracan Performante Coupe', '278000.00', 2024, 'Huracan Performante Coupe.jpg'),
(16, 'Lamborghini', 'Sian SKP 37', '54000000.00', 2024, 'Sian SKP 37.jpg'),
(17, 'Lamborghini', 'Urus', '222000.00', 2024, 'Urus.jpg'),
(18, 'Aston Martin', 'Valhalla', '1300000.00', 2024, 'Aston Martin Valhalla.jpg'),
(19, 'Aston Martin', 'Valkyrie', '3500000.00', 2024, 'Aston Martin Valkyrie 2024.jpg'),
(20, 'Aston Martin', 'DBS Superleggera Volante', '337525.00', 2024, 'Aston Martin DBS Superleggera Volante.jpg'),
(21, 'Aston Martin', 'DBS Superleggera Coupe', '319125.00', 2024, 'DBS Superleggera Coupe.jpg'),
(22, 'Koenigsegg', 'Regera', '5500000.00', 2024, 'Regera.jpg'),
(23, 'Koenigsegg', 'Agera R', '2100000.00', 2024, 'Agera R.jpg'),
(24, 'Koenigsegg', 'Agera RS', '2100000.00', 2024, 'Agera RS.jpg'),
(25, 'BMW', 'i5', '66800.00', 2024, 'i5.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `transactions`
--

CREATE TABLE `transactions` (
  `transaction_id` int(11) NOT NULL,
  `customer_id` int(11) default NULL,
  `car_id` int(11) default NULL,
  `transaction_date` date default NULL,
  `employee_id` int(11) default NULL,
  `amount` decimal(10,2) default NULL,
  PRIMARY KEY  (`transaction_id`),
  KEY `customer_id` (`customer_id`),
  KEY `car_id` (`car_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `transactions`
--

INSERT INTO `transactions` (`transaction_id`, `customer_id`, `car_id`, `transaction_date`, `employee_id`, `amount`) VALUES
(1, 1, 1, '2023-01-15', 2, '500000.00'),
(2, 2, 2, '2023-02-20', 3, '400000.00'),
(3, 3, 3, '2023-03-10', 1, '600000.00'),
(4, 4, 4, '2023-04-05', 4, '350000.00'),
(5, 5, 5, '2023-05-12', 2, '450000.00'),
(6, 6, 6, '2023-06-18', 1, '550000.00'),
(7, 7, 7, '2023-07-22', 3, '700000.00'),
(8, 8, 8, '2023-08-08', 1, '600000.00'),
(9, 9, 9, '2023-09-03', 4, '400000.00'),
(10, 10, 10, '2023-10-30', 2, '500000.00');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `inventory`
--
ALTER TABLE `inventory`
  ADD CONSTRAINT `inventory_ibfk_1` FOREIGN KEY (`car_id`) REFERENCES `supercars` (`car_id`);

--
-- Constraints for table `sales`
--
ALTER TABLE `sales`
  ADD CONSTRAINT `sales_ibfk_1` FOREIGN KEY (`car_id`) REFERENCES `supercars` (`car_id`),
  ADD CONSTRAINT `sales_ibfk_2` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`customer_id`),
  ADD CONSTRAINT `sales_ibfk_3` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`employee_id`);

--
-- Constraints for table `servicehistory`
--
ALTER TABLE `servicehistory`
  ADD CONSTRAINT `servicehistory_ibfk_1` FOREIGN KEY (`car_id`) REFERENCES `supercars` (`car_id`);

--
-- Constraints for table `transactions`
--
ALTER TABLE `transactions`
  ADD CONSTRAINT `transactions_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`customer_id`),
  ADD CONSTRAINT `transactions_ibfk_2` FOREIGN KEY (`car_id`) REFERENCES `supercars` (`car_id`);
