from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
import numpy as np
import nltk
import json
import re
import seaborn as sns

import spacy
from spacy import displacy
import en_core_web_sm
import datetime

nlp = en_core_web_sm.load()
sns.set()

def graphDates():
    with open("FILE.json", "r") as read_file:
        data = json.load(read_file)
        messages = data['messages']
        frequency = dict()
        for message in messages:
            if "timestamp_ms" in message:
                year = datetime.datetime.fromtimestamp(message["timestamp_ms"]/1000.0).year
                if year in frequency:
                    frequency[year] += 1
                else:
                    frequency[year] = 1
                    
        data = []
        length = len(frequency)
        for i in range(min(7, length)):
            max_value = max(frequency.values())  # maximum value
            max_keys = [k for k, v in frequency.items() if v == max_value] # getting all keys containing the `maximum`
            print(max_value, max_keys)
            data.append((max_value, max_keys[0]))
            #max_values.append(max_value)
            for key in max_keys:
                del frequency[key]
    data.sort(key=lambda pair: pair[1])
    max_values = []
    key_values = []
    print (data)
    for i in range(len(data)):
        max_values.append(data[i][0])
        key_values.append(data[i][1])
    x = np.arange(min(7, length))
    fig, ax = plt.subplots()
    plt.bar(x, max_values)
    plt.xticks(x, key_values)
    fig.suptitle("Messages Sent Per Year")
    plt.show()

graphDates()


def countMessages():
    with open("FILE.json", "r") as read_file:
        data = json.load(read_file)
        messages = data['messages']
        frequency = dict()
        count = 1
        for message in messages:
            if 'content' in message:
                count += 1
        print (count)


def extractNames():
    with open("FILE.json", "r") as read_file:
        data = json.load(read_file)
        messages = data['messages']
        frequency = dict()

        regex = re.compile('[@_!#$%^&*()â<>?/\|»ð}{~:]') 
        for message in messages:
            if 'content' in message:
                doc = nlp(message['content']) 

                for word in doc.ents:
                    if regex.search(word.text) != None:
                        continue
                    if word.label_ == "PERSON":
                        if word.text in frequency:
                            frequency[word.text] += 1
                        else:
                            frequency[word.text] = 1

        max_values = []
        key_values = []
        for i in range(min(10, len(frequency))):
            max_value = max(frequency.values())  # maximum value
            max_keys = [k for k, v in frequency.items() if v == max_value] # getting all keys containing the `maximum`
            print(max_value, max_keys)
            max_values.append(max_value)
            for key in max_keys:
                key_values.append(key)
            for key in max_keys:
                del frequency[key]


    print (key_values)
    x = np.arange(10)
    fig, ax = plt.subplots()
    plt.bar(x, max_values)
    plt.xticks(x, key_values)
    fig.suptitle("Messages Sent Per Year")
    plt.show()


def extractNouns():
    with open("FILE.json", "r") as read_file:
        data = json.load(read_file)
        messages = data['messages']
        frequency = dict()

        regex = re.compile('[@_!#$%^&*()<>?/\|»ð}{~:]') 
        for message in messages:
            if 'content' in message:
                tokens = nltk.word_tokenize(message['content'])
                tagged = nltk.pos_tag(tokens)
                for pair in tagged:
                    if regex.search(pair[0]) != None:
                        continue
                    if pair[1] == 'FW' or pair[1] == 'NN' or pair[1] == 'NNS' or pair[1] == 'NNP' or pair[1] == 'NNPS':
                        if pair[0] in frequency:
                            frequency[pair[0]] += 1
                        else:
                            frequency[pair[0]] = 1

        max_values = []
        key_values = []
        for i in range(10):
            max_value = max(frequency.values())  # maximum value
            max_keys = [k for k, v in frequency.items() if v == max_value] # getting all keys containing the `maximum`
            print(max_value, max_keys)
            max_values.append(max_value)
            for key in max_keys:
                key_values.append(key)
            for key in max_keys:
                del frequency[key]


    print (key_values)
    x = np.arange(10)
    fig, ax = plt.subplots()
    plt.bar(x, max_values)
    plt.xticks(x, key_values)
    plt.show()
