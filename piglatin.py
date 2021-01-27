# słowo, które zaczyna się na samogłoskę (aeiou) dostaje końcówkę "WAY"
# eat = eatway
# słowo zaczynające się na spółgł ma wszystkie gloski przed 1 samogł przemieszczone na koniec wyrazu i dostaje końcówkę "AY"
# pig = igpay
# latin = atinlay
# paryz = aryzpay
# kiedy słowo zaczyna się z grupą spółgłosek dostaje końcówkę „AY”
# smile = ileSMay
# string = ingSTRay
# grzmot = otgrzmay

def to_pig():
    text = input("Wpisz słowa do transformacji na Pig Latin: ")
    if text == "":
        print("*** Jeśli chcesz zatrzymać program wpisz 'exit' *** \n Wpisz tekst jeszcze raz!")
        to_pig()

    elif text == "exit":
        exit()

    else:
        word_list = text.lower().split(" ")
        text = []

        for word in word_list:
            if word[0] in "aeiou":
                text.append(word + "way")
                # np. egg + way

            elif word[0].isdigit():
                text.append(word)
                #np. 5

            elif len(word) == 1:
                text.append(word)
                # np. w

            else:
                for letter in word:
                    if letter in "aeiou":
                        text.append(word[word.index(letter):] + word[:word.index(letter)] + "ay")
                        # smile =          ile            ->   iles                  -> ileasmay
                        break
                        # np. smile = ilesmay, paris = arispay
                else:
                    text.append(word + "ay")
                    # psy = psyay, ghbhbghbg = ghbhbghbgay

        print("Transformacja brzmi:", " ".join(text))


to_pig()
