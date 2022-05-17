-- -----------------------------------------------------
-- Create Schema 'mag_piese.bd'
-- -----------------------------------------------------
CREATE SCHEMA `mag_piese.bd` ;

-- -----------------------------------------------------
-- Create Table 'locuri_munca'
-- -----------------------------------------------------
CREATE TABLE `mag_piese.bd`.`locuri_munca` (
  `id_loc_munca` INT NOT NULL AUTO_INCREMENT,
  `denumire` VARCHAR(45) NOT NULL,
  `salariu_min` INT UNSIGNED NOT NULL,
  `salariu_max` INT UNSIGNED NULL,
  PRIMARY KEY (`id_loc_munca`));

-- -----------------------------------------------------
-- Create Table 'angajati'
-- -----------------------------------------------------
CREATE TABLE `mag_piese.bd`.`angajati` (
  `id_angajat` INT NOT NULL AUTO_INCREMENT,
  `nume_familie` VARCHAR(45) NOT NULL,
  `prenume` VARCHAR(45) NOT NULL,
  `salariu` INT UNSIGNED NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `data_angajare` DATE NOT NULL,
  `data_nastere` DATE NOT NULL,
  `loc_munca` INT NOT NULL,
  PRIMARY KEY (`id_angajat`),
  INDEX `loc_munca_idx` (`loc_munca` ASC) VISIBLE,
  CONSTRAINT `loc_munca`
    FOREIGN KEY (`loc_munca`)
    REFERENCES `mag_piese.bd`.`locuri_munca` (`id_loc_munca`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT);
    
-- -----------------------------------------------------
-- Create Table 'adrese'
-- -----------------------------------------------------
CREATE TABLE `mag_piese.bd`.`adrese` (
  `id_adresa` INT NOT NULL AUTO_INCREMENT,
  `tara` VARCHAR(45) NOT NULL,
  `judet` VARCHAR(45) NOT NULL,
  `localitate` VARCHAR(45) NOT NULL,
  `strada` VARCHAR(45) NOT NULL,
  `nr_strada` INT UNSIGNED NOT NULL,
  `bloc` INT UNSIGNED NULL,
  `scara` VARCHAR(10) NULL,
  `etaj` INT UNSIGNED NULL,
  `apartament` INT UNSIGNED NULL,
  PRIMARY KEY (`id_adresa`));

-- -----------------------------------------------------
-- Create Table 'clienti'
-- -----------------------------------------------------
CREATE TABLE `mag_piese.bd`.`clienti` (
  `cnp` VARCHAR(13) NOT NULL,
  `nume_familie` VARCHAR(45) NOT NULL,
  `prenume` VARCHAR(45) NOT NULL,
  `nr_telefon` VARCHAR(412) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`cnp`));

-- -----------------------------------------------------
-- Create Table 'masini'
-- -----------------------------------------------------
CREATE TABLE `mag_piese.bd`.`masini` (
  `vin` VARCHAR(17) NOT NULL,
  `nr_inmatriculare` VARCHAR(10) NOT NULL,
  `an_fabricatie` YEAR NOT NULL,
  `kilometraj` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`vin`));
  
-- -----------------------------------------------------
-- Create Table 'modele_masini'
-- -----------------------------------------------------
CREATE TABLE `mag_piese.bd`.`modele_masini` (
  `id_model` INT NOT NULL AUTO_INCREMENT,
  `marca` VARCHAR(45) NOT NULL,
  `model` VARCHAR(45) NOT NULL,
  `an_incepere_fabricatie` YEAR NOT NULL,
  `an_finalizare_fabricatie` YEAR NOT NULL,
  `motorizare_cc` INT UNSIGNED NULL,
  `putere_cp` INT UNSIGNED NOT NULL,
  `combustibil` ENUM('benzina', 'diesel', 'hybrid-benzina', 'hybrid-diesel', 'electric', 'hidrogen') NOT NULL,
  `cod_motor` VARCHAR(10) NOT NULL DEFAULT 'nu exista',
  `tip_tractiune` ENUM('fata', 'spare', '4x4') NOT NULL,
  PRIMARY KEY (`id_model`));

