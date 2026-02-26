import json

data = {
    "name": "Alice",
    "age": 30,
    "languages": ["Python", "JavaScript"],
    "active": True,
}

serialized = json.dumps(data, indent=2)
print("Serialized JSON string:")
print(serialized)

deserialized = json.loads(serialized)
print("\nDeserialized back to dict:")
print(deserialized)
print(f"\nType: {type(deserialized)}")
