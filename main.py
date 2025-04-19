push_ups = {
    "exercise": "Push-ups",
    "sets": 3,
    "reps": 15,
    "notes": "Keep your back straight, hands shoulder-width apart."
}

# Accessing and printing each key
for key in push_ups:
    print(f"{key}: {push_ups[key]}")

# Update the sets for Push-ups
push_ups["sets"] = 5
print(push_ups["sets"])  # It should now print 5

# Delete the notes key
del push_ups["notes"]

# Add the 'workout_notes' key with the same value as 'notes'
push_ups["workout_notes"] = "Keep your back straight, hands shoulder-width apart."
print(push_ups["workout_notes"])

# Accessing the 'notes' for Lunges
workout_plan = {
    "Push-ups": {
        "sets": 3,
        "reps": 15,
        "notes": "Keep your back straight, hands shoulder-width apart."
    },
    "Squats": {
        "sets": 4,
        "reps": 12,
        "notes": "Go as low as you can while maintaining proper form."
    },
    "Plank": {
        "sets": 3,
        "reps": "Hold for 60 seconds",
        "notes": "Engage your core and keep your body in a straight line."
    },
    "Lunges": {
        "sets": 3,
        "reps": 10,
        "notes": "Each leg. Step forward and lower your body until your front knee is at a 90-degree angle."
    },
    "Bicep Curls": {
        "sets": 3,
        "reps": 12,
        "notes": "Use dumbbells, keep your elbows close to your body."
    }
}

# Accessing Lunges notes
lunge_notes = workout_plan["Lunges"]["notes"]
print(lunge_notes)

# Iterating over workout_plan dictionary and printing out all exercises and their details
for exercise, details in workout_plan.items():
    print(f"EXERCISE: {exercise}")
    print(f"SETS: {details['sets']}")
    print(f"REPS: {details['reps']}")
    print(f"WORKOUT_NOTES: {details['notes']}")
    print()

