Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> { (x + y) for x in [1,2,3] for y in [12,2,3] }
{3, 4, 5, 6, 13, 14, 15}
>>> { (x + y) for x in [1,2,3] for y in [1,2,3] }
{2, 3, 4, 5, 6}
>>> {"h"+str(x):x*5 for x in range(1,4)}
{'h1': 5, 'h2': 10, 'h3': 15}
>>> # ジェネレーター式でジェネレーターを生成
>>> ( x** 2 for x in [1, 2, 3] )
<generator object <genexpr> at 0x0000023079273850>
