import pandas as pd
from nltk.corpus import stopwords

stop = stopwords.words('english')
stop.append("The")

def abstract_cleaning(file, keyword):

    abstracts = pd.read_csv(file)

    #Remove all blank rows
    abstracts= abstracts.dropna()

    #Remove stop words
    abstracts['phrases']= abstracts['abstract'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))

    #Remove sentences without keyword and texts that have large character set
    a= abstracts[abstracts['phrases'].str.contains(keyword)]
    a['Desired_Phrase']= a.phrases.str.replace(r'\b(\w+)(\s+\1)+\b', r'\1')
    a= a[a['Desired_Phrase'].apply(lambda x: len(x)<1000)]

    phrase_list = []


    for index,row in a.iterrows():
        # print(row['abstract'])
        phrase_list.append([row['Desired_Phrase']])


    return phrase_list