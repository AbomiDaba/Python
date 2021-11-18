-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema belt_exam
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `belt_exam` ;

-- -----------------------------------------------------
-- Schema belt_exam
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `belt_exam` DEFAULT CHARACTER SET utf8 ;
USE `belt_exam` ;

-- -----------------------------------------------------
-- Table `belt_exam`.`users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `belt_exam`.`users` ;

CREATE TABLE IF NOT EXISTS `belt_exam`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `belt_exam`.`bands`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `belt_exam`.`bands` ;

CREATE TABLE IF NOT EXISTS `belt_exam`.`bands` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `genre` VARCHAR(255) NULL,
  `city` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_bands_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_bands_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `belt_exam`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
