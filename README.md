# NVIDIA-Line-Detection
Aim
To implement a line-following control rule based on pixel offset.
General Objective
To understand line-following in autonomous robots and how image-based offsets are used to generate steering corrections.
Specific Objective
To apply the rule:
Offset = +25 px
If offset > 0 → Turn Left (robot drifted right)
Dataset
OpenCV Line Dataset
Source: OpenCV Extra Modules
Procedure
Input pixel offset
Check sign of offset
If offset > 0 → Turn Left
Else → Turn Right or Straight
Display result
Algorithm
Start
Input offset
If offset > 0 → Turn Left
Else if offset < 0 → Turn Right
Else → Move Straight
Display result
Stop
Code Logic
if offset > 0:
    action = "Turn Left"
Python Code
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
Output
Turn Left

Program Executed Successfully
Result
Since the offset is positive:
Turn Left action is executed
Industry Application
Line detection is used in:
Autonomous vehicles
Line-following robots
Industrial automation
Vision-based navigation
Companies like NVIDIA use this in:
Computer vision systems
Autonomous driving
Robotics AI
Conclusion
Pixel offset-based correction enables accurate line tracking, which is essential for vision-based navigation systems.
