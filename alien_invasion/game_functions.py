import sys
import pygame
from bullet import Bullet
from alien import Alien
from raindrop import Raindrop


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, aliens, bullets, raindrops):
    """更新屏幕上的图像并切换到新屏幕"""
    # 每次循环都重绘屏幕
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    raindrops.draw(screen)
    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(bullets):
    # 更新子弹位置，并删除已消失的子弹
    bullets.update()
    # 删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.y < 0:
            bullets.remove(bullet)


def fire_bullet(ai_settings, screen, ship, bullets):
    """创建一颗子弹，并将其加入到编组bullets中"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def get_number_rows(ai_settings, ship_height, alien_height):
    # 计算屏幕可容纳多少行
    available_space_y = (ai_settings.screen_height -
                         (3 * alien_height) - ship_height)
    row_numbers = int(available_space_y / (2 * alien_height))
    return row_numbers


def get_number_aliens_x(ai_settings, alien_width):
    """计算每行可以容纳多少个外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    # 创建一个外星人并将其加入当前行
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    alien.rect.x = alien.x
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens, ):
    # 创建外星人群
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    row_numbers = get_number_rows(
        ai_settings, ship.rect.height, alien.rect.height)
    for row_number in range(row_numbers):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens,
                         alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    """有外星人达到边缘时采取相应的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """将外星人整体下移，并改变水平移动方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def update_aliens(ai_settings, aliens):
    """更新外星人的位置"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()


def get_number_raindrop(ai_settings, raindrop_width):
    """计算每行可以容纳的雨点数"""
    available_space_x = ai_settings.screen_width - 2 * raindrop_width
    number_raindrop = int(available_space_x / (2 * raindrop_width))
    return number_raindrop


def create_raindrop(ai_settings, screen, raindrops, number):
    # 创建一个雨滴并加入当前行
    raindrop = Raindrop(ai_settings, screen)
    raindrop_width = raindrop.rect.width
    raindrop.x = raindrop_width + 2 * raindrop_width * number
    raindrop.rect.x = raindrop.x
    raindrop.rect.y = raindrop.rect.height
    raindrops.add(raindrop)


def create_raindrops(ai_settings, screen, raindrops):
    # 创建雨滴群
    raindrop = Raindrop(ai_settings, screen)
    number_raindrop = get_number_raindrop(ai_settings, raindrop.rect.width)
    for number in range(number_raindrop):
        create_raindrop(ai_settings, screen, raindrops, number)


def update_raindrops(ai_settings, screen, raindrops):
    # 更新雨滴的位置
    check_raindrop_edges(ai_settings, screen, raindrops)
    raindrops.update()


def check_raindrop_edges(ai_settings, screen, raindrops):
    """雨滴到达边界，删除改行雨滴，新建一行新的雨滴"""
    for raindrop in raindrops.copy():
        if raindrop.check_edges():
            raindrops.remove(raindrop)
            print(len(raindrops))
    if len(raindrops) == 0:
        create_raindrops(ai_settings, screen, raindrops)
