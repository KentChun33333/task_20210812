import nltk
import string
import pandas as pd


class BslNameMatcher():
    def __init__(self, replace_dict={}):
        self.tokenizer = nltk.RegexpTokenizer(r"\w+")
        self.replace_dict = replace_dict

    def run(self, input_txt):
        name = input_txt.lower()
        new_words = self.tokenizer.tokenize(name)
        # prior knowledge filtering & sorting
        for i in range(len(new_words)):
            if new_words[i] in self.replace_dict.keys():
                new_words[i] = self.replace_dict[new_words[i]]

        new_words = [i for i in new_words if i != '']
        return ' '.join(new_words)


class AdNameMatcher():
    def __init__(self, replace_dict={}):
        self.replace_dict = replace_dict

    def _handle_brackets_abbre(self, x: str):
        if '(' in x:
            s_ind = x.find('(')
            e_ind = x.find(')')
            x = x[:s_ind+2] + x[e_ind:]
        return x

    def _handle_and_abbre(self, x: str):
        tar_patt, sub_patt = ' & ', '&'
        if tar_patt in x:
            x = x.replace(tar_patt, sub_patt)
            x_list = x.split()
            for ind in range(len(x_list)):
                if '&' in x_list[ind]:
                    e_word = x.split(sub_patt)[-1][0]
                    x_list[ind] = x_list[ind][0] + sub_patt + e_word
            x = ' '.join(x_list)
        return x

    def run(self, input_txt):
        name = input_txt.lower()
        # handel special abbreviation pattern
        name = self._handle_brackets_abbre(name)
        name = self._handle_and_abbre(name)
        # remove punctuation
        name.translate(str.maketrans('', '', string.punctuation))
        new_words = name.split()

        # prior knowledge filtering & sorting
        for i in range(len(new_words)):
            if new_words[i] in self.replace_dict.keys():
                new_words[i] = self.replace_dict[new_words[i]]
        new_words.sort()
        new_words = [i for i in new_words if i != '']
        return ' '.join(new_words)


def main_anas(input_list: list, test_func) -> dict:

    res = None
    for list_item in input_list:
        item_res = [test_func(i) for i in list_item]
        item_res = {k: [v] for k, v in zip(item_res, list_item)}
        if res is None:
            res = item_res
        else:
            for k, v in item_res.items():
                if k in res.keys():
                    res[k].extend(item_res[k])
            else:
                res[k] = item_res[k]
    return res


def test_bsl(input_list):
    replace_dict = {'holdings': '', 'pt': '', 'limited': 'ltd'}
    agent = BslNameMatcher(replace_dict)
    res = main_anas(input_list, agent.run)
    df = pd.DataFrame()
    df['Key'] = res.keys()
    df['Value'] = res.values()
    df.to_csv('basic_output.csv', index=False)


def test_ad(input_list):
    replace_dict = {'holdings': '', 'pt': '', 'limited': 'ltd'}
    agent = AdNameMatcher(replace_dict)
    res = main_anas(input_list, agent.run)
    df = pd.DataFrame()
    df['Key'] = res.keys()
    df['Value'] = res.values()
    df.to_csv('advance_output.csv', index=False)


if __name__ == '__main__':

    table_A = ['3 MOBILE TELECOM PTE. LTD.',
               'A. MENARINI ASIA-PACIFIC PTE. LTD.',
               'A. MENARINI ASIA-PACIFIC HOLDINGS PTE. LTD.',
               'ADEKA (SINGAPORE) PTE. LTD.',
               'ADM ASIA-PACIFIC TRADING PTE. LTD.',
               'ARROW ELECTRONICS ASIA (S) PTE. LTD.',
               'DELFI LIMITED',
               'FOOD EMPIRE HOLDINGS LTD.',
               'HANWELL HOLDINGS LIMITED',
               'HEMPEL (SINGAPORE) PTE. LTD.',
               'HEWLETT-PACKARD ASIA PACIFIC PTE. LTD.',
               'HOSEN GROUP LIMITED',
               'MSC MACHINERY COMPANY LIMITED',
               'C & C MACHINERY LIMITED',
               'JC MACHINERY SDN. BHD.',
               'PT. Bhumyamca Sekawan',
               'PT PURA BARUTAMA',
               'Chanua E&C Pte Ltd',
               'Chanua(Singapore) Pte Ltd',
               'Chanua(2000) Pte Ltd',
               'Chanua 2001 Pte Ltd',
               ]
    table_B = ['3 MOBILE TELECOM PTE. LTD.',
               'A. MENARINI SINGAPORE PTE. LTD.',
               'ADIDAS SINGAPORE PTE LTD',
               'ADM ASIA-PACIFIC TRADING PTE. LTD.',
               '1/ARROW ELECTRONICS (S) PTE LTD',
               'DELFI LTD.',
               'FOOD EMPIRE HOLDINGS LIMITED',
               'HANWELL HOLDINGS LTD.',
               'HERMES SINGAPORE (RETAIL) PTE LTD',
               'HEWLETT-PACKARD SINGAPORE (SALES) PTE. LTD.',
               'HOSEN GROUP LTD.',
               'BHUMYAMCA SEKAWAN,PT',
               'PT. GUDANG GARAM TBK.',
               'Chanua Engineering & Construction Pte ltd',
               'Chanua(S) Pte Ltd',
               'Chanua 2000 Pte Ltd',
               'C.N. MACHINERY SDN BHD',
               'DM MACHINERY SDN. BHD.',
               'JAY MACHINERY PTE LTD',
               ]

    input_list = [table_A, table_B]
    test_bsl(input_list)
    test_ad(input_list)
