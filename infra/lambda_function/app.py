import re
import json
import phonenumbers

def lambda_handler(event, context):
    phone_number = event['queryStringParameters']['phoneNumber']

    if not phone_number.startswith('+'):
        phone_number = '+' + phone_number

    phone_number = phone_number.replace(' ', '')

    if re.search(r'\d\s{2,}\d', phone_number):
        return {
            'statusCode': 400,
            'body': json.dumps({
                'phoneNumber': phone_number,
                'error': {
                    'message': 'Invalid phone number format'
                }
            })
        }

    try:
        parsed_number = phonenumbers.parse(phone_number, None)
    except phonenumbers.phonenumberutil.NumberParseException as e:
        error_message = str(e).split(":")[0]
        return {
            'statusCode': 400,
            'body': json.dumps({
                'phoneNumber': phone_number,
                'error': {
                    'message': error_message
                }
            })
        }

    formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
    national_number = str(parsed_number.national_number)
    area_code = str(parsed_number.national_number)[:3]

    return {
        'statusCode': 200,
        'body': json.dumps({
            'phoneNumber': formatted_number,
            'countryCode': phonenumbers.region_code_for_number(parsed_number),
            'areaCode': area_code,
            'localPhoneNumber': national_number[len(area_code):]
        })
    }
