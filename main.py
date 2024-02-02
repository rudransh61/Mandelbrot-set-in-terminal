def mandelbrot(c, max_iterations):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iterations:
        z = z**2 + c
        n += 1
    return n

def generate_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iterations):
    result = ""
    for row in range(height):
        for col in range(width):
            x = x_min + (x_max - x_min) * col / (width - 1)
            y = y_min + (y_max - y_min) * row / (height - 1)
            c = complex(x, y)
            value = mandelbrot(c, max_iterations)
            if value == max_iterations:
                result += "#"
            else:
                result += " "
        result += "\n"
    return result

if __name__ == "__main__":
    # Set parameters
    width = 160
    height = 40
    x_min, x_max = -2, 2
    y_min, y_max = -1, 1
    max_iterations = 50

    # Generate and print Mandelbrot set
    mandelbrot_set = generate_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iterations)
    print(mandelbrot_set)
    input(":")