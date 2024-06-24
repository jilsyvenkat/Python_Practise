def bonus_calculator(employees):
    for employee in employees:
        bonus = 0
        if employee['role'] == 'developer':
            bonus = employee['salary'] * 0.1
        employee['bonus'] = bonus
    return employees