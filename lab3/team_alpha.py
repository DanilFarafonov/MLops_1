import gradio as gr
import color_identifier

def generate_image(text, mdjrny):
    # "mdjrny" to add prompthero/openjourney prompt
    if mdjrny:
        text += ', mdjrny-v4 style'
    return picture_gen(text)

def make_palette(image, palette_size):
    return list(color_identifier.get_colours(image, palette_size, False))

def color_table(colors):
    '''Get a color table from a list of color names for Markdown as such:
    | #name | #name | #name |
    | :---: | :---: | :---: |
    | color | color | color |'''

    spaces = ('&emsp;' * 6 + '<br>') * 3
    row_1 = ''.join([f'| {color} ' for color in colors]) + '|'
    row_2 = ''.join(['| :---: ' for _ in colors]) + '|'
    row_3 = ''.join([f'| <span style="background-color: {color}">{spaces}</span> ' for color in colors]) + '|'
    return '\n'.join([row_1, row_2, row_3])

def generate_color_table(text='Apples', palette_size=4, mdjrny=False):
    '''Color table <- List of color names <- Generated image'''
    return color_table(make_palette(generate_image(text, mdjrny), palette_size))

if __name__ == '__main__':
    picture_gen = gr.load(name='models/prompthero/openjourney')  # Stable Diffusion model for image generation

    with gr.Blocks() as palette_generator:
        with gr.Row():

            with gr.Column(scale=1):
                pass

            with gr.Column(scale=2):
                gr.Markdown('''## <p style="text-align: center;">TEAM ALPHA</p>
                ### <p style="text-align: center;">Color palette for any occasion</p>''')
                palette = gr.Markdown()
                seed = gr.Text(label='Input your prompt:')
                palette_size = gr.Slider(3, 6, value=4, step=1, label='Choose palette size:')
                mdjrny = gr.Checkbox(label='In Openjourney style')
                btn = gr.Button('Generate palette')
                gr.Examples(['Cold autumn morning', 'Lonely birthday party', 'Good day for muffins'], inputs=[seed])

            with gr.Column(scale=1):
                pass

        btn.click(generate_color_table, inputs=[seed, palette_size, mdjrny], outputs=[palette])

    palette_generator.launch(server_name='0.0.0.0', server_port=8080)
