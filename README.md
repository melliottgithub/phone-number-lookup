# Phone Number Lookup Service

This is a simple phone number lookup service that provides information about phone numbers, including the country code, area code, and local phone number.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/melliottgithub/phone-number-lookup.git
   ```

2. Install the dependencies:
   ```bash
   set up a virtual environment
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask development server:
   python services/app.py

2. Access the phone number lookup service:

```bash
curl -i -X GET "http://127.0.0.1:5000/v1/phone-numbers?phoneNumber=%2B12125690123"

curl -i -X GET "http://127.0.0.1:5000/v1/phone-numbers?phoneNumber=%2B52%20631%203118150"

curl -i -X GET "http://127.0.0.1:5000/v1/phone-numbers?phoneNumber=%2B34%20915%20872200"

curl -i -X GET "http://127.0.0.1:5000/v1/phone-numbers?phoneNumber=351%2021%20094%20%202000"
```

3. The service will return the phone number details in JSON format, including the formatted phone number, country code, area code, and local phone number.

## API Endpoints

### Phone Number Lookup

- Endpoint: `/v1/phone-numbers`
- Method: `GET`
- Query Parameter:
- `phoneNumber`: The phone number to lookup. It should be URL-encoded.

Example Response:

```json
{
  "phoneNumber": "+12125690123",
  "countryCode": "US",
  "areaCode": "212",
  "localPhoneNumber": "5690123"
}
```

## Testing

To run the unit tests for the phone number lookup service, use the following command:

```bash
 python services/test.py
```

## Deployment WIP
```bash
curl -i -X GET "https://uxhx9b3e7f.execute-api.us-east-1.amazonaws.com/prod/phone-numbers?phoneNumber=%2B12125690123" 
curl -i -X GET "https://uxhx9b3e7f.execute-api.us-east-1.amazonaws.com/prod/phone-numbers?phoneNumber=%2B52%20631%203118150" 
curl -i -X GET "https://uxhx9b3e7f.execute-api.us-east-1.amazonaws.com/prod/phone-numbers?phoneNumber=%2B34%20915%20872200" 
```