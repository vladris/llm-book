import os
import shutil
from baku.markdown import make_markdown_processor
from baku.templating import render, VerySimpleTemplate


# Clean up the site directory
print('Cleaning up site directory')
for file in os.listdir('site'):
    if file.endswith('.html'):
        os.remove(os.path.join('site', file))

print('Removing images')
shutil.rmtree('site/images', ignore_errors=True)

# Chapter title mappings
chapter_titles = {
    'index': 'Front Cover',
    'toc': 'Table of Contents',
    '01': 'A New Paradigm',
    '02': 'Large Language Models',
    '03': 'Prompt Engineering',
    '04': 'Learning and Tuning',
    '05': 'Memory and Embeddings',
}

# Chapter prefix mappings
chapter_prefixes = {
    'index': '',
    'toc': '',
    '01': 'Chapter 1: ',
    '02': 'Chapter 2: ',
    '03': 'Chapter 3: ',
    '04': 'Chapter 4: ',
    '05': 'Chapter 5: ',
}

# Render markdown files
md = make_markdown_processor()
for file in os.listdir('text'):
    if not file.endswith('.md'):
        continue

    filepath = os.path.join('text', file)
    index = file.split('.')[0]
    title, prefix = chapter_titles[index], chapter_prefixes[index]
    
    if index != 'index':
        outpath = os.path.join('site', title.lower().replace(' ', '-') + '.html')
    else:
        outpath = os.path.join('site', 'index.html')

    print(f'Processing {filepath} -> {outpath}')
    with open(filepath, 'r') as f:
        text = f.read()

    with open(outpath, 'w+') as f:
        f.write(render(VerySimpleTemplate('./tools/template.html'), {'content': md(text), 'prefix': prefix, 'title': title}))


# Copy the directory tree
print('Copying images')
shutil.copytree('text/images', 'site/images')

print('Done')
