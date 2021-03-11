from bs4 import BeautifulSoup
import bs4
import json

def unit_parser(html):
    soup = BeautifulSoup(html,"html.parser")
    trs = soup.find_all('tr')
    final_content = list()
    element_tag_type = bs4.element.Tag


    for tr in trs:        
        course_dict = dict()
        temp = {
            "course_code" : tr.select_one('[target=_blank]'),
            "td_group" : tr.select_one('td:nth-child(3)'),
            "td_name" : tr.select_one('td:nth-child(4)'),
            "td_vahed" : tr.select_one('td:nth-child(5)'),
            "td_users" : tr.select_one('td:nth-child(6)'),
            "td_capacity" : tr.select_one('td:nth-child(7)'),
            "td_building" : tr.select_one('td:nth-child(8)'),
            "td_sir" : tr.select_one('td:nth-child(9)'),
            "td_reserve" : tr.select_one('td:nth-child(10)'),
            "td_details" : tr.select_one('td:nth-child(11)')
        }
        
        for _ in temp.keys():
            if _ == 'td_details' and type(temp['td_details']) == element_tag_type:
                img = temp['td_details'].find('img')
                img_atr_list = img.get_attribute_list('title')
                img_attr = img_atr_list[0].split('body=[')
                for_parse = img_attr[2].replace(']','')
                pars_detail = BeautifulSoup(for_parse,"html.parser")
                details_list = pars_detail.prettify().splitlines()
                
                if len(details_list) == 34:
                    course_dict[_] =  {
                        'sharhe_dars' : details_list[3],
                        'maqta' : details_list[8],
                        'gorohe amoozeshi' : details_list[13],
                        'jalase_one' : details_list[18],
                        'jalase_two' : details_list[23],
                        'emtehan' : details_list[28],
                        'for' : details_list[33]
                    }

            elif type(temp[_]) == element_tag_type:
                course_dict[_] = temp[_].text

        if len(course_dict) > 0:
            final_content.append(course_dict)
    return json.dumps(final_content)
