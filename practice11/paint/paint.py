import pygame


WIDTH, HEIGHT = 900, 640
CANVAS = pygame.Rect(0, 0, 760, HEIGHT)
PANEL = pygame.Rect(760, 0, 140, HEIGHT)
WHITE = (255, 255, 255)
BLACK = (20, 24, 28)
COLORS = [BLACK, (220, 60, 60), (50, 120, 220), (60, 160, 90), (240, 190, 60)]
TOOLS = ["square", "right_triangle", "equilateral_triangle", "rhombus"]


def button_rect(index):
    return pygame.Rect(775, 30 + index * 48, 115, 34)


def color_rect(index):
    return pygame.Rect(785 + (index % 2) * 48, 270 + (index // 2) * 48, 34, 34)


def draw_shape(surface, tool, start, end, color, width):
    """Draw only the four figures requested in Practice 11."""
    x1, y1 = start
    x2, y2 = end
    rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))

    if tool == "square":
        side = max(rect.width, rect.height)
        rect = pygame.Rect(x1, y1, side if x2 >= x1 else -side, side if y2 >= y1 else -side)
        rect.normalize()
        pygame.draw.rect(surface, color, rect, width)
    elif tool == "right_triangle":
        pygame.draw.polygon(surface, color, [(x1, y1), (x1, y2), (x2, y2)], width)
    elif tool == "equilateral_triangle":
        pygame.draw.polygon(surface, color, [(rect.centerx, rect.top), (rect.left, rect.bottom), (rect.right, rect.bottom)], width)
    elif tool == "rhombus":
        pygame.draw.polygon(surface, color, [(rect.centerx, rect.top), (rect.right, rect.centery), (rect.centerx, rect.bottom), (rect.left, rect.centery)], width)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Practice 11 Paint")
    font = pygame.font.SysFont("arial", 15)
    clock = pygame.time.Clock()

    canvas = pygame.Surface(CANVAS.size)
    canvas.fill(WHITE)
    tool, color, size = "square", BLACK, 4
    drawing, start = False, None

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
                    drawing, start = True, canvas_mouse

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and drawing:
                drawing = False
                draw_shape(canvas, tool, start, canvas_mouse, color, size)

        screen.fill((220, 220, 220))
        screen.blit(canvas, CANVAS.topleft)
        if drawing:
            preview = canvas.copy()
            draw_shape(preview, tool, start, canvas_mouse, color, size)
            screen.blit(preview, CANVAS.topleft)

        pygame.draw.rect(screen, (238, 238, 232), PANEL)
        for i, name in enumerate(TOOLS):
            rect = button_rect(i)
            pygame.draw.rect(screen, (70, 130, 210) if name == tool else WHITE, rect)
            pygame.draw.rect(screen, BLACK, rect, 1)
            screen.blit(font.render(name, True, BLACK), (rect.x + 5, rect.y + 8))
        for i, palette_color in enumerate(COLORS):
            rect = color_rect(i)
            pygame.draw.rect(screen, palette_color, rect)
            pygame.draw.rect(screen, BLACK, rect, 2 if palette_color == color else 1)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
