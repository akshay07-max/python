Part 10: Complete Example - Traffic Light System
print("=== Traffic Light System ===\n")

light = input("Enter light color (red/yellow/green): ").lower()

if light == "green":
    print("✓ GO - Drive safely")
elif light == "yellow":
    print("⚠ SLOW DOWN - Prepare to stop")
elif light == "red":
    print("✋ STOP - Wait for green")
else:
    print("❌ Invalid color - Check the light!")

print("\nDrive safely!")
Example runs:
=== Traffic Light System ===

Enter light color (red/yellow/green): green
✓ GO - Drive safely

Drive safely!
Enter light color (red/yellow/green): RED
✋ STOP - Wait for green

Drive safely!
Note: We used .lower() to handle uppercase input!