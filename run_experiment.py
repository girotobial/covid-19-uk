from bin.feature_engineering import main as features
from bin.plots import main as plot
from bin.update_data import main as update_data

def main():
    print('Updating data')
    update_data()
    print('Features...')
    features()
    print('Plotting...')
    plot()

if __name__ == '__main__':
    main()