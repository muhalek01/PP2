import pygame


WIDTH, HEIGHT = 900, 640
CANVAS = pygame.Rect(0, 0, 760, HEIGHT)
PANEL = pygame.Rect(760, 0, 140, HEIGHT)
WHITE = (255, 255, 255)
BLACK = (20, 24, 28)
COLORS = [BLACK, (220, 60, 60), (50, 120, 220), (60, 160, 90), (240, 190, 60), WHITE]
TOOLS = ["pencil", "rectangle", "circle", "eraser"]


def button_rect(index):
    return pygame.Rect(780, 30 + index * 48, 100, 34)


def color_rect(index):
    return pygame.Rect(785 + (index % 2) * 48, 270 + (index // 2) * 48, 34, 34)


def draw_shape(surface, tool, start, end, color, width):
    """Draw the required Practice 10 shapes from mouse drag coordinates."""
    rect = pygame.Rect(min(start[0], end[0]), min(start[1], end[1]), abs(end[0] - start[0]), abs(end[1] - start[1]))
    if tool == "rectangle":
        pygame.draw.rect(surface, color, rect, width)
    elif tool == "circle":
        pygame.draw.ellipse(surface, color, rect, width)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Practice 10 Paint")
    font = pygame.font.SysFont("arial", 16)
    clock = pygame.time.Clock()

    canvas = pygame.Surface(CANVAS.size)
    canvas.fill(WHITE)
    tool, color, size = "pencil", BLACK, 5
    drawing, start, last = False, None, None

    while True:
        mouse = pygame.mouse.get_pos()
        canvas_mouse = (mouse[0] - CANVAS.x, mouse[1] - CANVAS.y)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for i, name in enumerate(TOOLS):
                    if button_rect(i).collidepoint(event.pos):
                        tool = name
                for i, palette_color in enumerate(COLORS):
                    if color_rect(i).collidepoint(event.pos):
                        color = palette_color
                if CANVAS.collidepoint(event.pos):
                    drawing, start, last = True, canvas_mouse, canvas_mouse

            if event.type == pygame.MOUSEMOTION and drawing and tool in {"pencil", "eraser"}:
                draw_color = WHITE if tool == "eraser" else color
                pygame.draw.line(canvas, draw_color, last, canvas_mouse, size)
                last = canvas_mouse

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and drawing:
                drawing = False
                if tool in {"rectangle", "circle"}:
                    draw_shape(canvas, tool, start, canvas_mouse, color, size)

        screen.fill((220, 220, 220))
        screen.blit(canvas, CANVAS.topleft)
        if drawing and tool in {"rectangle", "circle"}:
            preview = canvas.copy()
            draw_shape(preview, tool, start, canvas_mouse, color, size)
            screen.blit(preview, CANVAS.topleft)

        pygame.draw.rect(screen, (238, 238, 232), PANEL)
        for i, name in enumerate(TOOLS):
            rect = button_rect(i)
            pygame.draw.rect(screen, (70, 130, 210) if name == tool else WHITE, rect)
            pygame.draw.rect(screen, BLACK, rect, 1)
            screen.blit(font.render(name, True, BLACK), (rect.x + 8, rect.y + 8))
        for i, palette_color in enumerate(COLORS):
            rect = color_rect(i)
            pygame.draw.rect(screen, palette_color, rect)
            pygame.draw.rect(screen, BLACK, rect, 2 if palette_color == color else 1)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
