import pygame

from src.screens import main_menu
from src.tools.button import Button
from src.database.dataBase_sql import find_setting
from utils.function import get_font
from utils.config import cfg


def screen(SCREEN):
    base_font = get_font(32)
    user_time = str(cfg.GAME_SETTING.END_TIME)

    input_rect = pygame.Rect(cfg.GAME_SETTING.WIDTH / 2 + 200, 420, 80, 40)
    color_active = pygame.Color("lightskyblue3")

    # color_passive store color(chartreuse4) which is
    # color of input box.
    color_passive = pygame.Color("white")
    color = color_passive

    active = False
    while True:
        SCREEN.blit(cfg.IMAGES.BG_OPTION[0], (0, 0))
        SCREEN.blit(
            base_font.render(f"CHANGE END TIME", True, "WHITE"),
            (cfg.GAME_SETTING.WIDTH / 2 - 300, 430),
        )  # show score
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        OPTIONS_BACK = Button(
            image=None,
            pos=(cfg.GAME_SETTING.WIDTH / 2 + 50, 300),
            text_input="BACK",
            font=get_font(50),
            base_color="BLACK",
            hovering_color="White",
        )
        OPTIONS_EASY = Button(
            image=None,
            pos=(cfg.GAME_SETTING.WIDTH / 2 - 500, 100),
            text_input="EASY",
            font=get_font(80),
            base_color="Green",
            hovering_color="White",
        )
        OPTIONS_MEDIUM = Button(
            image=None,
            pos=(cfg.GAME_SETTING.WIDTH / 2, 100),
            text_input="MEDIUM",
            font=get_font(80),
            base_color="Orange",
            hovering_color="White",
        )
        OPTIONS_HARD = Button(
            image=None,
            pos=(cfg.GAME_SETTING.WIDTH / 2 + 500, 100),
            text_input="HARD",
            font=get_font(80),
            base_color="Red",
            hovering_color="White",
        )

        OPTIONS_ENTER = Button(
            image=None,
            pos=(cfg.GAME_SETTING.WIDTH / 2 + 420, 450),
            text_input="ENTER",
            font=get_font(30),
            base_color="BLACK",
            hovering_color="White",
        )

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for button in [
            OPTIONS_BACK,
            OPTIONS_EASY,
            OPTIONS_MEDIUM,
            OPTIONS_HARD,
            OPTIONS_ENTER,
        ]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu.screen(SCREEN)
                else:
                    clic = False
                    if OPTIONS_EASY.checkForInput(OPTIONS_MOUSE_POS):
                        clic = True
                        settings = find_setting(
                            "EASY",
                            cfg.GAME_SETTING.HOST,
                            cfg.GAME_SETTING.USER,
                            cfg.GAME_SETTING.PASSWORD,
                            cfg.GAME_SETTING.DATABASE,
                        )
                        cfg.GAME_SETTING.LEVEL = "EASY"
                    if OPTIONS_MEDIUM.checkForInput(OPTIONS_MOUSE_POS):
                        clic = True
                        settings = find_setting(
                            "MEDIUM",
                            cfg.GAME_SETTING.HOST,
                            cfg.GAME_SETTING.USER,
                            cfg.GAME_SETTING.PASSWORD,
                            cfg.GAME_SETTING.DATABASE,
                        )
                        cfg.GAME_SETTING.LEVEL = "MEDIUM"
                    if OPTIONS_HARD.checkForInput(OPTIONS_MOUSE_POS):
                        clic = True
                        settings = find_setting(
                            "HARD",
                            cfg.GAME_SETTING.HOST,
                            cfg.GAME_SETTING.USER,
                            cfg.GAME_SETTING.PASSWORD,
                            cfg.GAME_SETTING.DATABASE,
                        )
                        cfg.GAME_SETTING.LEVEL = "HARD"
                    # ratio
                    if OPTIONS_ENTER.checkForInput(OPTIONS_MOUSE_POS):
                        if user_time != "":
                            end_time = int(float(user_time))
                            cfg.GAME_SETTING.END_TIME = end_time
                            user_time = ""

                    if clic:
                        cfg.GAME_SETTING.RATIO_BONUS = settings[1]
                        cfg.GAME_SETTING.RATIO_BOMB = settings[2]

                        # AMOUNT CREATION BY IT
                        cfg.GAME_SETTING.AMOUNT_IT = settings[3]

                    if input_rect.collidepoint(event.pos):
                        user_time = ""
                        active = True
                    else:
                        active = False

            if event.type == pygame.KEYDOWN:
                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
                    # get text input from 0 to -1 i.e. end.
                    user_time = user_time[:-1]

                # Unicode standard is used for string
                # formation
                if event.unicode.isdigit() and (len(user_time) <= 2):
                    user_time += event.unicode

        if active:
            color = color_active
        else:
            color = color_passive

        # draw rectangle and argument passed which should
        # be on screen

        LEVEL_TEXT = get_font(30).render(
            f"LEVEL : {cfg.GAME_SETTING.LEVEL}", True, "white"
        )
        LEVEL_RECT = LEVEL_TEXT.get_rect(center=(cfg.GAME_SETTING.WIDTH / 2 - 20, 500))

        END_TIME_TEXT = get_font(30).render(
            f"END TIME : {cfg.GAME_SETTING.END_TIME} seconds", True, "white"
        )
        END_TIME_RECT = END_TIME_TEXT.get_rect(
            center=(cfg.GAME_SETTING.WIDTH / 2 - 20, 550)
        )
        SCREEN.blit(LEVEL_TEXT, LEVEL_RECT)
        SCREEN.blit(END_TIME_TEXT, END_TIME_RECT)

        pygame.draw.rect(SCREEN, color, input_rect)

        text_surface = base_font.render(user_time, True, "Black")

        # render at position stated in arguments
        SCREEN.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

        # set width of textfield so that text cannot get
        # outside of user's text input
        input_rect.w = max(100, text_surface.get_width() + 10)

        pygame.display.update()
