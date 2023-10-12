from Tools import *


class Pong:
    def __init__(self, width, height, speed):
        self.score = [0, 0]

        if width < 16:
            width = 16
        elif width > 150:
            width = 15
        self.width = width

        if height < 8:
            height = 8
        elif width > 40:
            width = 40
        self.height = height

        if speed <= 0:
            speed = 0.01
        elif speed > 1:
            speed = 1
        self.speed = speed

        self.ball_x = width // 2
        self.ball_y = height // 2
        self.paddle_left_y = height // 2
        self.paddle_right_y = height // 2

    def display(self):
        switchScreen()
        print(f"{self.score[LEFT]}{' ' * (self.width - 1)}{self.score[RIGHT]}")
        for y in range(self.height):
            for x in range(self.width):
                if y == 0 or y == self.height - 1:
                    print("=", end="")
                elif y == self.ball_y and x == self.ball_x:
                    print("O", end="")
                elif y in range(self.paddle_left_y - 2, self.paddle_left_y + 3) and x == 1:
                    print("|", end="")
                elif y in range(self.paddle_right_y - 2, self.paddle_right_y + 3) and x == self.width - 2:
                    print("|", end="")
                else:
                    print(" ", end="")
            print()
        print("PRESS 'x' TO EXIT")

    def update_ball(self, ball_dir_x, ball_dir_y):
        projected_x = self.ball_x + ball_dir_x
        projected_y = self.ball_y + ball_dir_y

        # ball hit top and bottom walls
        if projected_y <= 0 or projected_y >= self.height - 1:
            ball_dir_y *= -1

        # ball hit paddles
        if (projected_x == 1 and self.paddle_left_y - 2 <= projected_y <= self.paddle_left_y + 3) or \
                (projected_x == self.width - 2 and self.paddle_right_y - 2 <= projected_y <= self.paddle_right_y + 3):
            ball_dir_x *= -1

        # ball out of bounds
        if projected_x <= 0 or projected_x >= self.width:
            self.ball_x = self.width // 2
            self.ball_y = self.height // 2

            if random.randint(0, 2) == 1:
                ball_dir_x *= -1
            if random.randint(0, 2) == 1:
                ball_dir_y *= -1

            if projected_x <= 0:
                self.score[RIGHT] += 1
            else:
                self.score[LEFT] += 1

        self.ball_x += ball_dir_x
        self.ball_y += ball_dir_y

        return ball_dir_x, ball_dir_y

    def play(self):
        ball_direction_x = -1
        ball_direction_y = 1

        while not keyboard.is_pressed('x'):
            self.display()

            if keyboard.is_pressed('w') and self.paddle_left_y > 3:
                self.paddle_left_y -= 1
            if keyboard.is_pressed('s') and self.paddle_left_y < self.height - 4:
                self.paddle_left_y += 1

            if keyboard.is_pressed('up') and self.paddle_right_y > 3:
                self.paddle_right_y -= 1
            if keyboard.is_pressed('down') and self.paddle_right_y < self.height - 4:
                self.paddle_right_y += 1

            ball_direction_x, ball_direction_y = self.update_ball(ball_direction_x, ball_direction_y)
            time.sleep(self.speed)


Pong(80, 20, 0.04).play()
