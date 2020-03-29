import requests
import hashlib


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)

    if res.status_code != 200:
        raise RuntimeError(f'Error fetching the record {res.status_code}')
    return res


def pwned_api_check(password):
    sha1_password = (hashlib.sha1(password.encode('utf-8')).hexdigest().upper())
    first5_chars, tail = sha1_password[:5], sha1_password[5:]
    response = request_api_data(first5_chars)
    return get_password_leaks(response, tail)


def get_password_leaks(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def main(password):
    count = pwned_api_check(password)
    if count:
        print(f'{password} was found {count} times, please change it.')
    else:
        print(f'{password} was not found, carry on the good work.')

    print('Done')


if __name__ == '__main__':
    answer = input('Enter password that you want to check ')
    main(answer)
