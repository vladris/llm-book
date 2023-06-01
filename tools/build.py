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

# Chapter prefix mappings
chapter_prefixes = {
    '01': 'Chapter 1',
    '02': 'Chapter 2',
    '03': 'Chapter 3',
    '04': 'Chapter 4',
    '05': 'Chapter 5',
}

# Render markdown files
md = make_markdown_processor()
for file in os.listdir('text'):
    if not file.endswith('.md'):
        continue

    filepath = os.path.join('text', file)
    index = file.split('.')[0]
    title, prefix = chapter_titles[index], chapter_prefixes[index]
    outpath = os.path.join('site', title.lower().replace(' ', '-') + '.html')

    print(f'Processing {filepath} -> {outpath}')
    with open(filepath, 'r') as f:
        text = f.read()

    with open(outpath, 'w+') as f:
        f.write(render(VerySimpleTemplate('./tools/template.html'), {'content': md(text), 'prefix': prefix, 'title': title}))
