from wpFunc import openai_text,list_to_dict_with_oai, wp_dict_list_html,wp_list_html
with open('keywords.txt','r') as file:
    keywords = [keyword_add.strip().strip('best') for keyword_add in file]

start = 'Write the selection process for wireless earbuds'
nest_dict = {}
for keyword in keywords:
    command = f"{start} {keyword}"
    openai_content = openai_text(command).strip()
    if "\n" in openai_content:
        nest_dict[keyword] = openai_content.strip().split('\n')
        remove_item = ['']
        nest_dict[keyword] = [item for item in nest_dict[keyword] if item not in remove_item]
    else:
        nest_dict[keyword] = openai_content.strip()


single_guide = nest_dict.get(' wireless earbud')
single_guide_instruction_html = wp_list_html(single_guide)

consider_start = 'Things to consider before buying'
consider_intro = {}
list_to_dict_with_oai(consider_start,keywords,consider_intro)
for keyword in keywords:
    consider_intro_html = consider_intro.get(f'{keyword}')
    print(consider_intro_html)