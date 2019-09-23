import numpy as np
import pandas as pd
import seaborn as sns

def inspect_discrete_continuous_var(input_series=None):
    
    """ Docstring: inspect discrete and continuous variable
    
    The argument of the function "input_series" should be 
    a pandas Series object.
    
    The function returns summary plots and summary statistics.
            
    """

    # Display boxplot and histogram/kde.
    f, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(10, 5) )
    sns.boxplot(x=input_series, ax=ax1)
    sns.distplot(input_series, ax=ax2)
    font = {'weight' : 'bold',
            'size'   : 16}
    ax1.set_title(input_series.name, fontdict=font)
    plt.show()

    # Print summary statistics.
    print('Min: \t\t\t {:,.0f}'.format(input_series.min()))
    print('Lower Quartile: \t {:,.0f}'.format(input_series.quantile([.25]).iloc[0]))
    print('median: \t\t {:,.0f}'.format(input_series.median()))
    print('mean: \t\t\t {:,.0f}'.format(input_series.mean()))
    print('Upper Quartile: \t {:,.0f}'.format(input_series.quantile([.75]).iloc[0]))                                    
    print('max: \t\t\t {:,.0f}'.format(input_series.max()))
    print('\n')
    print('Skew: \t\t\t {:,.2f}'.format(input_series.skew()))
    print('Kurtosis: \t\t {:,.2f}'.format(input_series.kurtosis()))
    print('Standard Deviation: \t {:,.0f}'.format(input_series.std()))

    return None

if __name__ == '__main__':
    dates = pd.date_range('20170101', periods=100, freq="W" )
    data = pd.DataFrame(np.random.randn(100, 5), index=dates, columns=list('ABCDE'))
    inspect_discrete_continuous_var(data['A'])