-- -----------------------------------------------------
-- Create Table 'piese'
-- -----------------------------------------------------
CREATE TABLE `mag_piese.bd`.`piese` (
  `id_piesa` INT NOT NULL AUTO_INCREMENT,
  `denumire_piesa` VARCHAR(45) NOT NULL,
  `producator` VARCHAR(45) NOT NULL,
  `interval_recomandat_schimb` VARCHAR(45) NOT NULL DEFAULT 'nu exista',
  `pret_ron` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id_piesa`, `pret_ron`));

-- -----------------------------------------------------
-- Create Table 'piesa_model'
-- -----------------------------------------------------
CREATE TABLE `mag_piese.bd`.`piesa_model` (
  `id_piesa` INT NOT NULL,
  `id_model` INT NOT NULL,
  `originala` ENUM('originala', 'compatibila') NOT NULL DEFAULT 'originala',
  PRIMARY KEY (`id_piesa`, `id_model`),
  INDEX `id_model_idx` (`id_model` ASC) VISIBLE,
  CONSTRAINT `id_piesa`
    FOREIGN KEY (`id_piesa`)
    REFERENCES `mag_piese.bd`.`piese` (`id_piesa`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `id_model`
    FOREIGN KEY (`id_model`)
    REFERENCES `mag_piese.bd`.`modele_masini` (`id_model`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);

-- -----------------------------------------------------
-- Create Table 'comenzi'
-- -----------------------------------------------------
CREATE TABLE `mag_piese.bd`.`comenzi` (
  `id_comanda` INT NOT NULL AUTO_INCREMENT,
  `data_comanda` DATE NOT NULL,
  `masina` VARCHAR(17) NOT NULL,
  `client` VARCHAR(13) NOT NULL,
  `pregatita_de_angajat` INT NOT NULL,
  `tip_livrare` ENUM('ridicare personala', 'livrare') NOT NULL DEFAULT 'ridicare personala',
  `status_comanda` ENUM('plasata', 'pregatita pentru ridicare', 'in curs de livrare', 'ridicata', 'livrata') NOT NULL DEFAULT 'plasata',
  PRIMARY KEY (`id_comanda`),
  INDEX `masina_idx` (`masina` ASC) VISIBLE,
  INDEX `client_idx` (`client` ASC) VISIBLE,
  INDEX `pregatita_de_angajat_idx` (`pregatita_de_angajat` ASC) VISIBLE,
  CONSTRAINT `masina`
    FOREIGN KEY (`masina`)
    REFERENCES `mag_piese.bd`.`masini` (`vin`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT,
  CONSTRAINT `client`
    FOREIGN KEY (`client`)
    REFERENCES `mag_piese.bd`.`clienti` (`cnp`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT,
  CONSTRAINT `pregatita_de_angajat`
    FOREIGN KEY (`pregatita_de_angajat`)
    REFERENCES `mag_piese.bd`.`angajati` (`id_angajat`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT);

-- -----------------------------------------------------
-- Create Table 'comanda_piesa'
-- -----------------------------------------------------
CREATE TABLE `mag_piese.bd`.`comanda_piesa` (
  `id-comanda` INT NOT NULL,
  `id-piesa` INT NOT NULL,
  `nr_piese` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id-comanda`, `id-piesa`),
  INDEX `id_piesa_idx` (`id-piesa` ASC) VISIBLE,
  CONSTRAINT `id-comanda`
    FOREIGN KEY (`id-comanda`)
    REFERENCES `mag_piese.bd`.`comenzi` (`id_comanda`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `id-piesa`
    FOREIGN KEY (`id-piesa`)
    REFERENCES `mag_piese.bd`.`piese` (`id_piesa`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);

-- -----------------------------------------------------
-- Create Table 'livrari'
-- -----------------------------------------------------
CREATE TABLE `mag_piese.bd`.`livrari` (
  `AWB` VARCHAR(20) NOT NULL,
  `livrata_de_angajat` INT NOT NULL,
  `comanda` INT NOT NULL,
  `adresa` INT NOT NULL,
  `status_livrare` ENUM('primita', 'in curs de livrare', 'livrata') NOT NULL DEFAULT 'primita',
  `data_programata_livrare` DATE NOT NULL,
  PRIMARY KEY (`AWB`),
  INDEX `livrata_de_angajat_idx` (`livrata_de_angajat` ASC) VISIBLE,
  INDEX `comanda_idx` (`comanda` ASC) VISIBLE,
  INDEX `adresa_idx` (`adresa` ASC) VISIBLE,
  CONSTRAINT `livrata_de_angajat`
    FOREIGN KEY (`livrata_de_angajat`)
    REFERENCES `mag_piese.bd`.`angajati` (`id_angajat`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT,
  CONSTRAINT `comanda`
    FOREIGN KEY (`comanda`)
    REFERENCES `mag_piese.bd`.`comenzi` (`id_comanda`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `adresa`
    FOREIGN KEY (`adresa`)
    REFERENCES `mag_piese.bd`.`adrese` (`id_adresa`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT);

-- -----------------------------------------------------
-- POPULAREA TABELELOR ---------------------------------
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Populate Table 'locuri_munca'
-- -----------------------------------------------------
INSERT INTO `mag_piese.bd`.`locuri_munca` (`denumire`, `salariu_min`, `salariu_max`) VALUES ('programator', '3000', '6000');
INSERT INTO `mag_piese.bd`.`locuri_munca` (`denumire`, `salariu_min`, `salariu_max`) VALUES ('programator-ajutor', '1000', '2000');
INSERT INTO `mag_piese.bd`.`locuri_munca` (`denumire`, `salariu_min`, `salariu_max`) VALUES ('curier', '2312', '3132');
INSERT INTO `mag_piese.bd`.`locuri_munca` (`denumire`, `salariu_min`, `salariu_max`) VALUES ('staff', '1500', '3000');
INSERT INTO `mag_piese.bd`.`locuri_munca` (`denumire`, `salariu_min`, `salariu_max`) VALUES ('manipulant', '1800', '3300');
INSERT INTO `mag_piese.bd`.`locuri_munca` (`denumire`, `salariu_min`, `salariu_max`) VALUES ('manager de magazin', '3500', '5500');
INSERT INTO `mag_piese.bd`.`locuri_munca` (`denumire`, `salariu_min`, `salariu_max`) VALUES ('it-ist', '2700', '4800');

-- -----------------------------------------------------
-- Populate Table 'angajati'
-- -----------------------------------------------------
INSERT INTO `mag_piese.bd`.`angajati` (`nume_familie`, `prenume`, `salariu`, `email`, `data_angajare`, `data_nastere`, `loc_munca`) VALUES ('Costea', 'Marian', '2400', 'costea.marian@yahoo.com', '2019-03-01', '1987-07-08', '3');
INSERT INTO `mag_piese.bd`.`angajati` (`nume_familie`, `prenume`, `salariu`, `email`, `data_angajare`, `data_nastere`, `loc_munca`) VALUES ('Popescu', 'Ion', '2700', 'popescu.ion@yahoo.com', '2019-05-23', '1987-09-23', '4');
INSERT INTO `mag_piese.bd`.`angajati` (`nume_familie`, `prenume`, `salariu`, `email`, `data_angajare`, `data_nastere`, `loc_munca`) VALUES ('Cristescu', 'Maria', '3030', 'cristescu.maria@yahoo.com', '2020-11-20', '1992-04-02', '1');
INSERT INTO `mag_piese.bd`.`angajati` (`nume_familie`, `prenume`, `salariu`, `email`, `data_angajare`, `data_nastere`, `loc_munca`) VALUES ('Macovei', 'Tudor', '4322', 'macovei.tudor@yahoo.com', '2022-12-23', '2000-02-05', '1');
INSERT INTO `mag_piese.bd`.`angajati` (`nume_familie`, `prenume`, `salariu`, `email`, `data_angajare`, `data_nastere`, `loc_munca`) VALUES ('Munteanu', 'Florin', '1700', 'munteanu.florin@gmail.com', '2022-11-28', '2001-06-05', '4');
INSERT INTO `mag_piese.bd`.`angajati` (`nume_familie`, `prenume`, `salariu`, `email`, `data_angajare`, `data_nastere`, `loc_munca`) VALUES ('Mihai', 'Bogdan', '3000', 'mihai.bogdan@gmail.com', '2021-06-01', '2001-02-05', '3');
INSERT INTO `mag_piese.bd`.`angajati` (`nume_familie`, `prenume`, `salariu`, `email`, `data_angajare`, `data_nastere`, `loc_munca`) VALUES ('Stefansecu', 'Mihai', '2765', 'stefanescu7@yahoo.com', '2019-08-23', '1987-02-05', '5');
INSERT INTO `mag_piese.bd`.`angajati` (`nume_familie`, `prenume`, `salariu`, `email`, `data_angajare`, `data_nastere`, `loc_munca`) VALUES ('Tudor', 'Alexandru', '2234', 'alexandru.tudor@gmail.com', '2021-10-11', '1989-09-08', '5');
INSERT INTO `mag_piese.bd`.`angajati` (`nume_familie`, `prenume`, `salariu`, `email`, `data_angajare`, `data_nastere`, `loc_munca`) VALUES ('Andreescu', 'Mihaela', '3045', 'andreescu.mihaela22@icloud.com', '2020-05-22', '1990-06-19', '3');
INSERT INTO `mag_piese.bd`.`angajati` (`nume_familie`, `prenume`, `salariu`, `email`, `data_angajare`, `data_nastere`, `loc_munca`) VALUES ('Baciu', 'Andreea', '3400', 'baciu@andreea.ro', '2018-03-16', '1985-12-15', '3');
INSERT INTO `mag_piese.bd`.`angajati` (`nume_familie`, `prenume`, `salariu`, `email`, `data_angajare`, `data_nastere`, `loc_munca`) VALUES ('Badea', 'Achim', '1600', 'badea@achim.ro', '2022-01-02', '1990-01-12', '2');
INSERT INTO `mag_piese.bd`.`angajati` (`nume_familie`, `prenume`, `salariu`, `email`, `data_angajare`, `data_nastere`, `loc_munca`) VALUES ('Begu', 'Codrin', '3150', 'begu@codrin.ro', '2020-04-27', '1984-07-13', '1');
INSERT INTO `mag_piese.bd`.`angajati` (`nume_familie`, `prenume`, `salariu`, `email`, `data_angajare`, `data_nastere`, `loc_munca`) VALUES ('Bonciu', 'Carol', '2730', 'bonciu@carol.ro', '2018-01-19', '1981-05-29', '4');
INSERT INTO `mag_piese.bd`.`angajati` (`nume_familie`, `prenume`, `salariu`, `email`, `data_angajare`, `data_nastere`, `loc_munca`) VALUES ('Nita', 'Alexandra', '1800', 'nita@alexandra.ro', '2021-12-18', '1996-06-06', '2');
INSERT INTO `mag_piese.bd`.`angajati` (`nume_familie`, `prenume`, `salariu`, `email`, `data_angajare`, `data_nastere`, `loc_munca`) VALUES ('Stanciu', 'George', '2370', 'stanciu@george.ro', '2019-10-21', '1995-11-25', '3');
INSERT INTO `mag_piese.bd`.`angajati` (`nume_familie`, `prenume`, `salariu`, `email`, `data_angajare`, `data_nastere`, `loc_munca`) VALUES ('Diaconu', 'Anca', '3220', 'diaconu@anca.ro', '2020-02-03', '1988-06-27', '3');
INSERT INTO `mag_piese.bd`.`angajati` (`nume_familie`, `prenume`, `salariu`, `email`, `data_angajare`, `data_nastere`, `loc_munca`) VALUES ('Mocanu', 'Florin', '5430', 'mocanu@florin.ro', '2017-09-07', '1980-10-09', '6');
INSERT INTO `mag_piese.bd`.`angajati` (`nume_familie`, `prenume`, `salariu`, `email`, `data_angajare`, `data_nastere`, `loc_munca`) VALUES ('Toma', 'Dani', '4800', 'toma@dani.ro', '2018-12-09', '1982-07-11', '6');
INSERT INTO `mag_piese.bd`.`angajati` (`nume_familie`, `prenume`, `salariu`, `email`, `data_angajare`, `data_nastere`, `loc_munca`) VALUES ('Rusu', 'Bianca', '4750', 'rusu@bianca.ro', '2020-10-11', '1997-03-20', '6');
INSERT INTO `mag_piese.bd`.`angajati` (`nume_familie`, `prenume`, `salariu`, `email`, `data_angajare`, `data_nastere`, `loc_munca`) VALUES ('Lupu', 'Bogdan', '4020', 'lupu@bogdan.ro', '2021-08-14', '1993-02-18', '6');

-- -----------------------------------------------------
-- Populate Table 'modele_masini'
-- -----------------------------------------------------
INSERT INTO `mag_piese.bd`.`modele_masini` (`marca`, `model`, `an_incepere_fabricatie`, `an_finalizare_fabricatie`, `motorizare_cc`, `putere_cp`, `combustibil`, `cod_motor`, `tip_tractiune`) VALUES ('Skoda', 'Octavia II', 2007, 2010, '1968', '140', 'diesel', 'BKD', 'fata');
INSERT INTO `mag_piese.bd`.`modele_masini` (`marca`, `model`, `an_incepere_fabricatie`, `an_finalizare_fabricatie`, `motorizare_cc`, `putere_cp`, `combustibil`, `cod_motor`, `tip_tractiune`) VALUES ('Volvo', 'S80 II', 2006, 2016, '1984', '163', 'diesel', 'D5204T3', 'fata');
INSERT INTO `mag_piese.bd`.`modele_masini` (`marca`, `model`, `an_incepere_fabricatie`, `an_finalizare_fabricatie`, `motorizare_cc`, `putere_cp`, `combustibil`, `cod_motor`, `tip_tractiune`) VALUES ('BMW', 'M2', 2016, 2020, '2999', '450', 'benzina', 'fsda22', '4x4');
INSERT INTO `mag_piese.bd`.`modele_masini` (`marca`, `model`, `an_incepere_fabricatie`, `an_finalizare_fabricatie`, `motorizare_cc`, `putere_cp`, `combustibil`, `cod_motor`, `tip_tractiune`) VALUES ('Dacia', 'Logan', 2004, 2009, '1399', '100', 'benzina', 'ffd', 'fata');
INSERT INTO `mag_piese.bd`.`modele_masini` (`marca`, `model`, `an_incepere_fabricatie`, `an_finalizare_fabricatie`, `motorizare_cc`, `putere_cp`, `combustibil`, `cod_motor`, `tip_tractiune`) VALUES ('Opel', 'Corsa', 2016, 2020, '1399', '90', 'benzina', '55', 'fata');
INSERT INTO `mag_piese.bd`.`modele_masini` (`marca`, `model`, `an_incepere_fabricatie`, `an_finalizare_fabricatie`, `motorizare_cc`, `putere_cp`, `combustibil`, `cod_motor`, `tip_tractiune`) VALUES ('Volvo', 'S80 II', 2006, 2016, '1984', '136', 'diesel', 'D3136T2', 'fata');
INSERT INTO `mag_piese.bd`.`modele_masini` (`marca`, `model`, `an_incepere_fabricatie`, `an_finalizare_fabricatie`, `motorizare_cc`, `putere_cp`, `combustibil`, `cod_motor`, `tip_tractiune`) VALUES ('Volkswagen', 'Golf V', 2005, 2009, '1968', '140', 'diesel', 'BKD', 'fata');
INSERT INTO `mag_piese.bd`.`modele_masini` (`marca`, `model`, `an_incepere_fabricatie`, `an_finalizare_fabricatie`, `motorizare_cc`, `putere_cp`, `combustibil`, `cod_motor`, `tip_tractiune`) VALUES ('Seat', 'Leon 1P', 2005, 2009, '1968', '140', 'diesel', 'BKD', 'fata');
INSERT INTO `mag_piese.bd`.`modele_masini` (`marca`, `model`, `an_incepere_fabricatie`, `an_finalizare_fabricatie`, `motorizare_cc`, `putere_cp`, `combustibil`, `cod_motor`, `tip_tractiune`) VALUES ('Volvo', 'S80 II', 2006, 2016, '4414', '315', 'benzina', 'B8444S', '4x4');
INSERT INTO `mag_piese.bd`.`modele_masini` (`marca`, `model`, `an_incepere_fabricatie`, `an_finalizare_fabricatie`, `motorizare_cc`, `putere_cp`, `combustibil`, `cod_motor`, `tip_tractiune`) VALUES ('Skoda', 'Octavia I', 1996, 2010, '1896', '90', 'diesel', 'ALH', 'fata');
INSERT INTO `mag_piese.bd`.`modele_masini` (`marca`, `model`, `an_incepere_fabricatie`, `an_finalizare_fabricatie`, `motorizare_cc`, `putere_cp`, `combustibil`, `cod_motor`, `tip_tractiune`) VALUES ('Skoda', 'Octavia II', 2004, 2013, '1968', '170', 'diesel', 'CEGA', 'fata');
INSERT INTO `mag_piese.bd`.`modele_masini` (`marca`, `model`, `an_incepere_fabricatie`, `an_finalizare_fabricatie`, `motorizare_cc`, `putere_cp`, `combustibil`, `cod_motor`, `tip_tractiune`) VALUES ('Volkswagen', 'Golf IV', 1999, 2004, '1896', '110', 'diesel', 'AXR', 'fata');
INSERT INTO `mag_piese.bd`.`modele_masini` (`marca`, `model`, `an_incepere_fabricatie`, `an_finalizare_fabricatie`, `motorizare_cc`, `putere_cp`, `combustibil`, `cod_motor`, `tip_tractiune`) VALUES ('Volkswage', 'Golf VII', 2012, 2019, '1984', '300', 'benzina', 'CJXC', '4x4');
INSERT INTO `mag_piese.bd`.`modele_masini` (`marca`, `model`, `an_incepere_fabricatie`, `an_finalizare_fabricatie`, `putere_cp`, `combustibil`, `tip_tractiune`) VALUES ('Volkswagen', 'e-Golf', 2017, 2021, '136', 'electric', 'fata');
INSERT INTO `mag_piese.bd`.`modele_masini` (`marca`, `model`, `an_incepere_fabricatie`, `an_finalizare_fabricatie`, `motorizare_cc`, `putere_cp`, `combustibil`, `cod_motor`, `tip_tractiune`) VALUES ('Seat', 'Leon 5F', 2012, 2020, '1984', '280', 'benzina', 'CJXA', 'fata');
INSERT INTO `mag_piese.bd`.`modele_masini` (`marca`, `model`, `an_incepere_fabricatie`, `an_finalizare_fabricatie`, `motorizare_cc`, `putere_cp`, `combustibil`, `cod_motor`, `tip_tractiune`) VALUES ('Seat', 'Leon 5F', 2012, 2020, '1968', '150', 'diesel', 'CKFC', 'fata');
INSERT INTO `mag_piese.bd`.`modele_masini` (`marca`, `model`, `an_incepere_fabricatie`, `an_finalizare_fabricatie`, `motorizare_cc`, `putere_cp`, `combustibil`, `cod_motor`, `tip_tractiune`) VALUES ('Seat', 'Leon 1P', 2005, 2012, '1798', '160', 'benzina', 'BZB', 'fata');
INSERT INTO `mag_piese.bd`.`modele_masini` (`marca`, `model`, `an_incepere_fabricatie`, `an_finalizare_fabricatie`, `motorizare_cc`, `putere_cp`, `combustibil`, `cod_motor`, `tip_tractiune`) VALUES ('Seat', 'Leon KL1', 2020, 2022, '1395', '204', 'hybrid-benzina', 'DGEA', 'fata');
INSERT INTO `mag_piese.bd`.`modele_masini` (`marca`, `model`, `an_incepere_fabricatie`, `an_finalizare_fabricatie`, `motorizare_cc`, `putere_cp`, `combustibil`, `cod_motor`, `tip_tractiune`) VALUES ('Peugeot', '508', 2011, 2014, '1997', '200', 'hybrid-diesel', 'RXH', '4x4');

-- -----------------------------------------------------
-- Populate Table 'piese'
-- -----------------------------------------------------
INSERT INTO `mag_piese.bd`.`piese` (`denumire_piesa`, `producator`, `interval_recomandat_schimb`, `pret_ron`) VALUES ('filtru aer vag', 'mann', '15000 km', '56');
INSERT INTO `mag_piese.bd`.`piese` (`denumire_piesa`, `producator`, `interval_recomandat_schimb`, `pret_ron`) VALUES ('stergator luneta opel corsa', 'bosch', '2 ani', '99');
INSERT INTO `mag_piese.bd`.`piese` (`denumire_piesa`, `producator`, `interval_recomandat_schimb`, `pret_ron`) VALUES ('filtru motorina vag', 'mann', '15000 km', '44');
INSERT INTO `mag_piese.bd`.`piese` (`denumire_piesa`, `producator`,  `pret_ron`) VALUES ('senzor parcare volvo', 'valeo', '54');
INSERT INTO `mag_piese.bd`.`piese` (`denumire_piesa`, `producator`, `interval_recomandat_schimb`, `pret_ron`) VALUES ('placute frana dacia', 'trw', '40000 km', '164');
INSERT INTO `mag_piese.bd`.`piese` (`denumire_piesa`, `producator`, `interval_recomandat_schimb`, `pret_ron`) VALUES ('placute frana bmw', 'brembo', '50000 km', '254');
INSERT INTO `mag_piese.bd`.`piese` (`denumire_piesa`, `producator`, `interval_recomandat_schimb`, `pret_ron`) VALUES ('discuri frana dacia', 'trw', '60000 km', '204');
INSERT INTO `mag_piese.bd`.`piese` (`denumire_piesa`, `producator`, `interval_recomandat_schimb`, `pret_ron`) VALUES ('filtru aer volvo', 'mann', '15000 km', '54');
INSERT INTO `mag_piese.bd`.`piese` (`denumire_piesa`, `producator`, `interval_recomandat_schimb`, `pret_ron`) VALUES ('distributie volvo', 'continental', '180000 km', '896');
INSERT INTO `mag_piese.bd`.`piese` (`denumire_piesa`, `producator`, `interval_recomandat_schimb`, `pret_ron`) VALUES ('distributie vag', 'luk', '210000 km', '1236');
INSERT INTO `mag_piese.bd`.`piese` (`denumire_piesa`, `producator`, `interval_recomandat_schimb`, `pret_ron`) VALUES ('filtru ulei vag', 'mann', '15000 km', '40');
INSERT INTO `mag_piese.bd`.`piese` (`denumire_piesa`, `producator`, `pret_ron`) VALUES ('valva control turbo volvo', 'continental', '568');

-- -----------------------------------------------------
-- Populate Table 'piesa_model'
-- -----------------------------------------------------
INSERT INTO `mag_piese.bd`.`piesa_model` (`id_piesa`, `id_model`) VALUES ('1', '1');
INSERT INTO `mag_piese.bd`.`piesa_model` (`id_piesa`, `id_model`) VALUES ('1', '7');
INSERT INTO `mag_piese.bd`.`piesa_model` (`id_piesa`, `id_model`) VALUES ('1', '8');
INSERT INTO `mag_piese.bd`.`piesa_model` (`id_piesa`, `id_model`) VALUES ('1', '10');
INSERT INTO `mag_piese.bd`.`piesa_model` (`id_piesa`, `id_model`) VALUES ('1', '11');
INSERT INTO `mag_piese.bd`.`piesa_model` (`id_piesa`, `id_model`) VALUES ('1', '12');
INSERT INTO `mag_piese.bd`.`piesa_model` (`id_piesa`, `id_model`) VALUES ('1', '16');
INSERT INTO `mag_piese.bd`.`piesa_model` (`id_piesa`, `id_model`) VALUES ('2', '5');
INSERT INTO `mag_piese.bd`.`piesa_model` (`id_piesa`, `id_model`) VALUES ('3', '1');
INSERT INTO `mag_piese.bd`.`piesa_model` (`id_piesa`, `id_model`) VALUES ('3', '7');
INSERT INTO `mag_piese.bd`.`piesa_model` (`id_piesa`, `id_model`) VALUES ('3', '8');
INSERT INTO `mag_piese.bd`.`piesa_model` (`id_piesa`, `id_model`) VALUES ('3', '10');
INSERT INTO `mag_piese.bd`.`piesa_model` (`id_piesa`, `id_model`) VALUES ('3', '11');
INSERT INTO `mag_piese.bd`.`piesa_model` (`id_piesa`, `id_model`) VALUES ('3', '12');
INSERT INTO `mag_piese.bd`.`piesa_model` (`id_piesa`, `id_model`) VALUES ('3', '16');
INSERT INTO `mag_piese.bd`.`piesa_model` (`id_piesa`, `id_model`) VALUES ('4', '2');
INSERT INTO `mag_piese.bd`.`piesa_model` (`id_piesa`, `id_model`) VALUES ('4', '6');
INSERT INTO `mag_piese.bd`.`piesa_model` (`id_piesa`, `id_model`) VALUES ('4', '9');
INSERT INTO `mag_piese.bd`.`piesa_model` (`id_piesa`, `id_model`, `originala`) VALUES ('5', '4', 'compatibila');
INSERT INTO `mag_piese.bd`.`piesa_model` (`id_piesa`, `id_model`, `originala`) VALUES ('7', '4', 'compatibila');
INSERT INTO `mag_piese.bd`.`piesa_model` (`id_piesa`, `id_model`) VALUES ('6', '3');
INSERT INTO `mag_piese.bd`.`piesa_model` (`id_piesa`, `id_model`) VALUES ('8', '2');
INSERT INTO `mag_piese.bd`.`piesa_model` (`id_piesa`, `id_model`) VALUES ('8', '6');
INSERT INTO `mag_piese.bd`.`piesa_model` (`id_piesa`, `id_model`) VALUES ('8', '9');
INSERT INTO `mag_piese.bd`.`piesa_model` (`id_piesa`, `id_model`) VALUES ('9', '2');
INSERT INTO `mag_piese.bd`.`piesa_model` (`id_piesa`, `id_model`) VALUES ('10', '1');
INSERT INTO `mag_piese.bd`.`piesa_model` (`id_piesa`, `id_model`) VALUES ('10', '7');
INSERT INTO `mag_piese.bd`.`piesa_model` (`id_piesa`, `id_model`) VALUES ('10', '8');
INSERT INTO `mag_piese.bd`.`piesa_model` (`id_piesa`, `id_model`) VALUES ('10', '10');
INSERT INTO `mag_piese.bd`.`piesa_model` (`id_piesa`, `id_model`) VALUES ('10', '11');
INSERT INTO `mag_piese.bd`.`piesa_model` (`id_piesa`, `id_model`) VALUES ('10', '12');
INSERT INTO `mag_piese.bd`.`piesa_model` (`id_piesa`, `id_model`) VALUES ('10', '16');
INSERT INTO `mag_piese.bd`.`piesa_model` (`id_piesa`, `id_model`) VALUES ('11', '1');
INSERT INTO `mag_piese.bd`.`piesa_model` (`id_piesa`, `id_model`) VALUES ('11', '7');
INSERT INTO `mag_piese.bd`.`piesa_model` (`id_piesa`, `id_model`) VALUES ('11', '8');
INSERT INTO `mag_piese.bd`.`piesa_model` (`id_piesa`, `id_model`) VALUES ('11', '10');
INSERT INTO `mag_piese.bd`.`piesa_model` (`id_piesa`, `id_model`) VALUES ('11', '11');
INSERT INTO `mag_piese.bd`.`piesa_model` (`id_piesa`, `id_model`) VALUES ('11', '12');
INSERT INTO `mag_piese.bd`.`piesa_model` (`id_piesa`, `id_model`) VALUES ('11', '16');
INSERT INTO `mag_piese.bd`.`piesa_model` (`id_piesa`, `id_model`) VALUES ('12', '2');
INSERT INTO `mag_piese.bd`.`piesa_model` (`id_piesa`, `id_model`) VALUES ('12', '6');
INSERT INTO `mag_piese.bd`.`piesa_model` (`id_piesa`, `id_model`) VALUES ('12', '9');

-- -----------------------------------------------------
-- Populate Table 'masini'
-- -----------------------------------------------------
INSERT INTO `mag_piese.bd`.`masini` (`vin`, `nr_inmatriculare`, `an_fabricatie`, `kilometraj`) VALUES ('OP1WS530XY1123456', 'IF65BAM', 2017, '91000');
INSERT INTO `mag_piese.bd`.`masini` (`vin`, `nr_inmatriculare`, `an_fabricatie`, `kilometraj`) VALUES ('TMBBE1234567890NJ', 'B67NJK', 2008, '189918');
INSERT INTO `mag_piese.bd`.`masini` (`vin`, `nr_inmatriculare`, `an_fabricatie`, `kilometraj`) VALUES ('FSSDE1234567890NJ', 'MM31HDD', 2008, '140000');
INSERT INTO `mag_piese.bd`.`masini` (`vin`, `nr_inmatriculare`, `an_fabricatie`, `kilometraj`) VALUES ('GREWE1234567890NJ', 'PH31ADE', 2005, '343232');
INSERT INTO `mag_piese.bd`.`masini` (`vin`, `nr_inmatriculare`, `an_fabricatie`, `kilometraj`) VALUES ('YV1WS530XY1123456', 'B555BXD', 2012, '184236');
INSERT INTO `mag_piese.bd`.`masini` (`vin`, `nr_inmatriculare`, `an_fabricatie`, `kilometraj`) VALUES ('YV1WS530XY1323456', 'B777BXD', 2013, '84236');
INSERT INTO `mag_piese.bd`.`masini` (`vin`, `nr_inmatriculare`, `an_fabricatie`, `kilometraj`) VALUES ('YV1MS98D123456789', 'B502BGD', 2012, '168116');

-- -----------------------------------------------------
-- Populate Table 'clienti'
-- -----------------------------------------------------
INSERT INTO `mag_piese.bd`.`clienti` (`cnp`, `nume_familie`, `prenume`, `nr_telefon`, `email`) VALUES ('5010502430038', 'Ionescu', 'Bogdan', '0748053805', 'ionescu.bogdan@gmail.com');
INSERT INTO `mag_piese.bd`.`clienti` (`cnp`, `nume_familie`, `prenume`, `nr_telefon`, `email`) VALUES ('5010231412428', 'Barbu', 'Andrada', '0748053235', 'barbu.andrada@gmail.com');
INSERT INTO `mag_piese.bd`.`clienti` (`cnp`, `nume_familie`, `prenume`, `nr_telefon`, `email`) VALUES ('5321321320038', 'Popa', 'Dragos', '0728053235', 'popa.dragos@gmail.com');
INSERT INTO `mag_piese.bd`.`clienti` (`cnp`, `nume_familie`, `prenume`, `nr_telefon`, `email`) VALUES ('5015235234333', 'Neamtu', 'Liviu', '0734342405', 'neamtu.liviu@gmail.com');
INSERT INTO `mag_piese.bd`.`clienti` (`cnp`, `nume_familie`, `prenume`, `nr_telefon`, `email`) VALUES ('5015232523532', 'Dumitrescu', 'Florin', '0708053995', 'dumitrescu.florin@gmail.com');
INSERT INTO `mag_piese.bd`.`clienti` (`cnp`, `nume_familie`, `prenume`, `nr_telefon`, `email`) VALUES ('5014324324338', 'Dura', 'Bogdan', '0731248443', 'bogdan2435@gmail.com');
INSERT INTO `mag_piese.bd`.`clienti` (`cnp`, `nume_familie`, `prenume`, `nr_telefon`, `email`) VALUES ('5014324234238', 'Stefanescu', 'Viorel', '0734353443', 'stefanescu.viorel@gmail.com');
INSERT INTO `mag_piese.bd`.`clienti` (`cnp`, `nume_familie`, `prenume`, `nr_telefon`, `email`) VALUES ('5010702550014', 'Popescu', 'Stefan', '0770434654', 'popescu@stefan.ro');
INSERT INTO `mag_piese.bd`.`clienti` (`cnp`, `nume_familie`, `prenume`, `nr_telefon`, `email`) VALUES ('1991225330023', 'Ionescu', 'Vlad', '0744553344', 'ionescu@vlad.ro');
INSERT INTO `mag_piese.bd`.`clienti` (`cnp`, `nume_familie`, `prenume`, `nr_telefon`, `email`) VALUES ('2961111660088', 'Popescu', 'Cristina', '0755234654', 'popescu@cristina.ro');

-- -----------------------------------------------------
-- Populate Table 'adrese'
-- -----------------------------------------------------
INSERT INTO `mag_piese.bd`.`adrese` (`tara`, `judet` ,`localitate`, `strada`, `nr_strada`, `bloc`, `scara`, `etaj`, `apartament`) VALUES ('Romania', 'Bucuresti', 'Sector 4', 'Viorele', '51', '30', '3', '7', '55');
INSERT INTO `mag_piese.bd`.`adrese` (`tara`, `judet` ,`localitate`, `strada`, `nr_strada`) VALUES ('Romania', 'Prahova', 'Ploiesti', 'Sarii', '30');
INSERT INTO `mag_piese.bd`.`adrese` (`tara`, `judet` ,`localitate`, `strada`, `nr_strada`, `bloc`, `scara`, `etaj`, `apartament`) VALUES ('Romania', 'Bucuresti', 'Sector 4', 'Cercetatorilor', '61', '37', '2', '4', '75');
INSERT INTO `mag_piese.bd`.`adrese` (`tara`, `judet` ,`localitate`, `strada`, `nr_strada`, `bloc`, `scara`, `etaj`, `apartament`) VALUES ('Romania', 'Bucuresti', 'Sector 1', 'Aripilor', '3', '22', 'A', '0', '33');
INSERT INTO `mag_piese.bd`.`adrese` (`tara`, `judet` ,`localitate`, `strada`, `nr_strada`, `bloc`, `scara`, `etaj`, `apartament`) VALUES ('Romania', 'Ploiesti', 'Ploiesti', 'Vornicei', '59', '13', 'B', '2', '15');
INSERT INTO `mag_piese.bd`.`adrese` (`tara`, `judet` ,`localitate`, `strada`, `nr_strada`) VALUES ('Romania', 'Ilfov', 'Snagov', 'Florilor', '87');

-- -----------------------------------------------------
-- Populate Table 'comenzi'
-- -----------------------------------------------------
INSERT INTO `mag_piese.bd`.`comenzi` (`data_comanda`, `masina`, `client`, `pregatita_de_angajat`, `tip_livrare`, `status_comanda`) VALUES ('2022-01-12', 'YV1WS530XY1123456', '5014324324338', '1', '1', '1');
INSERT INTO `mag_piese.bd`.`comenzi` (`data_comanda`, `masina`, `client`, `pregatita_de_angajat`, `tip_livrare`, `status_comanda`) VALUES ('2022-04-28', 'TMBBE1234567890NJ', '5014324324338', '5', '1', '2');
INSERT INTO `mag_piese.bd`.`comenzi` (`data_comanda`, `masina`, `client`, `pregatita_de_angajat`, `tip_livrare`, `status_comanda`) VALUES ('2022-04-28', 'GREWE1234567890NJ', '5015232523532', '5', '1', '2');
INSERT INTO `mag_piese.bd`.`comenzi` (`data_comanda`, `masina`, `client`, `pregatita_de_angajat`, `tip_livrare`, `status_comanda`) VALUES ('2022-05-14', 'FSSDE1234567890NJ', '5014324234238', '9', '1', '1');
INSERT INTO `mag_piese.bd`.`comenzi` (`data_comanda`, `masina`, `client`, `pregatita_de_angajat`, `tip_livrare`, `status_comanda`) VALUES ('2022-05-14', 'TMBBE1234567890NJ', '5014324324338', '5', '2', '1');
INSERT INTO `mag_piese.bd`.`comenzi` (`data_comanda`, `masina`, `client`, `pregatita_de_angajat`, `tip_livrare`, `status_comanda`) VALUES ('2022-05-14', 'YV1WS530XY1123456', '5014324324338', '5', '1', '1');
INSERT INTO `mag_piese.bd`.`comenzi` (`data_comanda`, `masina`, `client`, `pregatita_de_angajat`, `tip_livrare`, `status_comanda`) VALUES ('2022-04-28', 'GREWE1234567890NJ', '5010502430038', '5', '2', '1');

-- -----------------------------------------------------
-- Populate Table 'comanda_piesa'
-- -----------------------------------------------------
INSERT INTO `mag_piese.bd`.`comanda_piesa` (`id-comanda`, `id-piesa`, `nr_piese`) VALUES ('1', '4', '1');
INSERT INTO `mag_piese.bd`.`comanda_piesa` (`id-comanda`, `id-piesa`, `nr_piese`) VALUES ('1', '12', '1');
INSERT INTO `mag_piese.bd`.`comanda_piesa` (`id-comanda`, `id-piesa`, `nr_piese`) VALUES ('2', '1', '1');
INSERT INTO `mag_piese.bd`.`comanda_piesa` (`id-comanda`, `id-piesa`, `nr_piese`) VALUES ('2', '3', '2');
INSERT INTO `mag_piese.bd`.`comanda_piesa` (`id-comanda`, `id-piesa`, `nr_piese`) VALUES ('2', '11', '1');
INSERT INTO `mag_piese.bd`.`comanda_piesa` (`id-comanda`, `id-piesa`, `nr_piese`) VALUES ('3', '5', '2');
INSERT INTO `mag_piese.bd`.`comanda_piesa` (`id-comanda`, `id-piesa`, `nr_piese`) VALUES ('3', '7', '2');
INSERT INTO `mag_piese.bd`.`comanda_piesa` (`id-comanda`, `id-piesa`, `nr_piese`) VALUES ('4', '3', '3');
INSERT INTO `mag_piese.bd`.`comanda_piesa` (`id-comanda`, `id-piesa`, `nr_piese`) VALUES ('4', '1', '1');
INSERT INTO `mag_piese.bd`.`comanda_piesa` (`id-comanda`, `id-piesa`, `nr_piese`) VALUES ('5', '3', '1');
INSERT INTO `mag_piese.bd`.`comanda_piesa` (`id-comanda`, `id-piesa`, `nr_piese`) VALUES ('5', '1', '1');
INSERT INTO `mag_piese.bd`.`comanda_piesa` (`id-comanda`, `id-piesa`, `nr_piese`) VALUES ('6', '4', '3');
INSERT INTO `mag_piese.bd`.`comanda_piesa` (`id-comanda`, `id-piesa`, `nr_piese`) VALUES ('7', '1', '1');
INSERT INTO `mag_piese.bd`.`comanda_piesa` (`id-comanda`, `id-piesa`, `nr_piese`) VALUES ('7', '3', '1');

-- -----------------------------------------------------
-- Populate Table 'livrari'
-- -----------------------------------------------------
INSERT INTO `mag_piese.bd`.`livrari` (`awb`, `livrata_de_angajat`, `comanda`, `adresa`, `status_livrare`,  `data_programata_livrare`) VALUES ('DFASF8DSADAF8AS8FAS8', '6', '5', '1', '1', '2022-05-15');
INSERT INTO `mag_piese.bd`.`livrari` (`awb`, `livrata_de_angajat`, `comanda`, `adresa`, `status_livrare`,  `data_programata_livrare`) VALUES ('DJJN2IK31I2314913942', '6', '7', '2', '1', '2022-05-15');
