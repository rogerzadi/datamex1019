-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema my_sql
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema my_sql
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `my_sql` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `my_sql` ;

-- -----------------------------------------------------
-- Table `my_sql`.`cars`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `my_sql`.`cars` (
  `idCars` INT(11) NOT NULL,
  `VIN` INT(11) NULL DEFAULT NULL,
  `Model` VARCHAR(45) NULL DEFAULT NULL,
  `Year` VARCHAR(45) NULL DEFAULT NULL,
  `Color` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`idCars`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `my_sql`.`Invoices`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `my_sql`.`Invoices` (
  `idInvoices` INT NOT NULL,
  `Date` DATE NULL,
  `Car` VARCHAR(45) NULL,
  `Salesperson` VARCHAR(45) NULL,
  `cars_idCars` INT(11) NOT NULL,
  PRIMARY KEY (`idInvoices`),
  INDEX `fk_Invoices_cars_idx` (`cars_idCars` ASC) VISIBLE,
  CONSTRAINT `fk_Invoices_cars`
    FOREIGN KEY (`cars_idCars`)
    REFERENCES `my_sql`.`cars` (`idCars`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `my_sql`.`Customers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `my_sql`.`Customers` (
  `idCustomers` INT NOT NULL,
  `Name` VARCHAR(45) NULL,
  `Phone Number` INT NULL,
  `Email` VARCHAR(45) NULL,
  `City` VARCHAR(45) NULL,
  `Country` VARCHAR(45) NULL,
  `ZIP` INT NULL,
  `Invoices_idInvoices` INT NOT NULL,
  PRIMARY KEY (`idCustomers`, `Invoices_idInvoices`),
  INDEX `fk_Customers_Invoices1_idx` (`Invoices_idInvoices` ASC) VISIBLE,
  CONSTRAINT `fk_Customers_Invoices1`
    FOREIGN KEY (`Invoices_idInvoices`)
    REFERENCES `my_sql`.`Invoices` (`idInvoices`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `my_sql`.`Salespersons`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `my_sql`.`Salespersons` (
  `idSalespersons` INT NOT NULL,
  `Name` VARCHAR(45) NULL,
  `Store` VARCHAR(45) NULL,
  `Customers_idCustomers` INT NOT NULL,
  `Invoices_idInvoices` INT NOT NULL,
  PRIMARY KEY (`idSalespersons`, `Customers_idCustomers`, `Invoices_idInvoices`),
  INDEX `fk_Salespersons_Customers1_idx` (`Customers_idCustomers` ASC) VISIBLE,
  INDEX `fk_Salespersons_Invoices1_idx` (`Invoices_idInvoices` ASC) VISIBLE,
  CONSTRAINT `fk_Salespersons_Customers1`
    FOREIGN KEY (`Customers_idCustomers`)
    REFERENCES `my_sql`.`Customers` (`idCustomers`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Salespersons_Invoices1`
    FOREIGN KEY (`Invoices_idInvoices`)
    REFERENCES `my_sql`.`Invoices` (`idInvoices`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
