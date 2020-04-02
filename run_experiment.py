import bin.feature_engineering as feature_engineering
import bin.plots as plots

def main():
    feature_engineering.main()
    print('Plotting...')
    plots.main()

if __name__ == '__main__':
    main()