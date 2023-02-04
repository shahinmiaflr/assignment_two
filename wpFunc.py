
def wp_list_html(any_list):
    start = '<!-- wp:list --><ul>'
    for element in any_list:
        start += f'<!-- wp:list-item --><li>{element}</li><!-- /wp:list-item -->'
    end = '</ul><!-- /wp:list -->'
    code = start + end
    return code

def wp_dict_list_html(dicts):
    start = '<!-- wp:list --><ul>'
    for key, value in dicts.items():
        start += f'<!-- wp:list-item --><li><strong>{key.title()}</strong>: {value.title()}</li><!-- /wp:list-item -->'
    end = '</ul><!-- /wp:list -->'
    code = start + end
    return code
def wp_headers(username,password):

    import base64
    credentials = f'{username}:{password}'
    token = base64.b64encode(credentials.encode())
    headers = {'Authorization': f'Basic {token.decode("utf-8")}'}
    return headers

def wp_image_url(src,name):
    first_line = '<!-- wp:image {"align":"center","sizeSlug":"large"} -->'
    second_line = f'<figure class="wp-block-image aligncenter size-large"><img src="{src}" alt="{name} image"/>'
    last_line = f'<figcaption class="wp-element-caption">{name}</figcaption></figure><!-- /wp:image -->'
    code = f'{first_line}{second_line}{last_line}'
    return code
def wp_h2(text):
    heading = f'<!-- wp:heading --><h2>{text}</h2><!-- /wp:heading -->'
    return heading

def wp_h3(text):
    heading = f'<!-- wp:heading {{"level":3}} --><h3>{text}</h3><!-- /wp:heading -->'
    return heading


def wp_paragraph(text):
    code = f'<!-- wp:paragraph --><p>{text}</p><!-- /wp:paragraph -->'
    return code

def dict_to_wp_para(dict):
    code =''
    for key, value in dict.items():
        code += f'<!-- wp:paragraph --><p>{value}</p><!-- /wp:paragraph -->'
    return code

def list_to_wp_para(list_info):
    code = ''
    for info in list_info:
        code += f'<!-- wp:paragraph --><p>{info}</p><!-- /wp:paragraph -->'
    return code

def openai_text(prompt):
    import os
    from dotenv import load_dotenv
    load_dotenv()
    import openai
    openai.api_key = os.getenv("API_KEY")
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    data = response.get('choices')[0].get('text').strip()
    return data
def list_to_dict_with_oai(srat,keyword_list,dict_name):
    '''
    function will take command for open ai and will return dictonary with opanai content
    :param srat: instruction for openai
    :param keyword_list: it will take keyword in list format
    :param dict_name: return value to this dictonary
    :return: dictonary
    '''

    for keyword in keyword_list:
        command = f"{srat} {keyword}"
        ai_answer = openai_text(command).strip()
        if "\n" in ai_answer:
            dict_name[keyword] = ai_answer.strip().split('\n')
            remove_item = ['']
            dict_name[keyword] = [item for item in dict_name[keyword] if item not in remove_item]
        else:
            dict_name[keyword] = ai_answer.strip()