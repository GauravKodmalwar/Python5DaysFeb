# Write a code to get word count in a paragraph
# Nested loop, upper lower
# dictionary - word key, count value
# A word with number - Other category
News = """BENGALURU: Indian astronomers have reported one of the strongest flares from a feeding supermassive black hole or blazar called BL Lacertae, some 10 million light-years away. And, the analysis of the flare from this blazar — one of the oldest astronomical objects — can help trace the mass of the black hole and the source of this emission.
This, the team believes can provide a lead to probe into mysteries and trace events at different stages of evolution of the Universe.
A team of astronomers led by Alok Chandra Gupta from the Aryabhatta Research Institute of Observational Sciences (ARIES) had been following the blazar since October 2020 as part of an international observational campaign. The team detected the exceptionally high flare on January 16, 2021, with the help of Sampurnanand Telescope (ST) and 1.3m Devasthal Fast Optical Telescopes located in Nainital.
“This class of objects is very unique. They have complete electromagnetic emission, that is they emit radiation in all electromagnetic bands — Radio Waves; Microwaves; Infrared; Visible Light; Ultraviolet (UV); X-Rays and Gamma Rays — which is not something all objects can do. Gamma ray births do this, but they are short lived,” Gupta told TOI.
"""
varSpecialChar = ('.', ',', ':', '@', '#', '"', '(', ')', '\\')
varDict = dict()
for word in News.split(' '):
    temp = [word.replace(char, '') for char in varSpecialChar if char in word]
    if len(temp) == 0:
        pass
    else:
        word = temp[0]
    if len(word) < 4:
        pass
    else:
        if varDict.get(word) == None:
            varDict[word] = 1
        else:
            varDict[word] += 1
words, count = varDict.keys(), varDict.values()
print(varDict)