import tqdm
from PIL import Image, ImageDraw, ImageFont


def render_frame(i, frame_start, frame_end):

	sim_time_ns = 1000*(i - frame_start)/(frame_end-frame_start)
	img = Image.new('RGBA', (2560, 1440), color = (0, 0, 0, 0))
	fnt = ImageFont.truetype('/usr/share/fonts/OTF/FiraCode-Regular.otf', 60)
	d = ImageDraw.Draw(img)
	d.text(
		(10,10), 
		't = {}'.format(f'{sim_time_ns:7.3f} ns'),
		font=fnt,
		fill=(255, 255, 255, 255)
	)
	img.save(f'frame_{i}.png')


def render_frames():

	frame_start = 1329
	frame_end = 6120

	for i in tqdm.trange(frame_start, frame_end):
		render_frame(i, frame_start, frame_end)


if __name__=='__main__':
	render_frames()
