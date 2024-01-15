import rrprettier
data={
  "name": "John Doe",
  "age": 30,
  "city": "New York",
  "isStudent": False,
  "courses": ["Math", "Science", "English"],
  "address": {
    "street": "123 Main St",
    "zipCode": "10001"
  }
}
rrprettier.pprint(data)
