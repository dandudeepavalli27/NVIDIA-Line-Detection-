# SESSION 36 – Line Detection (Line Following)

# Step 1: Input offset
offset = 25   # positive pixel offset

# Step 2: Apply control rule
if offset > 0:
    print("Turn Left")
elif offset < 0:
    print("Turn Right")
else:
    print("Move Straight")

print("\nProgram Executed Successfully")
