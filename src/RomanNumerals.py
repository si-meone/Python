
numeralLookup = [
                 [ 1000,    'M',    1 ],
                 [ 900,     'CM',   2 ],
                 [ 500,     'D',    1 ],
                 [ 400,     'CD',   2 ],
                 [ 100,     'C',    1 ],
                 [ 90,      'XC',   2 ],
                 [ 50,      'L',    1 ],
                 [ 40,      'XL',   2 ],
                 [ 10,      'X',    1 ],
                 [ 9,       'IX',   2 ],
                 [ 5,       'V',    1 ],
                 [ 4,       'IV',   2 ],
                 [ 1,       'I',    1 ]
]

lookupLen = len(numeralLookup);

def toNumerals(number):
    if number < 1 or number > 3999:
        raise ValueError() 
    result = ''
    for numeral in numeralLookup:
        while number >= numeral[0]:
            number -= numeral[0]
            result += numeral[1]
            if number == 0:
                return result
    return result

def fromNumerals(numeral):
    result = 0
    fromIdx = 0
    while numeral:
        for i in range( fromIdx, lookupLen ):
            record = numeralLookup[i]
            if record[1] == numeral[0:record[2]]:
                result += record[0]
                numeral = numeral[record[2]:]
                fromIdx = i
                break
            elif record[0] == 1:
                raise ValueError("Invalid numeral: " + numeral)
    return result;
