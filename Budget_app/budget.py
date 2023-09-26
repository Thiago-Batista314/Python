class Category:
    def __init__(self, category):
        # It Initializes the catogory variables;
        self.category = category
        self.ledger = []
        self.balance = 0

    def __repr__(self):
        # It shows the spents and descriptions if use the class as a string;
        string = ''
        string += f'{self.category}'.center(30, '*') + '\n'
        for key in self.ledger:
            string += f'{key["description"][:23]:<23}{key["amount"]:>7.2f}\n'
        string += f'Total: {self.balance:.2f}'

        return string

    def deposit(self, amount, description=''):
        # It deposits the value in balance and data in ledger;
        self.ledger.append({'amount': amount, 'description': description})
        self.balance += amount       

    def withdraw(self, amount, description=''):
        # It does the withdraw if have enought funds, return True if did or False otherwise; 
        if self.check_funds(amount) == False:
            return False
        else:
            self.ledger.append({'amount': -amount, 'description': description})
            self.balance -= amount
            return True

    def get_balance(self):
        # It returns the total balance (deposits + withdraws + transfer + etc);
        return self.balance

    def transfer(self, amount, budget):
        # It does the transfer if have enought funds, it returns True if did or False otherwise;
        if self.check_funds(amount) == False:
            return False
        else:
            self.withdraw(amount, f'Transfer to {budget.category}')
            budget.deposit(amount, f'Transfer from {self.category}')
            return True

    def check_funds(self, amount):
        # It Verifies if the balance have enought funds to do the operations;
        if self.balance < amount:
            return False
        else:
            return True


def create_spend_chart(categories):
    spent_values = []

    # It adds all the negative values in spent values;
    # (The values of each category are summed to add at spent_values);
    for category in categories:
        spent = 0
        higher = 0
        for item in category.ledger:
            if item['amount'] <= 0:
                spent += -1 * item['amount']
        spent_values.append(spent)
        # Defines the highest lenght between the categories' name; 
        for category in categories:
            if len(category.category) > higher:
                higher = len(category.category)

    # Start building the table using a dictionary;
    # Example: {position_y: values_x} ==> {'50|': '    o  o '}
    y_axis = {}
    # Positions are in the sequence of: 10, 20, 30, ...;
    for point_y in range(100, -1, -10):
        y_axis[f'{point_y}|'] = ''
        for percent in spent_values:
            # The total percent is the sum of all spent values;
            # The percent of each category is its spent divided by 
            # total spent;
            # Mutiplied by 100 to turn it into a percent value not a fraction;
            # Round the number to the nearest 10;
            percent = int(round(percent / sum(spent_values) * 100))
            # Add the value_x in position_y if is higher or equals than;
            if percent >= point_y:
                y_axis[f'{point_y}|'] += ' o '
            else:
                y_axis[f'{point_y}|'] += '   '
        # Only excludes the unnecessary spaces and go to the next line;
        y_axis[f'{point_y}|'].rstrip()
        y_axis[f'{point_y}|'] += ' \n'

    # Create the header message and footer's line (+- x-axis);
    header = 'Percentage spent by category\n'
    footer = '    ' + '---'*(len(categories)) + '-'

    # Starts building the table adding the header;
    table = header

    # Uses the keys as y-axis and values as x-axis;
    for point_y, value in y_axis.items():
        table += f'{point_y:>4}{value}'

    # Writes the footer (+- x-axis);
    table += footer + '\n'

    # Builds the categories' names in vertical lines;
    # The higher is used for the loop throught the categories' names;
    # The higher, remembering, is the the highest length of categories' names;
    for c in range(0, higher):
        table += ' '*4
        for category in categories:
            # If the c (counter) already passed the lenght of category's name,
            # just add a empty space for the tabulation go correctly;
            if c > len(category.category)-1:
                table += '   '
            # Else add the letter in;
            else:
                table += f' {category.category[c]} '
        if c < higher-1:
            table += ' \n'
        # The FreeCodeCamp exercises needed that the last line doesn't have
        # a \n, so this if... else... is only for this (\_o_o_/);
        else:
            table += ' '

    # Finally, return the string totally formatted.
    return table
