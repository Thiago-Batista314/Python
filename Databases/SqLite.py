def execute(connection, command, table='', columns=(), values=()):
    import sqlite3
    try:
        con = sqlite3.connect(connection)
        cursor = con.cursor()
        code_command = ''
        # ? this do the command if it will be insert;
        if command == 'insert' and table != '' and columns != () and values != ():
            code_command += f'INSERT INTO {table}'
            code_command += '('

            for column in columns:
                if column == columns[-1]:
                    code_command += str(column)
                else:
                    code_command += str(column) + ','


            code_command += ')'
            code_command += ' VALUES '
            code_command += '('

            for value in values:
                if value == values[-1]:
                    if str(value).isnumeric() != True:
                        code_command += "'" + str(value) + "'" + ","

                    else:
                        code_command += str(value)

                else:
                    if str(value).isnumeric() != True:
                        code_command += "'" + str(value) + "'" + ","

                    else:
                        code_command += str(value) + ','

            code_command += ')'

        elif command == 'create' and table != '' and columns != {}:
            code_command += f'CREATE TABLE {table} ('

            lst = []
            for key in columns.keys():
                lst.append(key)

            for column in columns.items():
                if column[0] == lst[-1]:
                    code_command += f"'{column[0]}' {column[1]}"
                else:
                    code_command += f"'{column[0]}' {column[1]},"

            code_command += ');'


        cursor.execute(code_command)

    finally:
        con.commit()
        con.close()


