
def screen():
    base_font = get_font(32)
    user_text_default = cfg.GAME_SETTING.NAME
    user_text = user_text_default
    input_rect = pygame.Rect(cfg.GAME_SETTING.WIDTH / 2 - 200, 350, 150, 80)
    color_active = pygame.Color("lightskyblue3")

    # color_passive store color(chartreuse4) which is
    # color of input box.
    color_passive = pygame.Color("white")
    color = color_passive

    active = False
    while True:
        SCREEN.blit(BG_JUNGLE, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        NAME_TEXT = get_font(50).render("CHOOSE YOUR NAME", True, "white")
        MENU_RECT = NAME_TEXT.get_rect(center=(cfg.GAME_SETTING.WIDTH / 2, 300))

        PLAY_BUTTON = Button(
            image=pygame.image.load(
                os.path.join(cfg.PATHS.ASSET_PATH, "Play Rect.png")
            ),
            pos=(cfg.GAME_SETTING.WIDTH / 2, 700),
            text_input="PLAY",
            font=get_font(75),
            base_color="#d7fcd4",
            hovering_color="White",
        )
        BACK_BUTTON = Button(
            image=pygame.image.load(
                os.path.join(cfg.PATHS.ASSET_PATH, "Quit Rect.png")
            ),
            pos=(cfg.GAME_SETTING.WIDTH / 2, 900),
            text_input="BACK",
            font=get_font(75),
            base_color="#d7fcd4",
            hovering_color="White",
        )

        SCREEN.blit(NAME_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, BACK_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    if len(user_text) > 0:
                        cfg.GAME_SETTING.NAME = user_text
                    play()
                if BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_menu()

                if input_rect.collidepoint(event.pos):
                    user_text = ""
                    active = True
                else:
                    active = False

            if event.type == pygame.KEYDOWN:
                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
                    # get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]

                # Unicode standard is used for string
                # formation
                elif (event.key == pygame.K_RETURN) and (len(user_text) > 0):
                    cfg.GAME_SETTING.NAME = user_text
                    play()

                else:
                    user_text += event.unicode

        if active:
            color = color_active
        else:
            color = color_passive

        # draw rectangle and argument passed which should
        # be on screen
        pygame.draw.rect(SCREEN, color, input_rect)

        text_surface = base_font.render(user_text, True, "Black")

        # render at position stated in arguments
        SCREEN.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

        # set width of textfield so that text cannot get
        # outside of user's text input
        input_rect.w = max(100, text_surface.get_width() + 10)

        pygame.display.update()


