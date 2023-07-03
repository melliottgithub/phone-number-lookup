import re
from flask import Flask, request, jsonify
import phonenumbers

app = Flask(__name__)

class PhoneNumberLookup:
    def process_phone_number(self, phone_number):
        phone_number = str(phone_number)

        if not phone_number:
            return jsonify({
                'error': {
                    'message': 'Missing or invalid phoneNumber'
                }
            }), 400

        if not phone_number.startswith('+'):
            phone_number = '+' + phone_number

        if re.search(r'\d\s{2,}\d', phone_number):
            return jsonify({
                'phoneNumber': phone_number,
                'error': {
                    'message': 'Invalid phone number format'
                }
            }), 400

        phone_number = phone_number.replace(' ', '')

        try:
            parsed_number = phonenumbers.parse(phone_number, None)
        except phonenumbers.phonenumberutil.NumberParseException as e:
            error_message = str(e).split(":")[0]
            return jsonify({
                'phoneNumber': phone_number,
                'error': {
                    'message': error_message
                }
            }), 400

        formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
        national_number = str(parsed_number.national_number)
        area_code = str(parsed_number.national_number)[:3]

        return jsonify({
            'phoneNumber': formatted_number,
            'countryCode': phonenumbers.region_code_for_number(parsed_number),
            'areaCode': area_code,
            'localPhoneNumber': national_number[len(area_code):]
        })

@app.route('/v1/phone-numbers', methods=['GET'])
def phone_number_lookup():
    phone_number = request.args.get('phoneNumber')

    lookup = PhoneNumberLookup()
    return lookup.process_phone_number(phone_number)


if __name__ == '__main__':
    app.run(debug=True)
