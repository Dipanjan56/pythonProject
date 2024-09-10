def check_palindrome(s: str) -> bool:
    if s == s[::-1]:
        return True
    else:
        return False


if __name__ == '__main__':
    s = 'babab'
    print(check_palindrome(s))
