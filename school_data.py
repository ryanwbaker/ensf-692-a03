# school_data.py
# 
# Ryan Baker
# ENSF 692 P2024
#
# A terminal-based application for computing and printing statistics based on given input.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.
#
# PLEASE READ README.md for description on how all rubric criteria were met


import numpy as np
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022

# Declare any global variables needed to store the data here

schools = [{'id':1224, 'name':'Centennial High School'}, 
            {'id':1679, 'name':'Robert Thirsk School'}, 
            {'id':9626, 'name':'Louise Dean School'}, 
            {'id':9806, 'name':'Queen Elizabeth High School'}, 
            {'id':9813, 'name':'Forest Lawn High School'}, 
            {'id':9815, 'name':'Crescent Heights High School'}, 
            {'id':9816, 'name':'Western Canada High School'}, 
            {'id':9823, 'name':'Central Memorial High School'}, 
            {'id':9825, 'name':'James Fowler High School'}, 
            {'id':9826, 'name':'Ernest Manning High School'}, 
            {'id':9829, 'name':'William Aberhart High School'}, 
            {'id':9830, 'name':'National Sport School'}, 
            {'id':9836, 'name':'Henry Wise Wood High School'}, 
            {'id':9847, 'name':'Bowness High School'}, 
            {'id':9850, 'name':'Lord Beaverbrook High School'}, 
            {'id':9856, 'name':'Jack James High School'}, 
            {'id':9857, 'name':'Sir Winston Churchill High School'}, 
            {'id':9858, 'name':'Dr. E. P. Scarlett High School'}, 
            {'id':9860, 'name':'John G Diefenbaker High School'}, 
            {'id':9865, 'name':'Lester B. Pearson High School'}]


years = np.array([2013,2014,2015,2016,2017,2018,2019,2020,2021,2022])

# grades = np.array([year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022], dtype=int)
grades = np.array([year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022])

# Rubric --> Code Structure and Semantics: At least one 3-dimensional array
# Dimensions: [year, school, grade]
grades = np.array([np.resize(grade,(20,3)) for grade in grades])


# You may add your own additional classes, functions, variables, etc.
def validate_input(user_string):
    """Checks if user input matches school code or name and returns the school index if it is found, otherwise returns a ValueError exception
    
    parameters: user_string (str) string to check against the numpy array of school ids and school names

    returns: (int) index of school if found or ValueError if not found
    """

    for i, val in enumerate(schools):
        try:
            if val['id'] == int(user_string):
                return i
        except:
            if val['name'] == user_string:
                return i
            
    else:
        raise ValueError("Entry not found")
    

def prompt_user():
    """Prompts user for input and returns index of school if found, otherwise re-prompts user
    
    parameters: none
    
    returns: index of school (int)
    """
    
    while True:
        try:
            user_input = input("Please enter the high school name or high school code: ")
            return validate_input(user_input)
    
        except:    
            print("Invalid input")


def get_school_data(school_index):
    """Given a school index, returns school data as a 10 x 3 subarray (rows=years, cols=grades) from the 3-dimensional grades array.
    
    parameters: school_index (int) the id of the school to select data for
    
    returns: school_data (numpy.ndarray) a numpy subarray view of the specified data
    """
    
    return grades[::,school_index,::]


def print_school_statistics(school_data):
    """Prints the mean enrollments for each grade, highest enrollment for single grade, and lowest enrollment 
    for a single grade for a given school from a provided subarray view of the grade data for a given school
    
    parameters: school_data (numpy.ndarray) a numpy subarray view of the data for a given school
    
    returns: none
    """

    for col in np.arange(0,school_data.shape[1]):
        print(f"Mean enrollment for Grade {col + 10}: {int(np.nanmean(school_data[::,col]))}")
    print(f"Highest enrollment for a single grade: {int(np.nanmax(school_data))}")
    print(f"Lowest enrollment for a single grade: {int(np.nanmin(school_data))}")
    for row in np.arange(0, school_data.shape[0]):
        print(f"Total enrollment for {row+2013}: {int(np.nansum(school_data[row,::]))}")
    print(f"Total ten year enrollment: {int(np.nansum(school_data))}")
    print(f"Mean total enrollment over 10 years: {int(np.nanmean(np.nansum(school_data, axis=1)))}")
    
    # Some schools have no enrollments over 500.
    filtered_data = school_data[(school_data > 500) & (~np.isnan(school_data))]
    if filtered_data.size == 0:
        print("For all enrollments over 500, the median value was: Not Applicable (no enrollments over 500)")
    else:
        print(f"For all enrollments over 500, the median value was: {int(np.median(filtered_data))}")


def print_total_statistics():
    """Prints the mean enrollments for 2013 and 2022, 
    total graduating class of 2022, highest enrollment for a single grade, 
    and lowest enrollment for a single grade, highest enrollment for single grade, and lowest enrollment 
    for a single grade.
    
    parameters: none (uses `grades` global variable)
    
    returns: none
    """
    print(f"Mean enrollment in 2013: {int(np.nanmean(grades[0::20,::,::]))}")
    print(f"Mean enrollment in 2022: {int(np.nanmean(grades[9,::,::]))}")
    print(f"Total graduating class of 2022: {int(np.nansum(grades[9,::,2]))}")
    print(f"Highest enrollment for a single grade: {int(np.nanmax(grades))}")
    print(f"Lowest enrollment for a single grade: {int(np.nanmin(grades))}")



def main():
    print("ENSF 692 School Enrollment Statistics")

    # Print Stage 1 requirements here
    print("Shape of full data array:",grades.ndim)
    print("Dimensions of full data array:",grades.shape)
    
    # Prompt for user input
    school_index = prompt_user()
    school_data = get_school_data(school_index)


    # Print Stage 2 requirements here
    print("\n***Requested School Statistics***\n")
    print(f"School Name: {schools[school_index]['name']}, School Code: {schools[school_index]['id']}")
    print_school_statistics(school_data)
    

    # # Print Stage 3 requirements here
    print("\n***General Statistics for All Schools***\n")
    # Grouped statistics for all schools into a single function
    print_total_statistics()


if __name__ == '__main__':
    main()

