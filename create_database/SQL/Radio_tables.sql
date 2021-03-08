create database PatrolConsole;

\c patrolconsole

-- create tables 

create table radio_user
     (  UID serial primary key,
        LastName character varying(30),
        FirstName character varying(30),
        suffix varchar(5),
        NickName character varying(30),
        DOB date,
        employee_number character varying(30),
        NSP_ID varchar(15) unique,
        PSIA_ID character varying(15) unique,
        AASI_ID character varying(15) unique,
        payroll_id character varying(15) unique,
        Phone_cell character varying(11),
        Phone_cell_publish Boolean,
        Phone_2_text character varying(20),
        Phone_2 character varying(11),
        Phone_2_publish boolean,
        Phone_3_text character varying(20),
        Phone_3 character varying(11),
        Phone_3_publish boolean,
        Email character varying(50),
        Email_SMS character varying(50)
        
    )
;

create table radio_user_type
    (   UT serial primary key,
        user_type_name varchar(25)
    )
    ;
create table Radio 
    (   RID serial primary key,
        assetID varchar(25),
        serial_number varchar(25),
        date_in_service date,
        total_hours integer,
        total_carries integer,
        in_service boolean
    )
    ;

create table seasons
    ( SaID serial primary key,
      ss_date date,
      se_date date,
      season_name character varying(25)
    );
            
create table radio_signed_in
    (  RID integer primary key,
       UID integer,
       UT integer,
       sign_in_time timestamp,
       user_inservice_state boolean, 
       foreign key (UID) references radio_user (UID) on delete restrict,
       foreign key (UT) references radio_user_type (UT) on delete restrict
    )
    ;

create table patrol_log_book
    ( LID serial primary key,
      UID integer,
      sign_in_time timestamp,
      sign_out_time timestamp,
      RID integer,
      SaID integer default 1,
      foreign key (SaID) references seasons (SaID) on delete restrict,
      foreign key (UID) references radio_user (UID) on delete restrict,
      foreign key (RID) references radio (RID) on delete restrict
    )
    ;


create table employee_seasons
    ( ESID serial primary key,
      SaID integer default 1, --get_current_season(),
      uid integer,
      season_start_date date,
      season_end_date date,
      employee_returning integer,
      foreign key (SaID) references seasons (SaID) on delete restrict,
      foreign key (uid) references radio_user (UID) on delete restrict
    );

create table shift_templates
  ( StID serial primary key,
      Shift_Name character varying(45),
      start_time time, 
      End_Time time,
      DOW character varying(25),
      SaID integer default 1, --get_current_season(),
      deleted boolean default FALSE
    )
;

create table shifts 
	( SID serial primary key,
	  shift_name varchar(50),
    start_time time,
    end_time time,
    Shift_Date date,
    hill_chief integer,
    pro integer,
    SaID integer default 1, --default get_current_season(),
    foreign key (SaID) REFERENCES seasons (SaID) on delete restrict,
    foreign Key (hill_chief) REFERENCES radio_user (UID) on delete restrict,
    foreign Key (pro) references radio_user (UID) on delete restrict
    )
;
create table incident_type
  ( IT serial primary key,
    incident_type varchar(30) 
  )
;

create table transport_type
  ( TT serial primary key,
    transport_type varchar(30)
  )
;

create table incidents
  ( IID serial primary key,
    SID integer default 1, --get_current_shift(),
    active boolean default TRUE,
    current_primary integer,
    backed_up integer default Null,
    type varchar(10) default 'test', --get_default_incident(),
    found boolean default TRUE, 
    destination varchar(10) default 'Base', --get_default_destination(),
    current_location varchar(24) default Null,
    foreign key (SID) REFERENCES shifts (SID) on delete restrict,
    foreign key (current_primary) references radio_user on delete restrict,
    foreign key (backed_up) references radio_user on delete restrict
  )        
;

create table incident_user_assigned
  ( IAID serial primary key,
    IID integer,
    UID integer, 
    time_assigned timestamp default NOW(),
    time_released timestamp,
    foreign key (IID) references incidents (IID) on delete restrict,
    foreign key (UID) references radio_user (UID) on delete restrict
  )
;

create table injuries
  ( INID serial primary Key, 
    IID integer,
    transport_type integer,
    transporting_patroller_1 integer,
    transporting_patroller_2 integer,
    equitment_carry integer,
    foreign key (IID) references incidents (IID) on delete restrict,
    foreign key (transporting_patroller_1) references radio_user (UID) on delete restrict,
    foreign key (transporting_patroller_1) references radio_user (UID) on delete restrict,
    foreign key (transport_type) references transport_type (TT) on delete restrict
  )
;
create table hill_top_shifts
  (  HID serial primary key,
     SID integer default 1, --get_current_shift(),
     start_time time,
     end_time time,
     UID integer,
     foreign key (SID) REFERENCES shifts (SID) on delete restrict,
     foreign key (UID) references radio_user (UID) on delete restrict
  )
;
-- create views

-- create indeis

