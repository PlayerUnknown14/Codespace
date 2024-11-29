a_list_of_dictionaries = [

    {

        "Name": 'Adam',

        "Age": 28

    },

    {

        "Name": 'Beatrice',

        "Age": 29

    },

    {

        "Name": 'Ceri',

        "Age": 30

    },

    {

        "Name": 'Dean',

        "Age": 26

    }

]

pyexcel.save_as(records=a_list_of_dictionaries, dest_file_name="your_file.xls")import pyexcel

# make sure you had pyexcel-xls installed

a_list_of_dictionaries = [

    {

        "Name": 'Adam',

        "Age": 28

    },

    {

        "Name": 'Beatrice',

        "Age": 29

    },

    {

        "Name": 'Ceri',

        "Age": 30

    },

    {

        "Name": 'Dean',

        "Age": 26

    }

]

pyexcel.save_as(records=a_list_of_dictionaries, dest_file_name="your_file.xls")