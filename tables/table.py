from tables import *
from utils import font

map_of_styles = {
    'font-name': font.set_font_name,
    'font-size': font.set_font_size
}


async def apply_styles(styles: dict, element):
    not_applied_styles = set()

    for style in styles:
        if style not in available_styles:
            not_applied_styles.add(style)
            continue

        kwargs = {
            f'{style}': styles[style],
            'element': element
        }
        await map_styles(style, kwargs)


async def map_styles(style: str, kwargs):
    func = map_of_styles.get(style)
    await func(**kwargs)
