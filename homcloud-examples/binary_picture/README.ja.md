# この例題について

この例題は2値画像から「太らせる/痩せさせる」ことによる
パーシステンスや関連するデータを計算します。

# 入力データ

input.png

# 例題の動かしかた

    sh run.sh

で以下のファイルが生成されます。

* input.icomplex - 中間データ
* output.idiagram - パーシステンス図のデータ
* output.0.png - 0次のパーシステンス図
* output.1.png - 1次のパーシステンス図
* output.0.txt - 0次の birth-death pairs
* output.1.txt - 1次の birth-death pairs
* output.death.0.png - 0次の birth-death pair で (-5, -4) に対応するものの death pixels
* output.birth.1.png - 1次の birth-death pair で (6, 7) に対応するものの birth pixels


# 各種 GUI の使い方

まず、あらかじめ run.sh を動かして、output.idiagram を生成しておいてから、以下の
プログラムを動かしてください。

## plot\_PD\_gui (パーシステンス図をインタラクティブに表示)

    sh plot_PD_gui.sh 0

0 はホモロジーの次数(0 or 1)

## view_index_pict_gui (birth/death pixel を描画)

    sh view_index_pict_gui.sh 0

0 は上と同じでホモロジーの次数(0 or 1)
