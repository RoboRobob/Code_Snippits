"""
Description:
this program uses a hardcoded variable for the cyptertext.
it will re-code the text each time a positive integer (N) is used.
after offsetting each letter by N it will print out the final result
in the terminal.
"""

if __name__ == "__main__":

    cyphertext = "Scrambled Text goes Here: Numbers and special chars dissappear"
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    output = ""
    keepAlive = True
    cyphertext = cyphertext.lower()
    #main loop of program
    while keepAlive == True:
        N = input("please enter the amount to shift the cypher (numeric values only): ")
        output = ""
        if N.isnumeric() and cyphertext.isascii():
            N = int(N)
        else:
            keepAlive = False
            print("Either the shift value is invalid or the cyphertext is not ascii.")

        #while keepAlive == True:
        if(keepAlive == True):
            for i in range(len(cyphertext)):
                if(alphabet.find(cyphertext[i]) != -1):
                    output += alphabet[(alphabet.find(cyphertext[i])+N)%len(alphabet)]
                else:
                    output += cyphertext[i]
            print(output)
    print("Exiting...")
