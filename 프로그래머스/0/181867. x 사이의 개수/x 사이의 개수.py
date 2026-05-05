def solution(myString):
    parsed = myString.split("x")
    return [len(str) for str in parsed]