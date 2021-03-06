"""This script generates a set of 2560x1440 images which are mostly transparent
except for a timer in the top left. This timer shows the simulation time of the
frame currently being displayed. Although the total mumax simulation ran for
1000 ns, after the first 96 ns (corresponding to 480 mumax output files) the
domain wall annihilated, so I clipped the final rendered animation short.

The images generated here are then overlayed on top of the animation of the
simulation using blender's Video Editing tab.
"""
import tqdm
from PIL import Image, ImageDraw, ImageFont


def render_frame(i, frame_start, frame_end):
    """Generate an image displaying the current simulation time.

    The animation contains simulation data from the first 96 ns of the
    simulation.

    Parameters
    ----------
    i : int
        Index of the current frame
    frame_start : int
        Index of the frame the simulation animation begins playing
    frame_end : int
        Index of the frame the simulation animation stops playing
    """

    sim_time_ns = 96*(i - frame_start)/(frame_end-frame_start)
    img = Image.new('RGBA', (2560, 1440), color=(0, 0, 0, 0))
    fnt = ImageFont.truetype('/usr/share/fonts/OTF/FiraCode-Regular.otf', 60)
    d = ImageDraw.Draw(img)
    d.text(
        (10, 10),
        't = {}'.format(f'{sim_time_ns:7.3f} ns'),
        font=fnt,
        fill=(255, 255, 255, 255)
    )
    img.save(f'frame_{i}.png')


def render_frames():
    """Render the timer frames for the whole animation."""

    frame_start = 1329
    frame_end = 6120

    for i in tqdm.trange(frame_start, frame_end):
        render_frame(i, frame_start, frame_end)


if __name__ == '__main__':
    render_frames()
