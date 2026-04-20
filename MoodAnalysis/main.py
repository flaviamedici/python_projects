from nltk.sentiment import SentimentIntensityAnalyzer
import glob

# Get all files in a specific folder
files = glob.glob('diary/*')

for file in files:
    with open(file, 'r') as f:
        diary_entries = f.read()


    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(diary_entries)
    print(str(file[6:-4]) +" "+ str(scores))

    if scores["pos"] > scores["neg"]:
        print("This is a positive day")
    else:
        print("This is a negative day")