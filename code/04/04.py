from llm_utils import ChatTemplate

response = ChatTemplate.from_file('rewrite.json').completion({
    'sample': '''
Deep in the shady sadness of a vale
Far sunken from the healthy breath of morn,
Far from the fiery noon, and eve's one star,
Sat gray-hair'd Saturn, quiet as a stone,
Still as the silence round about his lair;
Forest on forest hung about his head
Like cloud on cloud. No stir of air was there,
Not so much life as on a summer's day
Robs not one light seed from the feather'd grass,
But where the dead leaf fell, there did it rest.
A stream went voiceless by, still deadened more
By reason of his fallen divinity
Spreading a shade: the Naiad 'mid her reeds
Press'd her cold finger closer to her lips.''',
    'text': "Let's start with an example: a large language model trained \
on a wide range of texts can perform a translation task from one language to \
another without ever having been explicitly trained on that particular \
translation pair. The model can be given a prompt in the source language, \
along with a description of the target language, and it will generate a \
translation based on its understanding of language."})

print(response.choices[0].message.content)
