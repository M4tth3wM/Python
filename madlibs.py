"""--------------------------------------------------
[✅] 1. Header Docstring included.
[✅] 2. Program asks for at least 5 different inputs (variables).
[✅] 3. Output uses F-Strings to combine text and variables.
[✅] 4. Output uses at least one escape sequence (\n or \t).
[✅] 5. Code contains comments explaining the steps.
[✅] 6. Program runs without errors.
--------------------------------------------------"""

# ℹ️variables
# animal
# color
# emotion
# action
# place

# ⌨️inputs
animal = input("Name an animal: ")
color = input(f"What color is the {animal}: ")
emotion = input(f"How does the {color} {animal} feel: ")
action = input(f"What is the {emotion} {color} {animal} doing: ")
place = input(f"Where is the {color} {animal}: ")

# 🖨️print string
print(f"\n\nThe {emotion} {color} {animal} is {action} in {place}")
