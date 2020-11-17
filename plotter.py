import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    df = pd.DataFrame(pd.read_csv('text_data/to_kill_a_mocking_bird.csv', usecols=[0]))

    plt.style.use('ggplot')

    fig, axs = plt.subplots(2, 1)
    plt.suptitle('Correlation')
    plt.subplot(211)
    plt.xlabel('Genes')
    plt.ylabel('Count')

    plt.hist(df)

    plt.subplot(212)
    plt.xlabel('Sentence')
    plt.ylabel('Evos')
    plt.plot(df)

    fig.savefig('anal_data.png')
    fig.show()
