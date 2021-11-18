select * from ninjas;
select * from dojos;

insert into dojos(name, created_at, updated_at)
values('Dojo_1', now(), now());

insert into dojos(name, created_at, updated_at)
values('Dojo_2', now(), now());

insert into dojos(name, created_at, updated_at)
values('Dojo_3', now(), now());

delete from dojos where id < 100;

insert into dojos(name, created_at, updated_at)
values('Dojo_4', now(), now());

insert into dojos(name, created_at, updated_at)
values('Dojo_5', now(), now());

insert into dojos(name, created_at, updated_at)
values('Dojo_6', now(), now());

insert into ninjas(first_name, last_name, age, created_at, updated_at, dojos_id)
values('Mike', 'Jones', 44, now(), now(), 47);

insert into ninjas(first_name, last_name, age, created_at, updated_at, dojos_id)
values('Joseph', 'McVey', 45, now(), now(), 47);

insert into ninjas(first_name, last_name, age, created_at, updated_at, dojos_id)
values('Hakeem','Seraki', 42, now(), now(), 47);

insert into ninjas(first_name, last_name, age, created_at, updated_at, dojos_id)
values('John','Kee', 64, now(), now(), 48);

insert into ninjas(first_name, last_name, age, created_at, updated_at, dojos_id)
values('Lee','Williams', 75, now(), now(), 48);

insert into ninjas(first_name, last_name, age, created_at, updated_at, dojos_id)
values('HB','Charles', 42, now(), now(), 48);

insert into ninjas(first_name, last_name, age, created_at, updated_at, dojos_id)
values('Usher','Raymond', 43, now(), now(), 49);

insert into ninjas(first_name, last_name, age, created_at, updated_at, dojos_id)
values('Tyreese','Gibson', 41, now(), now(), 49);

insert into ninjas(first_name, last_name, age, created_at, updated_at, dojos_id)
values('Robert','Kelly', 46, now(), now(), 49); 

select ninjas.first_name, ninjas.last_name
from dojos
join ninjas
on dojos.id = ninjas.dojos_id
where dojos.id = 47;

select  ninjas.id, ninjas.first_name, ninjas.last_name
from dojos
join ninjas
on dojos.id = ninjas.dojos_id
where dojos.id = 49;

select dojos.name as Dojo_name
from dojos
join ninjas
on dojos.id = ninjas.dojos_id
where dojos.id = 49
and ninjas.id = 10;