# この例題について

この例題はポイントクラウドデータに対する
パーシステンス図や関連するデータを計算します。

# 入力データ

input.txt

5000個のデータ点

# 例題の動かしかた

    sh run.sh

で以下のファイルが生成されます。

* input.icomplex - 中間データ
* output.idiagram - パーシステンス図のデータ
* output.1.png - 1次のパーシステンス図
* output.1.txt - 1次の birth-death pairs
* output.2.png - 2次のパーシステンス図
* output.2.txt - 2次の birth-death pairs

# 各種 GUI の使い方

まず、あらかじめ run.sh を動かして、output.idiagram
を生成しておいてから、以下のプログラムを動かしてください。

## plot\_PD\_gui (パーシステンス図をインタラクティブに表示)

    sh plot_PD_gui.sh 1

1 はホモロジーの次数(0 or 1 or 2)
