import requests, bs4

# sudo apt-get install python-bs4 python3-bs4


def escape_string_quotes(s):
    return s.replace('"', '\\"')


def format_session(session):
    info = session.findChildren()
    data = {
        'title': escape_string_quotes(info[0].getText()),
        'presenter': escape_string_quotes(info[1].getText()),
        'room': escape_string_quotes(info[2].getText().replace('Room: ', '')),
        'category': escape_string_quotes(info[3].getText().replace('Category: ', ''))
    }
    # print(session)
    return u'''                {{
                    "title": "{title}",
                    "presenter": "{presenter}",
                    "room": "{room}",
                    "category": "{category}"
                }}'''.format(**data).encode('ascii', 'replace')


def format_time_slot(i, time_slot):
    sessions = time_slot.select('div.schedule-item')
    begin = '''        {{
            "name": "Slot {index}",
            "sessions": [
'''.format(index = i + 1)
    middle = ',\n'.join(map(format_session, sessions))
    end = '''
            ]
        }'''
    return begin + middle + end
    

def main():
    res = requests.api.request('get', 'https://atlantacodecamp.com/2017/Schedule', verify=False)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)
    time_slots = soup.select('div.col-lg-11 > div.row')
    result = '''{
    "slots": [
'''
    result += ',\n'.join(map(lambda (i, time_slot): format_time_slot(i, time_slot), enumerate(time_slots)))
    result += '''
    ]
}'''
    print(result)

if __name__ == '__main__':
    main()
