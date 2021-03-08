if psql -lqt | cut -d \| -f 1 | grep -qw patrolconsole; then
    # database exists
    printf "%s\n"
    printf "%s\n" "Database already exists!"
    printf "%s\n"
    read -p 'Delete it?: ' databasedelete
    if [ $databasedelete = 'YES' ]
    then
      printf "%s\n" "bye bye database!"
      psql -f /Users/halc/source/PatrolConsole/create_database/SQL/deletepatrolconsole.sql postgres
    else
        printf "%s\n" $databasedelete
        printf "%s\n" "database left alone!"
        exit
    fi
fi
psql -f /Users/halc/source/PatrolConsole/create_database/SQL/Radio_tables.sql -d postgres
#python python/load_employees.py /Users/halc/source/PatrolConsole/create_database/csv/radipwdo_user_data.csv
#psql -f /Users/halc/source/SkiSchedule/Database_create/sql/data_load.sql -d skischool
#psql -f /Users/halc/source/SkiSchedule/Database_create/sql/Add_test_data.sql -d skischool
#python python/load_shift_templates.py /Users/halc/source/SkiSchedule/Database_create/csv/Shift_templates.csv