import sys
import random

try:
    import pygame
except ImportError:
    print("Error: pygame is not installed. Install it with 'pip install pygame'.")
    sys.exit(1)

# -----------------------------
# START PYGAME
# -----------------------------
pygame.init()

# Screen
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("⭐ Catch the Stars ⭐")

clock = pygame.time.Clock()

# -----------------------------
# COLORS
# -----------------------------
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 150, 255)
YELLOW = (255, 255, 0)
RED = (255, 50, 50)
GREEN = (50, 255, 100)

# -----------------------------
# FONTS
# -----------------------------
score_font = pygame.font.Font(None, 40)
game_over_font = pygame.font.Font(None, 80)
message_font = pygame.font.Font(None, 40)

# -----------------------------
# GAME SETTINGS
# -----------------------------

catcher_width = 120
catcher_height = 25
catcher_speed = 8

star_size = 20
star_speed = 5

# -----------------------------
# RESET GAME FUNCTION
# -----------------------------

def reset_game():

    global catcher_x
    global star_x
    global star_y
    global star_speed
    global score
    global lives
    global game_over

    # Catcher position
    catcher_x = WIDTH // 2 - catcher_width // 2

    # Star position
    star_x = random.randint(0, WIDTH - star_size)
    star_y = 0

    # Speed
    star_speed = 5

    # Score
    score = 0

    # Lives
    lives = 3

    # Game state
    game_over = False


# Start the game
reset_game()

# -----------------------------
# MAIN GAME LOOP
# -----------------------------

running = True

while running:

    # -------------------------
    # EVENTS
    # -------------------------

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Restart with R
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_r and game_over:
                reset_game()

            # Quit with Q
            if event.key == pygame.K_q:
                running = False

    # -------------------------
    # GAME IS RUNNING
    # -------------------------

    if not game_over:

        # Keyboard
        keys = pygame.key.get_pressed()

        # Move LEFT
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            catcher_x -= catcher_speed

        # Move RIGHT
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            catcher_x += catcher_speed

        # Keep catcher inside screen
        if catcher_x < 0:
            catcher_x = 0

        if catcher_x > WIDTH - catcher_width:
            catcher_x = WIDTH - catcher_width

        # -------------------------
        # MOVE STAR
        # -------------------------

        star_y += star_speed

        # Create catcher rectangle
        catcher = pygame.Rect(
            catcher_x,
            HEIGHT - 60,
            catcher_width,
            catcher_height
        )

        # Create star rectangle
        star = pygame.Rect(
            star_x,
            star_y,
            star_size,
            star_size
        )

        # -------------------------
        # CATCH STAR
        # -------------------------

        if catcher.colliderect(star):

            score += 1

            # New star
            star_x = random.randint(
                0,
                WIDTH - star_size
            )

            star_y = 0

            # Make game harder
            star_speed += 0.3

        # -------------------------
        # MISS STAR
        # -------------------------

        if star_y > HEIGHT:

            lives -= 1

            # New star
            star_x = random.randint(
                0,
                WIDTH - star_size
            )

            star_y = 0

            # Check Game Over
            if lives <= 0:
                game_over = True

    # -------------------------
    # DRAW BACKGROUND
    # -------------------------

    screen.fill(BLACK)

    # -------------------------
    # DRAW CATCHER
    # -------------------------

    catcher = pygame.Rect(
        catcher_x,
        HEIGHT - 60,
        catcher_width,
        catcher_height
    )

    pygame.draw.rect(
        screen,
        BLUE,
        catcher
    )

    # -------------------------
    # DRAW STAR
    # -------------------------

    if not game_over:

        pygame.draw.circle(
            screen,
            YELLOW,
            (
                star_x + star_size // 2,
                star_y + star_size // 2
            ),
            star_size // 2
        )

    # -------------------------
    # SCORE
    # -------------------------

    score_text = score_font.render(
        f"Score: {score}",
        True,
        WHITE
    )

    screen.blit(
        score_text,
        (20, 20)
    )

    # -------------------------
    # LIVES
    # -------------------------

    lives_text = score_font.render(
        f"Lives: {'❤️' * lives}",
        True,
        RED
    )

    screen.blit(
        lives_text,
        (550, 20)
    )

    # -------------------------
    # GAME OVER SCREEN
    # -------------------------

    if game_over:

        # Game Over
        game_over_text = game_over_font.render(
            "GAME OVER!",
            True,
            RED
        )

        screen.blit(
            game_over_text,
            (
                WIDTH // 2 -
                game_over_text.get_width() // 2,
                200
            )
        )

        # Final Score
        final_score = message_font.render(
            f"Final Score: {score}",
            True,
            WHITE
        )

        screen.blit(
            final_score,
            (
                WIDTH // 2 -
                final_score.get_width() // 2,
                300
            )
        )

        # Restart
        restart_text = message_font.render(
            "Press R to Restart",
            True,
            GREEN
        )

        screen.blit(
            restart_text,
            (
                WIDTH // 2 -
                restart_text.get_width() // 2,
                370
            )
        )

        # Quit
        quit_text = message_font.render(
            "Press Q to Quit",
            True,
            WHITE
        )

        screen.blit(
            quit_text,
            (
                WIDTH // 2 -
                quit_text.get_width() // 2,
                420
            )
        )

    # -------------------------
    # UPDATE SCREEN
    # -------------------------

    pygame.display.flip()

    # 60 FPS
    clock.tick(60)


# -----------------------------
# CLOSE PYGAME
# -----------------------------

pygame.quit()