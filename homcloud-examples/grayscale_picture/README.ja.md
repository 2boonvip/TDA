# この例題について

この例題はグレイスケール画像を閾値を変化させることによる
パーシステンスや関連するデータを計算します。

# 入力データ

input.png

# 例題の動かしかた

    sh run.sh

で以下のファイルが生成されます。

* sublevel.icomplex - 中間データ(sublevel persistence)
* sublevel.idiagram - パーシステンス図のデータ(sublevel persistence)
* sublevel.0.png - 0次のパーシステンス図(sublevel persistence)
* sublevel.1.png - 1次のパーシステンス図(sublevel persistence)
* sublevel.0.txt - 0次のbirth-death pairs(sublevel persistence)
* sublevel.1.txt - 1次のbirth-death pairs(sublevel persistence)
* sublevel.0.birth.png - 0次の birth-death pair で lifetime > 20 であるものの birth/death pixels(sublevel persistence)
* sublevel.1.death.png - 1次の birth-death pair で lifetime > 30 であるものの birth/death pixels(sublevel persistence)

* superlevel.icomplex - 中間データ(superlevel persistence)
* superlevel.idiagram - パーシステンス図のデータ(superlevel persistence)
* superlevel.0.png - 0次のパーシステンス図(superlevel persistence)
* superlevel.1.png - 1次のパーシステンス図(superlevel persistence)
* superlevel.0.txt - 0次のbirth-death pairs(superlevel persistence)
* superlevel.1.txt - 1次のbirth-death pairs(superlevel persistence)
* superlevel.0.birth.png - 0次の birth-death pair で lifetime > 30 であるものの birth/death pixels(superlevel persistence)
* superlevel.1.death.png - 1次の birth-death pair で lifetime > 20 であるものの birth/death pixels(superlevel persistence)

# 各種 GUI の使い方

まず、あらかじめ run.sh を動かして、sublevel.idiagram および superlevel.idiagram
を生成しておいてから、以下のプログラムを動かしてください。

## plot\_PD\_gui (パーシステンス図をインタラクティブに表示)

    sh plot_PD_gui.sh 0 sublevel

0 はホモロジーの次数(0 or 1)
superlevel は閾値を変化させる向き (superlevel or sublevel)

## view_index_pict_gui (birth/death pixel を描画)

    sh view_index_pict_gui.sh 0 sublevel

0 はホモロジーの次数(0 or 1)
superlevel は閾値を変化させる向き (superlevel or sublevel)
