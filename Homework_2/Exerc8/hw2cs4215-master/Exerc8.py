import itertools
import pandas as pd
from main import train



if __name__ == '__main__':
    a = b = [1,2]
    df = pd.DataFrame(columns = ['a', 'b', 'Q_bar', 'final_accuracy']) 		    
    Q_bar = [0.1, 0.2]
    dataset = 'mnist'
    replications = 3
    for alpha, beta, Q in itertools.product(a, b, Q_bar):
        for replication in range(replications):
            accuracy = train(dataset, alpha, beta, Q)
            df = df.append({'a': alpha, 'b': beta, 'Q_bar': Q, 'final_accuracy': accuracy}, ignore_index=True)
            # each time make the csv file.
            df.to_csv("results.csv", sep='\t', encoding='utf-8')
        
   
