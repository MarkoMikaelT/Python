import requests 
import json

#using dictionaryapi
#fetches given words data
#user can print out the definition, origin and searcha new word
def Main():
    print("Give a word")
    word = input()

    responseAPI = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/" + word)
    data = responseAPI.text
    parseJson = json.loads(data)

    while True:
        if Choices(parseJson, word) == 0:
            print("Program stopped...")
            break
        else:
            Choices(parseJson, word)


def Choices(parseJson, word):
    print("0. Quit \n1. Origin \n2. Definition \n3. New word")

    try:
        sw = int(input())
    except ValueError:
        print("Invalid input! Give a shown number!")
        return 1
    except:
        print("Invalid input!")
        return 1

    match(sw):
        case 0:
            return 0
        case 1:
            print(word + " origin:")
            try:
                info1 = parseJson[0]["origin"]
                print(info1)
            except KeyError:
                print("Couldn't find a origin :(")
            except:
                print("Something went wrong :( :(")

        case 2:
            print(word + " definition:")
            try:
                info2 = parseJson[0]["meanings"]
                print(info2[0]["definitions"][0]["definition"])
            except KeyError:
                print("Couldn't find a definition :(")
            except:
                print("Something went wrong :( :(")
        case 3:
            Main()

Main()
