create table if not exists user_finder (
 id_user int,
 first_name varchar(100),
 sex int,
 age_user int,
 city varchar(100),
 relation int,
 tv varchar(1000), 
 quotes varchar(1000), 
 interests varchar(1000),
 games varchar(1000),
 books varchar(1000),
 about varchar(1000),
 activities varchar(1000),
 music varchar(1000),
 movies varchar(1000),
 alcohol int,
 inspired_by varchar(100),
 life_main int,
 people_main int,
 political int,
 religion varchar(100),
 smoking int,
 token_user varchar(100)
);
 
ALTER TABLE public.user_finder ALTER COLUMN id_user SET NOT NULL;
ALTER TABLE public.user_finder  
ADD CONSTRAINT id_Password UNIQUE (id_user);


create table if not exists communications (
	user_finder_id integer references user_finder(id_user),
	search_results_id int
);

create table if not exists whitelist(
	user_finder_id integer references user_finder(id_user),
	search_results_id int
);


create table if not exists blacklist(
	user_finder_id integer references user_finder(id_user),
	search_results_id int
);


