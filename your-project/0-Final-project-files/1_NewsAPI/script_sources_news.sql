ALTER TABLE `virdishc_IH_Project3`.`sources` 
CHANGE COLUMN `source_id` `source_id` INT NOT NULL AUTO_INCREMENT ,
CHANGE COLUMN `name` `name` VARCHAR(255) NOT NULL ,
CHANGE COLUMN `category` `category` VARCHAR(255) NULL DEFAULT NULL ,
CHANGE COLUMN `country` `country` VARCHAR(255) NOT NULL ,
CHANGE COLUMN `language` `language` VARCHAR(255) NOT NULL ,
CHANGE COLUMN `url` `url` TEXT NOT NULL ,
ADD PRIMARY KEY (`source_id`);
;

ALTER TABLE `virdishc_IH_Project3`.`news` 
CHANGE COLUMN `index` `id` INT NOT NULL ,
CHANGE COLUMN `date_published` `date_published` TIMESTAMP NOT NULL ,
CHANGE COLUMN `source_id` `source_id` INT NOT NULL ,
ADD PRIMARY KEY (`id`);
;


ALTER TABLE virdishc_IH_Project3.news 
ADD FOREIGN KEY (source_id) REFERENCES virdishc_IH_Project3.sources (source_id);
