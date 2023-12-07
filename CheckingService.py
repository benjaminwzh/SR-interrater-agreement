import pandas as pd

class CheckingService():
    ## Takes in the Datasets of two reviwers.
    ## If no duplicates are present, check for agreement and generate the output files and agreement matrix
    ## If duplicates are present, reviewers should recheck and regenerate the library with them removed

    def __init__(self, r1dataset, r2dataset):
        if r1dataset.get_clear() and r2dataset.get_clear():
            print("No duplicates present, checking agreement now...")
            self.r1name, self.r2name = r1dataset.get_name(), r2dataset.get_name()
            self.includedData = self.findAgreement(r1dataset.get_included(), r2dataset.get_included())
            self.excludedData = self.findAgreement(r1dataset.get_excluded(), r2dataset.get_excluded())
            self.generate(self.includedData, self.excludedData)
        else:
            print(f"Check the duplicate articles before rerunning the program!")

    def findAgreement(self, r1data, r2data):
        agreed, r1only, r2only = [], r1data, []
        # Check whether title is defined in both data, or only one
        for title in r2data:
            if title in r1only:
                agreed.append(title)
                r1only.remove(title)
            else:
                r2only.append(title)
        # Each list has a count of titles, followed by the titles
        final = [agreed, r1only, r2only]
        for lst in final:
            count = f"{str(len(lst))} article(s)"
            lst.insert(0, count)
        return final

    def generate(self, includedData, excludedData):
        # Generate files with article titles
        with open("includedAgreed.txt", "w", encoding="utf8") as f:
            print(f"Generating includedAgreed.txt with {includedData[0][0]}.")
            lines = "\n".join(includedData[0])
            f.write(lines)
        with open("excludedAgreed.txt", "w", encoding="utf8") as f:
            print(f"Generating excludedAgreed.txt with {excludedData[0][0]}.")
            lines = "\n".join(excludedData[0])
            f.write(lines)
        with open(f"{self.r1name}Only.txt", "w", encoding="utf8") as f:
            print(f"Generating {self.r1name}Only.txt with {includedData[1][0]}.")
            lines = "\n".join(includedData[1])
            f.write(lines)
        with open(f"{self.r2name}Only.txt", "w", encoding="utf8") as f:
            print(f"Generating {self.r2name}Only.txt with {includedData[2][0]}.")
            lines = "\n".join(includedData[2])
            f.write(lines)
        
        # Print a table for articles in each segment
        table = [[includedData[0][0], includedData[1][0]],
                [includedData[2][0], excludedData[0][0]]]
        df = pd.DataFrame(table, 
                        columns = [f"{self.r2name} Included", f"{self.r2name} Excluded"], 
                        index = [f"{self.r1name} Included", f"{self.r1name} Excluded"])
        print(f"""
**********
Agreement matrix:
{df}
**********""")