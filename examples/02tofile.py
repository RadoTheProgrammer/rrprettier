import rrprettier
data={
  "name": "John Doe",
  "age": 30,
  "city": "New York City",
  "isStudent": False,
  "courses": ["Math", "Science", "English"],
  "address": {
    "street": "123 Main St",
    "zipCode": "10001"
  }
}
rrprettier.tofile(data) 


