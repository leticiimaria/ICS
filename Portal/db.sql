create database db_portal;
use db_portal;

create table tb_usuarios(
usu_id int not null auto_increment primary key,
usu_nome varchar(200),
usu_email varchar(45),
usu_senha varchar(256)
);