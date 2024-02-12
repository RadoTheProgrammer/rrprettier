# RRPrettier

A tool to prettify data of python objects

A simple example in python:

```python
import rrprettier
data={
"name": "John Doe",
"age": 56,
"city": "New york",
"isStudent": False,
"courses": ["Math", "Science", "English"],
"address": {
    "street": "123 Main St",
    "zipCode": "10001"
}
}
rrprettier.pprint(data)
```
