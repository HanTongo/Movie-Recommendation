import spacy
nlp = spacy.load("en_core_web_md")

def menu_options_display():
    print("[1] Input movie summary.")
    print("[2] Movie suggestion.")

def input_movie_summary():
    
    user_interest = input("Please enter the movie summary, that you would like a suggestion for another movie.: ")
    # Prepares the user_interest for further spacy language processing - for comparison to another sentence
    nlp_user_interest = nlp(user_interest)

    print("Movie summary submitted successfully.")
    input("Please press [ENTER] to return to the menu.")
    return nlp_user_interest

def movie_suggestion():
    with open('movies.txt', 'r') as file:
        file_content = file.readlines()
        # Variables to store the single string of movies and a list containing it all.
        line_sentence = ""
        line_list = []

        # Variables to store the similarity result and contain in a list.
        line_sentence_result = 0
        result_list = []

        for line in file_content:
            # Splits the movie recommendations by Line breaks
            line_sentence = line.split("\n")

            # Finds the similarity result between the movie recommendations and the user description.
            line_sentence_result = float((nlp(str(line_sentence)).similarity(nlp_user_interest)))

            # Adds the movie recommendation into a list, to be retrieved later
            line_list.append(line.split("\n"))

            # Adds the similarity result into a list, to be retrieved later
            result_list.append(float(line_sentence_result))

        # Stores the index position of the highest similarity result 
        highest_similarity_position = result_list.index(max(result_list))

        # Returns and stores the corresponding movie recommendation and its similarity score
        most_similar_movie = line_list[highest_similarity_position]
        similar_movie_score = result_list[highest_similarity_position]

        # Casts the list type of the movie recommendation into a single string
        single_string_most_similar_movie = ''.join(most_similar_movie)
        print("I think this movie would be great to watch next!")
        print(single_string_most_similar_movie)
        print(similar_movie_score)


menu_options_display() 
user_choice = input("Please enter your option [1-2, 0 to exit]: ")

# Loop to send the user to the desired service
# If there is an incorrect input, direct the user to retry.
while user_choice != "0":
    if user_choice == "1":
        nlp_user_interest = input_movie_summary()
    elif user_choice == "2":
        movie_suggestion()
    else:
        print("Invalid option. Please try again.")

    print()
    menu_options_display()
    user_choice = input("Please enter your option [1-2, 0]: ")

print("Thank you for using the program. Hope to see you again.")
input("[Press ENTER to exit]")
