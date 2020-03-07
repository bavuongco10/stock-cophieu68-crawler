#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 13:22:13 2020

@author: user
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 14:03:06 2020

@author: user
"""

import requests
from datetime import datetime

cookies = {
    'PHPSESSID': 'l12f51q61tgjic3i1u07neou81',
    'cophieu68username': 'cGhhdGRhdDIxMkBnbWFpbC5jb20%3D',
    'cophieu68password': 'YjUzYWQ1MTI4YmExZDAzNTY1NzdjODBjOGZjYWZkYTA%3D',
}

headers = {
    'Connection': 'keep-alive',
    'DNT': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
}


def get_stock_lastest(id):
  params = (
      ('id', id),
  )

  response = requests.get('https://www.cophieu68.vn/export/metastock.php', headers=headers, params=params, cookies=cookies)

  stock_data = response.content.decode('utf-8')

  stock_matrix = [line.split(',') for line in stock_data.split('\r\n')]

  now  = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)



  stock_matrix_cols = [col.replace('<', '').replace('>', '') for col in stock_matrix[0]]
  stock_matrix_rows = stock_matrix[1:]

  unprocessed_stocks = [stock_matrix_cols]

  for i in range(len(stock_matrix_rows)):
    print(now)
    print(datetime.strptime(stock_matrix_rows[i][1], '%Y%m%d'))
    if(datetime.strptime(stock_matrix_rows[i][1], '%Y%m%d') < now):
      break;
    else:
      unprocessed_stocks.append(stock_matrix_rows[i])

  return unprocessed_stocks


print(get_stock_lastest('AAM'))



