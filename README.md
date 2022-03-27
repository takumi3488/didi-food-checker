# DiDi Food Checker

DiDi Foodの店舗が「受付時間外」でなくなったら、自動でブラウザで店舗ページを開きます。

## 使い方

`url.txt`を作成して、チェックしたい店舗のURLを貼り付けてください。

`main.py`の`driver = webdriver.Safari()`の箇所を、使いたいブラウザによって変更してください。例えば`driver = webdriver.Chrome()`のようになります。

その後`python3 main.py`を実行します。
