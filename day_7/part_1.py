import copy

source = 'day_7\\input.txt'

def get_operations(operators, terms):
    transactions = []
    operations = []
    equations = []
    for operator in operators:
        for term in terms[:-1]:
            operations.append(operator)    
    for i in range(0, len(terms) - 1):
        transaction = copy.deepcopy(operations)
        if i > 0:
            temp = transaction.pop(0)
            transaction.append(temp)    
        transactions.append(transaction)    
    operations = []
    for j in range(0, len(transactions[0])):
        operation = []
        for i in range(0, len(transactions)):
            operation.extend(transactions[i][j])
        operations.append(operation)   
    computations = []
    for i in range(0, len(operations)):
        computation = []
        for j in range(len(operations[0])):
            computation.append(terms[j])
            computation.append(operations[i][j])
        computation.append(terms[-1])

        computations.append(computation)
    print(computations)
    exit()
    return computations
    

if __name__ == '__main__':
    operators = ['*', '+']
    data = open(source).read()
    numbers = []
    for line in data.split('\n'):
        answer, terms = line.split(': ')
        answer = int(answer)
        terms = [int(term) for term in terms.split(' ')]
        numbers.append([answer, terms])
    
    combinations = []
    for answer, terms in numbers:
        combinations.append(get_operations(operators, terms))
    
    total = 0
    for i, combination in enumerate(combinations):
        sub_total = 0
        answer = numbers[i][0]
        print(answer, combination)
        
            
        
        
    
        #for i in range(0, len(terms) - 1):
            
    
    """     for i,term in enumerate(terms):
            print(term, end='')
            print(operations)
     """        

    
                
        
        


                


        
            

        

#[[answer], [terms]]
