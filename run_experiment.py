from bin.feature_engineering import main as features
from bin.plots import main as plot


def main():
    print('Features...')
    features()
    print('Plotting...')
    plot()

if __name__ == '__main__':
    main()