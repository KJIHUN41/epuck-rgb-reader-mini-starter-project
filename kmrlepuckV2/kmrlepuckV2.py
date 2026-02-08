from controller import Robot, Camera, Keyboard

# Robot ve timestep
robot = Robot()
timestep = int(robot.getBasicTimeStep())

# Motorlar
left_motor = robot.getDevice("left wheel motor")
right_motor = robot.getDevice("right wheel motor")
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

# Klavye
keyboard = Keyboard()
keyboard.enable(timestep)
max_speed = 6.28

# Kamera
camera = robot.getDevice("camera")
camera.enable(timestep)
width = camera.getWidth()
height = camera.getHeight()

# Main loop
while robot.step(timestep) != -1:
    # Kamera görüntüsü ve RGB değerleri
    image = camera.getImage()
    r = camera.imageGetRed(image, width, width//2, height//2)
    g = camera.imageGetGreen(image, width, width//2, height//2)
    b = camera.imageGetBlue(image, width, width//2, height//2)

    print(f"R:{r}, G:{g}, B:{b}")

    # Klavye tuşu oku
    key = keyboard.getKey()

    # Tuş kontrolü
    if key == ord('W') or key == ord('w'):  # ileri
        left_motor.setVelocity(max_speed)
        right_motor.setVelocity(max_speed)
    elif key == ord('S') or key == ord('s'):  # geri
        left_motor.setVelocity(-max_speed)
        right_motor.setVelocity(-max_speed)
    elif key == ord('A') or key == ord('a'):  # sola dön
        left_motor.setVelocity(-max_speed)
        right_motor.setVelocity(max_speed)
    elif key == ord('D') or key == ord('d'):  # sağa dön
        left_motor.setVelocity(max_speed)
        right_motor.setVelocity(-max_speed)
    else:  # tuş bırakıldığında dur
        left_motor.setVelocity(0.0)
        right_motor.setVelocity(0.0)
