from Dataset import Dataset
from CheckingService import CheckingService

## Before running the program, check that:
## The names here are changed to the names of you and your reviewer
## The 4 txt files are named as name_included.txt or name_excluded.txt as necessary for each reviewer
REVIEWER1 = "name1"
REVIEWER2 = "name2"

def main(r1, r2):
    try:
        # Generate Datasets of reviewers
        r1data = Dataset(r1, f"{r1.lower()}_included.txt", f"{r1.lower()}_excluded.txt")
        r2data = Dataset(r2, f"{r2.lower()}_included.txt", f"{r2.lower()}_excluded.txt")
    except FileNotFoundError:
        print("File containing data not found. Please check that the reviewer names and txt files are correct!")
    else:
        # If Datasets generated, do the agreement checking
        CheckingService(r1data, r2data)

if __name__ == "__main__":
    main(REVIEWER1, REVIEWER2)