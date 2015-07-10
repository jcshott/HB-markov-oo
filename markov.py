import sys
import random


class SimpleMarkovGenerator(object):

    char_count = 500

    def read_files(self, filenames):
        """Given a list of files, make text (the corpus) from them."""

        text_of_all_files = ""

        for file_name in filenames:
            file_handle = open(file_name)
            text_of_all_files = text_of_all_files + " " + file_handle.read()

        return text_of_all_files

    def make_chains(self, corpus, n):
        """Takes input text as string; returns dictionary of markov chains."""
        # print corpus
        ngram_dict = {}
        # Create a list of words in order by splitting on spaces
        input_words = corpus.split()

        # Iterate over word list and create tuple keys for dictionary
        for index in xrange(len(input_words) - n):
            ngram = ()
            for index_n in xrange(n):
                ngram = ngram + (input_words[index + index_n],)
            # print ngram
        # For each tuple, check if the tuple is already a key in the dict
        # If it is a key, add to its value. If it is not a key, make it key, with new list
            if ngram not in ngram_dict:
                ngram_dict[ngram] = []
            
            ngram_dict[ngram].append(input_words[index + n])
        # print ngram_dict
        return ngram_dict

    def make_text(self, chains):
        """Takes dictionary of markov chains; returns random text."""
        # Grab random key from markov chain dict to start off the generated text
        #print self.char_count
        key_list = chains.keys()
            #  start_index = random.randint(0, (len(key_list) - 1))
        start_key = random.choice(key_list)
    
        # print "start_key:", start_key
        while not start_key[0][0].isupper(): 
            start_key = random.choice(key_list)
        key = start_key
        random_list_for_string = []

        
        for n in range(len(key)):
            random_list_for_string.append(key[n])
        
        # Until a ngram is not present in the dict, generate random next word from the values associated
        # with that ngram
        next_word = " "
        # print "next word", next_word
        while key in chains: #and char_count <= 140:
            value_list = chains[key]
        # random_index = random.randint(0, (len(value_list) - 1))
            next_word = random.choice(value_list)
            random_list_for_string.append(next_word)        
    
            temp_key = ()
            for n in range(1, len(key)):
                temp_key += (key[n],)
            # print "next word", next_word
            key = temp_key + (next_word,)

        temp_markov_string = " ".join(random_list_for_string)
        final_markov_string = temp_markov_string[:self.char_count]
       
        #print final_markov_string
    # print random_list_for_string
        
        
        for search_i in xrange(len(final_markov_string) - 1, 0, -1):
            if final_markov_string[search_i][-1] == "." or final_markov_string[search_i][-1] == "!" or final_markov_string[search_i][-1] == "?":
                final_markov_string = final_markov_string[:search_i + 1]
        
        

        return final_markov_string 


class TwitterMarkovGenerator(SimpleMarkovGenerator):
    """creates a tweet (140 character) sized Markov chain"""
    char_count = 300

if __name__ == "__main__":

    # we should get list of filenames from sys.argv
    filenames = []
    for i in range(1, len(sys.argv)):
        filenames.append(sys.argv[i])

    # we should make an instance of the class
    markov = TwitterMarkovGenerator()

    # we should call the read_files method with the list of filenames
    text = markov.read_files(filenames)
    markov_chains = markov.make_chains(text, 2)
    # we should call the make_text method 5x
    #for i in xrange(5):
    print markov.make_text(markov_chains)
