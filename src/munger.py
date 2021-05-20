def data_populator(center, session):
    result = {
        'age': session['min_age_limit'],
        'address': center['address'],
        'availability': session['available_capacity'],
        'vaccine': session['vaccine'],
        'pincode': center['pincode'],
        'date': session['date'],
        'center_id': center['center_id'],
        'fee_type': center['fee_type']
    }
    return result


def data_parser(data):
    results = {}
    for center in data['centers']:
        for session in center['sessions']:
            if session['min_age_limit'] == 18 and session['available_capacity'] >= 0:
                try:
                    results[str(center['pincode'])][str(center['center_id'])] = data_populator(center, session)
                except KeyError as e:
                    results[str(center['pincode'])] = {}
                    results[str(center['pincode'])][str(center['center_id'])] = data_populator(center, session)
    return results
