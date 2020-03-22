import bin.feature_engineering as feature_engineering
import bin.update_data as update_data
import bin.plots as plots

def main():
    print('Updating...')
    update_data.main()
    feature_engineering.main()
    print('Plotting...')
    plots.main()

if __name__ == '__main__':
    main()