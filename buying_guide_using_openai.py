import requests
import os
from dotenv import load_dotenv
load_dotenv()
from wpFunc import list_to_dict_with_oai, wp_h2, wp_paragraph,wp_list_html, wp_headers,list_to_wp_para
with open('keywords.txt','r') as file:
    keyword_list = [input_keyword.strip().strip('best').strip() for input_keyword in file]


kw_start = 'Write 120 words about'
guide_intro_dict = {}
intro_text = list_to_dict_with_oai(kw_start,keyword_list,guide_intro_dict)

select_start = 'Write 250 words description about'
guide_desc = {}
list_to_dict_with_oai(select_start,keyword_list,guide_desc)


consider_start = 'Things to consider before buying'
consider_intro = {}
list_to_dict_with_oai(consider_start,keyword_list,consider_intro)

start_conclusion = 'Write 200 words buying guide conclusion about'
conclusion_dict = {}
list_to_dict_with_oai(start_conclusion,keyword_list,conclusion_dict)

user = 'shahin'
password = '88a6 VLB2 A0zb L5nd PSno 9nTb'

wp_head = wp_headers(user, password)

wp_post_end = 'https://shahin.local/wp-json/wp/v2/posts'

for input_keyword in keyword_list:
    title = f"Top 10 Best {input_keyword} - Buying Guide"
    single_intro = guide_intro_dict.get(f'{input_keyword}')
    single_intro_html = wp_paragraph(single_intro)
    description_heading = f'Details about {input_keyword}'
    description_heading_html = wp_h2(description_heading)
    single_desc = guide_desc.get(f'{input_keyword}')
    single_desc_html = list_to_wp_para(single_desc)
    consider_heading = f'Things to Consider Before Buying {input_keyword.title()}'
    consider_heading_html = wp_h2(consider_heading)
    single_consider = consider_intro.get(f'{input_keyword}')
    single_consider_html = wp_list_html(single_consider)
    conclusion_html = wp_h2('Conclusion')
    single_conclusion = conclusion_dict.get(f'{input_keyword}')
    single_conclusion_html = list_to_wp_para(single_conclusion)
    content = f'{single_intro_html}{description_heading_html}{single_desc_html}{consider_heading_html}{single_consider_html}{conclusion_html}{single_conclusion_html}'
    slug = f"best {input_keyword} buying guide"
    data = {
        'title': title.title().strip(),
        'content': content,
        'slug': slug.strip().lower().replace(' ','-').replace('--','-')
    }
    resp = requests.post(wp_post_end, data=data, headers=wp_head, verify=False)
    print(resp.status_code)

