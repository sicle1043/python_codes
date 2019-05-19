import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
import game_functions as gf


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建 Play 按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建储存游戏统计信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    scoreboard = Scoreboard(ai_settings, screen, stats)

    # 创建一艘飞船、一个子弹编组和、外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # 创建外星群
    gf.creat_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏循环
    while True:
        gf.check_events(ai_settings, screen, stats, scoreboard, play_button,
                        ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, scoreboard, ship,
                              aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, scoreboard,
                             ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, scoreboard, ship, aliens,
                         bullets, play_button)


if __name__ == "__main__":
    run_game()
