from nltk.tokenize import word_tokenize

def calculate_score(assinged_input, user_input):
    assinged_input_tokenized = word_tokenize(assinged_input)
    user_input_tokenized = word_tokenize(user_input)

    if user_input_tokenized == assinged_input_tokenized:
        return 100
    else:
        total_matching_words = 0
        for word in assinged_input_tokenized:
            if word in user_input_tokenized:
                total_matching_words += 1
        score = round((total_matching_words / len(assinged_input_tokenized)) * 100, 2)
        return score


def main():
    text = "God is Great! I won a lottery."
    u_text = "God is Great!I won a lottery."
    print(calculate_score(text, u_text))

if __name__ == '__main__':
    main()
