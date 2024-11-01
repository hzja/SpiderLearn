import pygame
import sys
from pygame.locals import *
import numpy as np


class Card(pygame.sprite.Sprite):
    def __init__(self, x, y, card_state):
        self.image = pygame.image.load("images/card.png")
        width, height = self.image.get_size()
        self.rect = (x, y, width, height)
        # 切换卡片牌面
        self.card_state = card_state

    def update(self):
        # 当牌面为 2 时显示哭脸
        if self.card_state == 2:
            self.image = pygame.image.load("images/cry.png")

        if self.card_state == 3:
            self.image = pygame.image.load("images/fuzong.png")
            self.image = pygame.transform.scale(self.image, (100, 100))

        if self.card_state == 4:
            self.image = pygame.image.load("images/zong.jpg")
            self.image = pygame.transform.scale(self.image, (100, 100))


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((900, 600))
        pygame.display.set_caption("总裁翻牌")
        self.clock = pygame.time.Clock()

        self.card_nums = 28
        self.points = self.all_point()

        # 点击卡片记录数组
        self.click_list = []

        # 随机生成数组，中奖为1，不中奖为0
        self.win_list = list(np.random.randint(0, 3, 28))

    def all_point(self):
        points = []
        for num in range(self.card_nums):
            if num // 7 == 0:
                x = num * 120 + 40
                y = 45
            elif num // 7 == 1:
                x = (num - 7) * 120 + 40
                y = 175
            elif num // 7 == 2:
                x = (num - 7 * 2) * 120 + 40
                y = 305
            elif num // 7 == 3:
                x = (num - 7 * 3) * 120 + 40
                y = 435
            points.append((x, y))
        return points

    def set_bg(self):
        bg = pygame.image.load("images/bg.png")
        # width, height = bg.get_size()
        # 素材缩小
        # pygame.transform.scale(bg,(width,height))
        self.screen.blit(bg, (0, 0))

    # 绘制牌子
    def set_card(self):
        for i, num in enumerate(self.points):
            x, y = num
            card_state = 1
            # 卡片是否被点击
            if i in self.click_list:
                card_state = 2
            # 卡片是否被点击
            if i in self.click_list and self.win_list[i] == 1:
                card_state = 3
            # 卡片是否被点击
            if i in self.click_list and self.win_list[i] == 2:
                card_state = 4

            card = Card(x, y, card_state)
            card.update()
            self.screen.blit(card.image, card.rect)

    # 计算鼠标点击卡片
    def mouse_card(self, mosx, mosy):
        for i, (x, y) in enumerate(self.points):
            if (mosx >= x and mosx <= (x + 100)) and (mosy >= y and mosy <= (y + 100)):
                print("翻牌，点到卡片序号为", i)
                self.click_list.append(i)

    def run(self):

        while True:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == MOUSEBUTTONDOWN:
                    mosx, mosy = event.pos
                    self.mouse_card(mosx, mosy)

            self.set_bg()
            self.set_card()

            pygame.display.update()


if __name__ == '__main__':
    g = Game()
    g.run()
