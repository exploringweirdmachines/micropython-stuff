import time
import random
import asyncio
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY, PEN_P8
from async_stuff import run_concurrent, run_sequential

display = PicoGraphics(display=DISPLAY_PICO_DISPLAY, pen_type=PEN_P8)
display.set_backlight(1.0)

WIDTH, HEIGHT = display.get_bounds()

async def main():
    #run_concurrent()
    #run_sequential()
    pass

if __name__ == "__main__":
    asyncio.run(main())