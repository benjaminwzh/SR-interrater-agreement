# Systematic Review Interrater Agreement

## What this is
This program checks the interrater agreement between two reviewers in the process of a systematic review.
It can be used during the title and abstract screening phase, or the full text screening phase.
Duplicates will be identified based on identical titles. They should be removed before rerunning the program as the agreement table will only be generated if no duplicates are present.

### How to use
1. Download the files into a location of your choice.
2. In `main.py`, edit the two reviewer names to be the names of you and your peer.
3. Export you and your peer's citation in RIS format as a txt file. 
4. Name it as such: `name_included.txt` or `name_excluded.txt`. The `name` should be the reviewer name in `main.py`.
5. Run `main.py` with the 4 files above in the same folder.

### Output
If duplicate article titles are found in either reviewer's data, txt file(s) will be generated in the format of `(name)_dupesIn(Location).txt`, where the location is the location of the duplicates.
If there are no duplicates, the agreement matrix will be printed in the terminal, along with 4 txt files generated in the folder:
1. includedAgreed, containing titles included by both reviewers
2. exlcudedAgreed, containing titles excluded by both reviewers
3. reviewer1Only, containing titles included by reviewer1 but not reviewer2
4. reviewer2Only, containing titles included by reviewer2 but not reviewer1

### Assumptions
1. Both reviewers screen from the same pool of articles.
2. The included and excluded articles should add up to be the same between both reviewers.
3. pandas is installed. If not, install using `pip install pandas`.