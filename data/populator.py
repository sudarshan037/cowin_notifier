import json

data_users = {
    'Sudarshan Choudhary': ['311022'],
    '@manjeettanwar1026': ['302012', '302013'],
    '@zedd5321': ['302013', '302003', '302004', '302020', '302017', '302033', '302018']
}

data_districts = {
    'Bhilwara': '523',
    'Jaipur I': '505',
    'Jaipur II': '506'
}


def user_populator(users):
    data = {}
    unique_code = set()
    for user in users.keys():
        unique_code = unique_code.union(set(users[user]))
        for pincode in users[user]:
            try:
                data[pincode].append(user)
            except KeyError:
                data[pincode] = [user]
    for code in unique_code:
        data[code].append('Sudarshan Choudhary')
    data['311022'] = ['Sudarshan Choudhary']
    with open("users.json", "w") as u:
        json.dump(data, u)


def district_populator(districts):
    with open('districts.json', 'w') as d:
        json.dump(districts, d)


if __name__ == "__main__":
    user_populator(data_users)
    district_populator(data_districts)
