import gensim.downloader as api
import random
import csv

def main():
    # Push all the 5 words into a list
    # iterate thru the list, compare list[0] with list[0+i]
    # Store the values of similarity in an array, call max(arr_of_similiar) len(arr) = 4 > 0,1,2,3
    # find the index of the value which max returned > e.g. 2
    # compare that to the [a,b,c,d] array. 

    list_of_words = []
    list_of_similarity_score = []
    possible_answers = ['a','b','c','d']
    label = ''

    #Load the corpus
    wv = api.load('word2vec-google-news-300')

    # loading the synonyms file with open()
    myfile = open('synonyms.txt')
    # open the 'word2vec-google-news-300-details.csv' file in the write mode
    f = open('word2vec-google-news-300-details.csv', 'w', newline='')
    # create the csv writer
    writer = csv.writer(f)
    # write the header row to the csv file
    header = ['question-word', 'answer-word', 'guess-word', 'label']
    writer.writerow(header)

    # reading each line of the file and printing to the console
    for line in myfile:
        temp = line.split('\t')
        if len(temp) > 1:
            #question + 4 options
            list_of_words.append(temp[1].split('\n')[0])
        else:
            #Actual answer
            answer = temp[0].split('\n')[0]
            #Store the question_word
            question_word = list_of_words[0]
            for i in range(len(list_of_words)):
                if i>0: #start at index 1
                    try:
                        #Compare similarity of the words and push the score into a list
                        list_of_similarity_score.append(wv.similarity(list_of_words[0], list_of_words[i]))
                    except KeyError:
                        #Need to handle an exception in case word was not found in Word2Vec model
                        print("a word did not appear in this model")
            #Store the actual answer            
            answer_word = list_of_words[possible_answers.index(answer) + 1]
            #Find the most probable synonym
            if len(list_of_similarity_score) > 0:           
                answer_by_model = max(list_of_similarity_score)
                if list_of_similarity_score.index(answer_by_model) == possible_answers.index(answer):
                    label = 'correct'
                else:
                    label = 'wrong'
                #Store the guessed word
                guess_word = list_of_words[list_of_similarity_score.index(answer_by_model)]
            else:
                label = 'guess'
                #Store the guessed word
                guess_word = list_of_words[random.randint(1,4)]
            row = [question_word, answer_word, guess_word, label]
            writer.writerow(row)
            #When an answer is found, reset the list_of_words array and start filling it for the new question
            list_of_words = []
            list_of_similarity_score = []

    myfile.close()
    f.close()

    #Question 2 > Generating analysis.csv file

    # open the 'analysis.csv' file in the write mode
    analysis_file = open('analysis.csv', 'w', newline='')
    # open the 'word2vec-google-news-300-details.csv' file
    details_file = open('word2vec-google-news-300-details.csv')
    # create the csv reader
    csv_reader = csv.reader(details_file, delimiter=',')
    #Start reading the file and calculating stats
    line_count = 0
    correct_label_ctr = 0 #C
    not_guess_label_ctr = 0 #V
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            if row[3] == 'correct':
                correct_label_ctr +=1
            if row[3] != 'guess':
                not_guess_label_ctr +=1
            line_count += 1
    accuracy = correct_label_ctr/not_guess_label_ctr
    # create the csv writer
    writer = csv.writer(analysis_file)
    # write the header row to the csv file
    data = ['word2vec-google-news-300', '3000000', correct_label_ctr, not_guess_label_ctr, accuracy]
    writer.writerow(data)
    
    #Close files after processing
    analysis_file.close()
    details_file.close()
    
if __name__ == "__main__":
    main()