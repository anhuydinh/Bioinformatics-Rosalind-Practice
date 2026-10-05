'''
Problem
Given: A string s of length at most 200 letters and four integers a, b, c and d.
Return: The slice of this string from indices a through b and c through d (with space in between), inclusively.
 In other words, we should include elements s[b] and s[d] in our slice.
Sample Dataset
HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.
22 27 97 102

Sample Output
Humpty Dumpty
'''

wordOneStartPos = 62
wordOneEndPos = 71

wordTwoStartPos = 87
wordTwoEndPos = 97

txtStr = "SBlgVWyewuP324R9agG2iOSRvcfFg4YaKJPNZlXgmtdaPEznYkM4bQjUIfUonMCtenosauraIwH7LlGCl1zjcwZtridactylumLLVqz5JRgILj7X8k1fRYeut8rBeez3mGwTNzB5sfZlggvPv0uL3vXQBvDgPa5g4O1Dq4SsX."
# End position is not inclusive, so we add 1 to capture it.
print(f'{txtStr[wordOneStartPos:wordOneEndPos + 1]} {txtStr[wordTwoStartPos:wordTwoEndPos+1]}')