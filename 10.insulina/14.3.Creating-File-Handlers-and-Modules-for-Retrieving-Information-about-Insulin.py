# Exercise 3: Creating the main program

import jsonFileHandler


# Retrieve JSON data
data = jsonFileHandler.readJsonFile("14.1.insulin.json")


# Check if the JSON data was successfully retrieved
if data != "":

    # Get insulin sequences

    bInsulin = data["molecules"]["bInsulin"]
    aInsulin = data["molecules"]["aInsulin"]
    insulin = bInsulin + aInsulin


    # Get actual molecular weight
    molecularWeightInsulinActual = data["molecularWeightInsulinActual"]


    # Display insulin information

    print("bInsulin: " + bInsulin)
    print("aInsulin: " + aInsulin)
    print(
        "molecularWeightInsulinActual: "
        + str(molecularWeightInsulinActual)
    )


    # Calculating the molecular weight of insulin
    # Getting a list of the amino acid (AA) weights
    aaWeights = data["weights"]


    # Count the number of each amino acid
    aaCountInsulin = {
        x: float(insulin.upper().count(x))
        for x in [
            "A", "C", "D", "E", "F", "G", "H", "I", "K", "L",
            "M", "N", "P", "Q", "R", "S", "T", "V", "W", "Y"
        ]
    }

    # Multiply the count by the weights
    molecularWeightInsulin = sum({
        x: aaCountInsulin[x] * aaWeights[x]
        for x in [
            "A", "C", "D", "E", "F", "G", "H", "I", "K", "L",
            "M", "N", "P", "Q", "R", "S", "T", "V", "W", "Y"
        ]
    }.values())

    # Display molecular weight
    print(
        "The rough molecular weight of insulin: "
        + str(molecularWeightInsulin)
    )


    # Calculate percentage error
    print(
        "Percent error: "
        + str(
            ((molecularWeightInsulin - molecularWeightInsulinActual)
            / molecularWeightInsulinActual) * 100
        )
    )

else:
    print("Error. Exiting program")