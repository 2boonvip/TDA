# やってみよう

* まずは PCA を以下のような手順やってみる
  * `compute-pd.py`
  * `vectorize-pd.py`
  * `pca.py`
  * `plot_pca.py`
  * `pca_masks.py`
  * 下のPCAの課題の一つ目をしよう
  
* 次は分類問題
  * 同じデータが使える
  * `classification.py`

* 線形回帰はソースコードの改造が必要
# 課題など

## 総合的課題
* 各種パラメータを変更して試す
  * ベクトル化のパラメータなど
* `data-2` `data-3` などで動かす

## PCA
* 1st PC, 2nd PCなどを表示する
  * `view_vectorized_PD` を用いる
  
    ```
    python3 -m homcloud.view_vectorized_PD --linear-midpoint 0.0 ファイル名 ヒストグラム化情報
    ```
* pca のプロット結果をファイルに保存できるようにする    
* pc1上の正の領域に乗っているbirth-death pairに対応するbirth-pixelを表示する
  
    ```
    homcloud-view-index-pict -d 0 -v data-1-result/pca-pc1-mask-positive.txt -H data-1-pd/histoinfo.json -f "lifetime > 1" -B --no-label data-1/0070.png data-1-pd/0070.idiagram -S 3 -o 0070-pc1-positive.png
    ```

## Classification
* 係数を可視化する
* CV(cross-validation)を使わずにpenaltyの重みいろいろ変えてみる
* l1 penalty項を使う
* PCA同じように「逆」を解く
  * PCAの場合より直感的な意味付けができる
  * point cloudの場合のやりかたは大林に聞いてください
* Support Vector Classifierを使ってみる
* 学習データのラベルをランダムに反転させてみてどうなるか調べる (難)

## linear regression
* ベクトル化までのところを他のソースコードを改造して作る
* areas.txt を追加情報として使ってみる
* CVを使わずにpenaltyの重みを変える
* l1 penalty項を使う
