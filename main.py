import pygame

pygame.init()
pygame.font.init()

display = pygame.display.set_mode((1280,720))

#Desenho do Jogador 1
player1 = pygame.Rect(0,50,30,150)
player1_score = 0
player1_speed = 1

#Desenho do Jogador 2
player2 = pygame.Rect(1250,80,30,150)
player2_score = 0
player2_speed = 1

#Desenho Bola
Ball = pygame.Rect(600,350,15,15)

Ball_dir_x = 1
Ball_dir_y = 1


font = pygame.font.Font(None, 50)
placar_player1 = font.render(str(player1_score), True, "white")
placar_player2 = font.render(str(player2_score), True, "white")

#Loop do Jogo
cena = "menu"

loop = True

while loop:
    
    if cena == "jogo":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            #Controle do Player1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player1_speed = -1
                elif event.key == pygame.K_s:
                    player1_speed = 1
            #Controle do Player 2
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_o:
                    player2_speed = -1
                elif event.key == pygame.K_l:
                    player2_speed = 1

        if player2_score >= 3:
            cena = "gameover"
        if player1_score >= 3:
            cena = "gamerover"
        #Bolinha em colisao com o player
        if Ball.colliderect(player1) or Ball.colliderect(player2):
            Ball_dir_x *= -1
            hit = pygame.mixer.Sound('assets/pong.wav')
            hit.play()

        #Player 1 nao passa dos limites da tela
        if player1.y <= 0:
            player1.y = 0
        if player1.y >=570:
            player1.y = 570
        #Sempre atualiza a velocidade
        player1.y += player1_speed

        if player2.y <= 0:
            player2.y = 0
        if player2.y >=570:
            player2.y = 570
        #Sempre atualiza a velocidade
        player2.y += player2_speed



        if Ball.x <= 0:
            player2_score += 1
            placar_player2 = font.render(str(player2_score), True, "white")
            Ball.x = 600
            Ball_dir_x *= -1
        elif Ball.x >= 1280:
            player1_score += 1
            placar_player1 = font.render(str(player1_score), True, "white")
            Ball.x = 600
            Ball_dir_x *= -1

        #Direcao da bolinha
        if Ball.y <= 0:
            Ball_dir_y *= -1
        elif Ball.y >= 720 - 15:
            Ball_dir_y *= -1

        Ball.x += Ball_dir_x
        Ball.y += Ball_dir_y

        #player2.y = Ball.y - 75

        if player2.y <= 0:
            player2.y = 0
        if player2.y >=570:
            player2.y = 570



        #desenhar na tela
        display.fill((0,0,0))
        pygame.draw.rect(display,"white", player1)
        pygame.draw.rect(display,"white", player2)
        pygame.draw.circle(display, "white", Ball.center, 8)
        display.blit(placar_player1, (500,50))
        display.blit(placar_player2, (780,50))
    
    elif cena == "gameover":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

        display.fill((0,0,0))
        if player2_score == 3:
            text_win = font.render("GAME OVER", True, "white")
            tex_vencedor = font.render("PLAYER 2 VENCEU!!!", True, "white")
            display.blit(text_win, (540, 360))
            display.blit(tex_vencedor,(480,550))
        
        if player1_score == 3:
            text_win = font.render("GAME OVER", True, "white")
            tex_vencedor = font.render("PLAYER 1 VENCEU!!!", True, "white")
            display.blit(text_win, (540, 360))
            display.blit(tex_vencedor, (480, 550))
        
    elif cena == "menu":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    cena = "jogo"
        
        display.fill((0,0,0))
        titulo = font.render("MEU JOGO", True, "white")
        texto = font.render("PRESSIONE START PARA COMEÇAR", True, "white")
        display.blit(titulo, (540, 360))
        display.blit(texto, (320, 550))


    pygame.display.flip()
