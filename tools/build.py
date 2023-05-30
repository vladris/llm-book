import os
from baku.markdown import make_markdown_processor
from baku.templating import render, VerySimpleTemplate


# Clean up the site directory
for file in os.listdir('site'):
    if file.endswith('.html'):
        os.remove(os.path.join('site', file))


# Chapter title mappings
chapter_titles = {
    '01': 'A New Paradigm',
    '02': 'Large Language Models',
    '03': 'Prompt Engineering',
    '04': 'Learning and Tuning',
    '05': 'Memory and Embeddings',
}


# Render markdown files
md = make_markdown_processor()
for file in os.listdir('text'):
    if not file.endswith('.md'):
        continue

    filepath = os.path.join('text', file)
    title = chapter_titles[file.split('.')[0]]
    outpath = os.path.join('site', title.lower().replace(' ', '-') + '.html')

    print(f'Processing {filepath} -> {outpath}')
    with open(filepath, 'r') as f:
        text = f.read()

    with open(outpath, 'w+') as f:
        f.write(render(VerySimpleTemplate('./tools/template.html'), {'content': md(text), 'title': title}))
