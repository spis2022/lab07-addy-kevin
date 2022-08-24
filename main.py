import pandas as pd
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import stopwords
from nltk.classify.util import accuracy

# "Stop words" that you might want to use in your project/an extension
stop_words = set(stopwords.words('english'))

def train(s):
  main_dict = {}
  wordList = s.split()
    
  # for i in wordList:
  #     main_dict[i] = "" #add word as a key to main_dict as key = i
  #     main_dict[i].append[wordList[i]] 
  for i in range(len(wordList) - 1): #len = 4, range = 0,1,2,3, wordList[i=3 + 1 = 4, which is not a real index], so minus 1
    if wordList[i] not in main_dict:
      main_dict[wordList[i]] = [] #add word as a key to main_dict as key = i
    main_dict[wordList[i]].append(wordList[i+1]) #checks if wordList[i] == key, appendable because value is a list #lines 20-22 execute for each word, looping

train("Yeah baby I like it like that You gotta believe me when I tell you I said I like it like that")

  
def format_sentence(sent):
    ''' format the text setence as a bag of words for use in nltk'''
    tokens = nltk.word_tokenize(sent)
    return({word: True for word in tokens})

def get_reviews(data, rating):
    ''' Return the reviews from the rows in the data set with the
        given rating '''
    rows = data['Rating']==rating
    return list(data.loc[rows, 'Review'])


def split_train_test(data, train_prop):
    ''' input: A list of data, train_prop is a number between 0 and 1
              specifying the proportion of data in the training set.
        output: A tuple of two lists, (training, testing)
    '''
    # TODO: You will write this function, and change the return value

  
    return ([], [])

def format_for_classifier(data_list, label):
    ''' input: A list of documents represented as text strings
               The label of the text strings.
        output: a list with one element for each doc in data_list,
                where each entry is a list of two elements:
                [format_sentence(doc), label]
    '''
    # TODO: Write this function, change the return value
    return []

def classify_reviews():
    ''' Perform sentiment classification on movie reviews ''' 
    # Read the data from the file
    data = pd.read_csv("data/movie_reviews.csv")

    # get the text of the positive and negative reviews only.
    # positive and negative will be lists of strings
    # For now we use only very positive and very negative reviews.
    positive = get_reviews(data, 4)
    negative = get_reviews(data, 0)

    # Split each data set into training and testing sets.
    # You have to write the function split_train_test
    (pos_train_text, pos_test_text) = split_train_test(positive, 0.8)
    (neg_train_text, neg_test_text) = split_train_test(negative, 0.8)

    # Format the data to be passed to the classifier.
    # You have to write the format_for_classifier function
    pos_train = format_for_classifier(pos_train_text, 'pos')
    neg_train = format_for_classifier(neg_train_text, 'neg')

    # Create the training set by appending the pos and neg training examples
    training = pos_train + neg_train

    # Format the testing data for use with the classifier
    pos_test = format_for_classifier(pos_test_text, 'pos')
    neg_test = format_for_classifier(neg_test_text, 'neg')
    # Create the test set
    test = pos_test + neg_test


    # Train a Naive Bayes Classifier
    # Uncomment the next line once the code above is working
    #classifier = NaiveBayesClassifier.train(training)

    # Uncomment the next two lines once everything above is working
    #print("Accuracy of the classifier is: " + str(accuracy(classifier, test)))
    #classifier.show_most_informative_features()

    # TODO: Calculate and print the accuracy on the positive and negative
    # documents separately
    # You will want to use the function classifier.classify, which takes
    # a document formatted for the classifier and returns the classification
    # of that document ("pos" or "neg").  For example:
    # classifier.classify(format_sentence("I love this movie. It was great!"))
    # will (hopefully!) return "pos"

    # TODO: Print the misclassified examples


if __name__ == "__main__":
    classify_reviews()
