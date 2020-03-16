import bin.feature_engineering as feature_engineering
import bin.update_data as update_data
import bin.plots as plots

def main():
    update_data.main()
    feature_engineering.main()
    plots.main()

if __name__ == '__main__':
    main()