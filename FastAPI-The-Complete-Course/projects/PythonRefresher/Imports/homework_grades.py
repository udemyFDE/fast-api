"""
- Modules get used all the time throughout the programming
- Helps to create more files, with unique purposes, to help with clean maintainable code
"""

# import <directory of the file>.<file name> as <name after import>
import Imports.grade_average_service as grade_service

homework_assignment_grades = {
    'homework_1': 85,
    'homework_2': 100,
    'homework_3': 81
}

grade_service.calculate_homework(homework_assignment_grades)


# OR

# import Imports.grade_average_service
#
# homework_assignment_grades = {
#     'homework_1': 85,
#     'homework_2': 100,
#     'homework_3': 81
# }
#
# Imports.grade_average_service.calculate_homework(homework_assignment_grades)


















