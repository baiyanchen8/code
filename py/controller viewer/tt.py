import pygame

pygame.init()

# 初始化手把
pygame.joystick.init()
joystick_count = pygame.joystick.get_count()

if joystick_count > 0:
    # 選擇第一個手把
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    print("手把名稱:", joystick.get_name())
    print("手把數量:", joystick_count)
else:
    print("找不到手把")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.JOYBUTTONDOWN:
            print("press:", event.button)
        elif event.type == pygame.JOYBUTTONUP:
            print("up:", event.button)
        elif event.type == pygame.JOYAXISMOTION:
            print("axis:", event.axis, "value:", event.value)
            
buttonlist=["a","b","x",'y',"lb","rb"]
