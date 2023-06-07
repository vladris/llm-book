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
    'preface': 'Preface',
    '01': 'A New Paradigm',
    '02': 'Large Language Models',
    '03': 'Prompt Engineering',
    '04': 'Learning and Tuning',
    '05': 'Memory and Embeddings',
}

# Chapter heading mappings
chapter_headings = {
    'index': '%s ~ Large Language Models at Work',
    'toc': '%s ~ Large Language Models at Work',
    'preface': '%s ~ Large Language Models at Work',
    '01': 'Chapter 1: %s',
    '02': 'Chapter 2: %s',
    '03': 'Chapter 3: %s',
    '04': 'Chapter 4: %s',
    '05': 'Chapter 5: %s',
}

# Chapter order
chapters = ['index', 'toc', 'preface', '01', '02', '03']

# Get chapter outpath
def get_chapter_outpath(index):
    if index == 'index':
        return 'index.html'
    else:
        title = chapter_titles[index]
        return title.lower().replace(' ', '-') + '.html'

# Render markdown files
md = make_markdown_processor()
for file in os.listdir('text'):
    if not file.endswith('.md'):
        continue

    filepath = os.path.join('text', file)
    index = file.split('.')[0]
    title = chapter_titles[index]
    heading = chapter_headings[index] % (title)
    outpath = os.path.join('site', get_chapter_outpath(index))

    # Link to previous and next chapters
    i = chapters.index(index)
    prev_title, prev_link = None, None
    if i != 0:
        prev_title, prev_link = chapter_titles[chapters[i - 1]],  get_chapter_outpath(chapters[i - 1])
    next_title, next_link = None, None
    if i != len(chapters) - 1:
        next_title, next_link = chapter_titles[chapters[i + 1]], get_chapter_outpath(chapters[i + 1])

    print(f'Processing {filepath} -> {outpath}')
    with open(filepath, 'r') as f:
        text = f.read()

    with open(outpath, 'w+') as f:
        f.write(render(VerySimpleTemplate('./tools/template.html'), {
            'content': md(text),
            'title': title,
            'heading': heading,
            'prev_title': prev_title,
            'prev_link': prev_link,
            'next_title': next_title,
            'next_link': next_link,}))


# Copy the directory tree
print('Copying images')
shutil.copytree('text/images', 'site/images')

print('Done')
