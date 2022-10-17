import os
import re
from collections import Counter
import jieba


path = os.getcwd() + '/file/'
file = os.listdir(path)
r4 = "\【.*?】+|\《.*?》+|\#.*?#+|[.!/_,$&%^*()<>+""'?@|:~{}#]+|[——！\，。=？、：“”‘’￥……()《》【】]"
MOST_COMMON_NUM = 50
total_word = []
cnt_lst = [None for _ in range(20)]
for i, fl in enumerate(file):
    with open(path + fl, "r", encoding='utf-8') as f:
        data = re.sub(r4, '', "".join([s for s in f.read().splitlines(True) if s.strip()]))
        seg_lst = jieba.cut(data.replace('\n', ''))
        cnt_lst[i] = Counter(seg_lst)
        print(cnt_lst[i])
        total_word.extend([x[0] for x in cnt_lst[i].most_common(MOST_COMMON_NUM)])
        f.close()

        
