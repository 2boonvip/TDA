# 入力データ

`picts/` ディレクトリにある画像100枚と `labels.txt` (これはpcaの結果を表示するための赤青の色分けのために使います)です。

# 例の動かしかた

まず、PDを計算してベクトル化します。

    sh compute-pd-vectorize-pd.sh

すると、`diagrams/` 以下にPD(拡張子`.idiagram`)が生成され、
`vects/`以下にPIでベクトル化したPD(拡張子`.txt`)が生成されます。

つぎに PCA を計算します。

    python3 pca.py
    
すると `mean.txt`、`pc1.txt`、`pc2.txt` (それぞれ、平均、1st principal component、2nd principal componentです)
が生成されます。また、実行時に表示されるのは寄与率です。また、入力データを2次元に落とした
データ(`pca.txt`)も生成されます。

`pca.txt` は以下のコマンドで可視化できます。

    python3 plot_pca.py
    
`labels.txt` の 0-1 情報はここでの色付けで使われます。

また、principal componentをPDの形で可視化するには以下のコマンドでOKです。

    sh show_pc.sh mean.txt # 平均成分を表示
    sh show_pc.sh pc1.txt # 1st PCを表示
    sh show_pc.sh pc2.txt # 2nd PCを表示
    




