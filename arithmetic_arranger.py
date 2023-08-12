def arithmetic_arranger(problems, show=False):
    import re
    first_line = ''
    second_line = ''
    third_line = ''
    arranged_problems = ''

    # Verify if has too many problems;
    if len(problems) > 5 : return 'Error: Too many problems.'
    for problem in problems:

        # Verify if the problems are correct;
        if re.search('[a-z]', problem) != None : return 'Error: Numbers must only contain digits.'

        for c in range(len(problem.split())):
            # Verify if number's greater than 9999;
            if c % 2 == 0 and len(problem.split()[c]) > 4: return 'Error: Numbers cannot be more than four digits.'

            # Verify if operators are diferent of + or -;
            if c % 2 == 1 and re.search('[+-]', problem.split()[c]) == None: return "Error: Operator must be '+' or '-'."

        # Find the longest character in the problem;
        len_longest_in_each_problem = len(max(re.findall('[0-9]\S*', problem), key=int))

        # Write the first line;
        first_line += ' '*2 + ' '*(len_longest_in_each_problem-len(problem.split()[0])) + str(problem.split()[0]) + ' '*4

        # Write the second line;
        second_line += str(problem.split()[1]) + ' ' + ' '*(len_longest_in_each_problem-len(problem.split()[2])) + str(problem.split()[2]) + ' '*4
        
        # Write the third line;
        third_line += '-'*(len_longest_in_each_problem + 2) + ' '*4

    # Excludes unnecessary spaces and go to the next line;
    first_line = first_line.rstrip() + '\n'
    second_line = second_line.rstrip() + '\n'
    third_line = third_line.rstrip()

    # Saves all the results in the variable;
    arranged_problems = first_line + second_line + third_line

    if show:
        
        # Start the results' line in a new line;
        results_line = '\n'
        for problem in problems:
            
            # Match the longest value in the problem;
            len_longest_in_each_problem = len(max(re.findall('[0-9]\S*', problem), key=int))
            
            # If the problem is negative or its result is has more digits than the account length, it doesn't write one space;
            if eval(problem) < 0 or len(str(eval(problem))) > len_longest_in_each_problem:
                results_line += ' ' + ' '*(len_longest_in_each_problem-len(str(eval(problem)))) + str(eval(problem)) + ' '*4
            
            # Write the space excluded in the past conditional;
            else:
                results_line += ' '*2 + ' '*(len_longest_in_each_problem-len(str(eval(problem)))) + str(eval(problem)) + ' '*4
        
        # It saves the result without unnecessary spaces; 
        arranged_problems += results_line.rstrip()

    # Return the result final;
    return arranged_problems
