import pandas as pd
import matplotlib.pyplot as plt

# Reads the CSV file as a Pandas dataframe.
def exercise_0(file):
    return pd.read_csv(file)

# Returns a list of column names from the dataframe.
def exercise_1(df):
    return list(df)

# Returns the first k rows from the dataframe.
def exercise_2(df, k):
    return df.head(k)

# Returns a random sample of k rows from the dataframe.
def exercise_3(df, k):
    return df.sample(n=k)

# Returns unique transaction types.
def exercise_4(df):
    return df['type'].unique()

# Returns a Pandas series of the top 10 transaction destinations with frequencies.
def exercise_5(df):
    return df['nameDest'].value_counts().head(10)

# Returns all rows for which fraud was detected.
def exercise_6(df):
    return df[df['isFraud'] == 1]

# Returns a dataframe with the number of distinct destinations for each source.
def exercise_7(df):
    df1 = df.groupby('nameOrig')['nameDest'].agg(['nunique'])
    df1.sort_values(by='nunique', ascending=False, inplace=True)
    return df1

# Visualizations for the dataset.
def visual_1(df):
    def transaction_counts(df):
        return df['type'].value_counts()

    def transaction_counts_split_by_fraud(df):
        return df.groupby(by=['type', 'isFraud']).size()

    fig, axs = plt.subplots(2, figsize=(6, 10))
    transaction_counts(df).plot(ax=axs[0], kind='bar')
    axs[0].set_title('Transaction Types Frequency')
    axs[0].set_xlabel('Transaction Type')
    axs[0].set_ylabel('Count')
    transaction_counts_split_by_fraud(df).plot(ax=axs[1], kind='bar')
    axs[1].set_title('Transaction Types by Fraud')
    axs[1].set_xlabel('Transaction Type')
    axs[1].set_ylabel('Count')
    fig.suptitle('Transaction Analysis')
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    for ax in axs:
        for p in ax.patches:
            ax.annotate(p.get_height(), (p.get_x(), p.get_height()))
    plt.show()
    return 'The first chart shows the frequency of different transaction types. The second chart shows the distribution of transaction types by fraud status. This visualization can help identify potential patterns in fraudulent transactions.'


def visual_2(df):
    def query(df):
        df['Origin Delta'] = df['oldbalanceOrg'] - df['newbalanceOrig']
        df['Destination Delta'] = df['oldbalanceDest'] - df['newbalanceDest']
        return df[df['type'] == 'CASH_OUT']
    plot = query(df).plot.scatter(x='Origin Delta', y='Destination Delta')
    plot.set_title(
        'Source v. Destination Balance Delta for Cash Out Transactions')
    plot.set_xlim(left=-1e3, right=1e3)
    plot.set_ylim(bottom=-1e3, top=1e3)
    plt.show()
    return 'A cash out occurs when a partipant withdraws money. It is reassuring that only two of the four quadrants have activity, as the contrary would indicate something wrong with the dataset. The y=-x line is particularly interesting as it indicates instant settlement.'

def main():
    df = exercise_0('transactions.csv')
    print(exercise_1(df))
    print(exercise_2(df, 5))
    print(exercise_3(df, 5))
    print(exercise_4(df))
    print(exercise_5(df))
    print(exercise_6(df))
    print(exercise_7(df))
    visual_1(df)
    visual_2(df)

main()
