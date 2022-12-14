from src.tools import HasThreeVowels, ContainsDuplicates, ContainsBadStrings, ContainsPairOfLetters, ContainsRepeatLetters

string1 = 'ugknbfddgicrmopn'
string2 = 'jchzalrnumimnmhp'
string3 = 'haegwjzuvuyypxyu'
string4 = 'dvszwmarrgswjxmb'


def test_HasThreeVowels():
    assert HasThreeVowels(string1) == True
    assert HasThreeVowels(string2) == True
    assert HasThreeVowels(string3) == True
    assert HasThreeVowels(string4) == False


def test_ContainsDuplicates():
    assert ContainsDuplicates(string1) == True
    assert ContainsDuplicates(string2) == False
    assert ContainsDuplicates(string3) == True
    assert ContainsDuplicates(string4) == True


def test_ContainsBadStrings():
    assert ContainsBadStrings(string1) == False
    assert ContainsBadStrings(string2) == False
    assert ContainsBadStrings(string3) == True
    assert ContainsBadStrings(string4) == False


def test_ContainsPairOfLetters():
    assert ContainsPairOfLetters('qjhvhtzxzqqjkmpb') == True
    assert ContainsPairOfLetters('xxyxx') == True
    assert ContainsPairOfLetters('uurcxstgmygtbstg') == True
    assert ContainsPairOfLetters('ieodomkazucvgmuy') == False


def test_ContainsRepeatLetters():
    assert ContainsRepeatLetters('qjhvhtzxzqqjkmpb') == True
    assert ContainsRepeatLetters('xxyxx') == True
    assert ContainsRepeatLetters('uurcxstgmygtbstg') == False
    assert ContainsRepeatLetters('ieodomkazucvgmuy') == True
