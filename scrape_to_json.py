import requests
import bs4
import json

# sudo apt-get install python3-bs4
# sudo apt-get install python3-requests


def extract_session(session_elements):
    info = session_elements.findChildren()
    return {
        'title': info[0].getText(),
        'presenter': info[1].getText(),
        'room': info[2].getText().replace('Room: ', ''),
        'category': info[3].getText().replace('Category: ', '')
    }


def extract_time_slot(i, time_slot):
    session_elements = time_slot.select('div.schedule-item')
    sessions = map(extract_session, session_elements)
    return {
        'name': 'Slot {index}'.format(index=i + 1),
        'sessions': list(sessions)
    }


def main():
    res = requests.api.request(
            'get',
            'https://atlantacodecamp.com/2017/Schedule',
            verify=False
    )
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    time_slot_elements = soup.select('div.col-lg-11 > div.row')
    time_slots = [
            extract_time_slot(i, time_slot)
            for i, time_slot in enumerate(time_slot_elements)
    ]
    result = {
        'slots': list(time_slots)
    }
    print(json.dumps(result, sort_keys=True, indent=4))


if __name__ == '__main__':
    main()
