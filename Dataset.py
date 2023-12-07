class Dataset():
    ## Takes in the EndNote library export of included articles and excluded articles of one reviewer
    ## Checks for presence of duplicates within the library, determined by articles having identical titles
    ## Articles are stored by their title only

    def __init__(self, name, included, excluded):
        self.name = name
        ## Take in the data
        self.included = self.processData(included)
        self.excluded = self.processData(excluded)
        ## Filter through the articles
        self.inclDuplicates = self.removeDuplicates(self.included)
        self.exclDuplicates = self.removeDuplicates(self.excluded)
        self.inBoth = self.crossCheck(self.included, self.excluded)
        self.clear = self.canContinue()

    ## Getters to obtain relevant datasets ##
    def get_name(self):
        return self.name
    def get_included(self):
        # A list of strings
        return self.included
    def get_excluded(self):
        # A list of strings
        return self.excluded
    def get_clear(self):
        return self.clear

    ## Methods that handle data processing ##
    def processData(self, filename):
        # Extract all the titles from the file, lines beginning with "TI  -"
        # From the filename, generate a list of strings
        with open(filename, "r", encoding="utf8") as f:
            contents = f.readlines()
            contents = list(map(lambda x: x.replace('\ufeff', ''), contents))
            contents = list(map(lambda x: x.strip(), contents))
        
        res = list(filter(lambda x: x[0:5] == "TI  -", contents))
        return res

    def removeDuplicates(self, file):
        # Extracts duplicates into a list along with a count of its appearance
        duplicates = []
        for title in file:
            count = file.count(title)
            if count > 1:
                dupe = (count, title)
                if not dupe in duplicates:
                    duplicates.append(dupe)

        # Direct removal of the duplicates in the attribute
        for title in duplicates:
            for _ in range(title[0]):
                file.remove(title[1])

        # Make count a string for file output later
        duplicates = list(map(lambda item: (str(item[0]), item[1]), duplicates))
        # A list of tuples, where each tuple contains the duplicate count and article title
        return duplicates

    def crossCheck(self, incl, excl):
        # Check within incl, if exist in excl, mark as duplicate
        # No need to do for excl, if title in excl exists in incl, it would be marked as duplicate in the above step
        duplicates = []
        for title in incl:
            count = excl.count(title)
            if count >= 1:
                dupe = (count, title)
                if not dupe in duplicates:
                    duplicates.append(dupe)

        # Direct removal of the duplicates from the two attributes
        for title in duplicates:
            for _ in range(title[0]):
                incl.remove(title[1])
                excl.remove(title[1])

        # Make count a string for file output later
        duplicates = list(map(lambda item: (str(item[0]), item[1]), duplicates))
        # A list of tuples, where each tuple contains the duplicate title count and article title
        return duplicates

    def canContinue(self):
        # If a duplicate is present, generate file with the duplicates
        if self.inclDuplicates:
            self.generateDuplicateFile("InIncluded")
        if self.exclDuplicates:
            self.generateDuplicateFile("InExcluded")
        if self.inBoth:
            self.generateDuplicateFile("InBoth")

        if not (self.inclDuplicates or self.exclDuplicates or self.inBoth):
            # No duplicates are present
            return True
        else:
            # Can consider giving the de-duplicated titles as an output file, but since it only has titles, it is less likely to be useful
            return False

    def generateDuplicateFile(self, typing):
        if typing == "InIncluded":
            data = self.inclDuplicates
        elif typing == "InExcluded":
            data = self.exclDuplicates
        elif typing == "InBoth":
            data = self.inBoth
        
        filename = f"{self.name}_dupes{typing}.txt"
        print(f"Duplicates found, generating {filename}.")
        final = [", ".join(tups) for tups in data]
        final = "\n".join(final)
        with open(filename, "w", encoding="utf8") as f:
            f.write(final)