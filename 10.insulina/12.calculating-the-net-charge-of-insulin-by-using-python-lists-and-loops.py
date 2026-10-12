# Exercise 1: Assigning variables, lists, and dictionaries

# Python3.11
# Coding: utf-8


# Store the human preproinsulin sequence in a variable called preproinsulin:

preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
                "reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"


# Store the remaining sequence elements of human insulin in variables:

lsInsulin = "malwmrllpllallalwgpdpaaa"

bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"

aInsulin = "giveqcctsicslyqlenycn"

cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"


# Merge the insulin chains:

insulin = bInsulin + aInsulin


# Create a dictionary containing the pKR values:

pKR = {
    'y': 10.07,
    'c': 8.18,
    'k': 10.53,
    'h': 6.00,
    'r': 12.48,
    'd': 3.65,
    'e': 4.25
}


# Exercise 2: Using count() to count the numbers of each amino acid

# Count the number of each amino acid:

seqCount = {
    x: float(insulin.upper().count(x.upper()))
    for x in ['y', 'c', 'k', 'h', 'r', 'd', 'e']
}


# Exercise 3: Writing the net charge formula

# Initialize pH:

pH = 0


# Calculate the net charge for each pH value:

while pH <= 14:

    netCharge = (
        +(sum({
            x: ((seqCount[x] * (10 ** pKR[x])) /
                ((10 ** pH) + (10 ** pKR[x])))
            for x in ['k', 'h', 'r']
        }.values()))

        -(sum({
            x: ((seqCount[x] * (10 ** pH)) /
                ((10 ** pH) + (10 ** pKR[x])))
            for x in ['y', 'c', 'd', 'e']
        }.values()))
    )

    print('{0:.2f}'.format(pH), netCharge)

    pH += 1