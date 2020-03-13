import bin.feature_engineering as feature_engineering
import bin.update_data as update_data

def main():
    update_data.main()
    feature_engineering.main()

if __name__ == '__main__':
    main()