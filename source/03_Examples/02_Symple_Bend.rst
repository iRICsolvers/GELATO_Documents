========================================
[計算例 2] 単純な湾曲水路の浮遊物追跡
========================================

:numref:`02_jikken` に示すような直線+湾曲+直線水路実験の流量解析およびトレーサーの追跡計算を行う。
この実験は水路全幅約1.8mで、左岸側半分が高水敷、右岸側半分が低水路の複断面水路で、右岸側のみが
移動床となっている。平面形状および断面形状の概略を :numref:`02_heimen` に示す。
この実験は `寒地土木研究所 <https://www.ceri.go.jp/>`_ の委託により。
`(株)建設技術研究所 <http://www.ctie.co.jp/>`_ によって行われたものである。


.. _02_jikken:

.. figure:: images/02/jikken.gif
   :width: 400pt

   : 実験状況の動画

.. _02_heimen:

.. figure:: images/02/heimen.png
   :width: 450pt

   : 実験水路の形状

以下の計算事例では以下の手順で計算を実施する。

(1) Nays2DHにより河床変動計算を実施し、河床変動がほぼ定常に達すた状態の河床形状を得る。
(2) Nays2d+により準3次元流れ場の計算をする。
(3) GELATOによりトレーサーの追跡を行う。乱流拡散強度パラーメーターを変更してその影響を比較する。


Nays2DHによる流れと河床変動の計算
===================================

ソルバの選択
---------------

iRICの起動画面から、[新しいプロジェクト]を選ぶと表示されるソルバの選択画面で、
[Nays2DH]を選んで[OK]ボタン押すと、

.. figure:: images/01/Select_Nays2dh.png
   :width: 600pt

   : ソルバーの選択

「無題- iRIC 4.x.x.xxxx [Nays2DH iRIC3X 1.0 64bit]」と書かれた
Windowが現れる。

.. _02_mudai:

.. figure:: images/01/mudai.png 
   :width: 100%

   : 無題


計算格子の作成
--------------

[格子]->[格子生成アルゴリズムの選択]で現れるウィンドウで、
[2次元単純円弧格子作成ツール(複断面対応版)]を選んで[OK]を押す。
(:numref:`02_koshi1` )

.. _02_koshi1:

.. figure:: images/02/koshi1.png 
   :width: 600pt

   : 格子生成アルゴリズムの選択

[格子生成]のグループ[水路形状]、[断面形状]、[追加水路]、[粗度と河床状態]を
それぞれ、
:numref:`02_koshi2` 、
:numref:`02_koshi3` ,
:numref:`02_koshi4` ,
:numref:`02_koshi5` 
のようにパラメータを設定して、最後に[格子生成]を押す。

.. _02_koshi2:

.. figure:: images/02/koshi2.png
   :width: 400pt

   : 格子生成(1)

.. _02_koshi3:

.. figure:: images/02/koshi3.png
   :width: 400pt

   : 格子生成(2)  

.. _02_koshi4:

.. figure:: images/02/koshi4.png 
   :width: 400pt

   : 格子生成(3)

.. _02_koshi5:

.. figure:: images/02/koshi5.png
   :width: 400pt

   : 格子生成(4)

「マッピングを実行しますか？」と聞かれるので[はい(Y)]を押す。
( :numref:`02_mapping` )

.. _02_mapping:

.. figure:: images/02/mapping.png
   :width: 300pt

   : 確認

オブジェクトブラウザーの[格子][セルの属性][固定床と移動床]に☑マークを入れると、
:numref:`02_koshi6` のように固定床部分が赤、移動床部分が青で示された
格子の図が示される。

.. _02_koshi6:

.. figure:: images/02/koshi6.png
   :width: 100%

   : 固定床と移動床

低水路と高水敷の境界の固定床は護岸を想定しているが、本実験での護岸は湾曲部を含むその上下流のみ
なので、:numref:`02_koshi7` に示すように[固定床と移動床]をフォーカスして、
直線部の護岸部分(この例では格子番号101より上流の赤色の格子部分)を選んで右クリックして、
属性を[移動床]に変更すし、[OK]を押す。

.. _02_koshi7:

.. figure:: images/02/koshi7.png
   :width: 100%

   : 固定床と移動床の属性変更

また下流端は固定床なので、:numref:`02_koshi8` に示すように拡大、回転して
最下流の格子属性を[固定床]に変更する。

.. _02_koshi8:

.. figure:: images/02/koshi8.png
   :width: 100%

   : 最下流端の格子を固定床に変更

計算条件の設定
----------------

メインメニューから[計算条件]->[設定]で現れる[計算条件]ウィンドウの、
[グループ]において、
[ソルバー・タイプ]、[境界条件]、[時間]、[河床材料]を
それぞれ、
:numref:`02_joken1` 、
:numref:`02_joken2` ,
:numref:`02_joken3` ,
:numref:`02_joken4` 
のようにパラメータを設定する。

.. _02_joken1:

.. figure:: images/02/joken1.png
   :width: 600pt

   : 計算条件(ソルバー・タイプ)

.. _02_joken2:

.. figure:: images/02/joken2.png
   :width: 600pt

   : 計算条件(境界条件)

.. _02_joken3:

.. figure:: images/02/joken3.png
   :width: 600pt

   : 計算条件(時間)

.. _02_joken4:

.. figure:: images/02/joken4.png
   :width: 600pt

   : 計算条件(河床材料)


なお。:numref:`02_joken2` の[境界条件]においては、
[上流端流量と下流端水位の時間変化]で[Edit]を押して現れる、
:numref:`02_joken5` の[流量時間変化設定ウィンドウ]で時間と流量の関係を与える。

.. _02_joken5:

.. figure:: images/02/joken5.png
   :width: 600pt

   : 計算条件(流量の時間配分の設定)

計算条件の設定が終了したら、[計算条件]ウィンドウで[OK]を押す。

計算の実行
--------------

計算を実行する前に、メインメニューから[ファイル]->[名前を付けてポロジェクトに保存]を選択して、
新しいフォルダを作成し、そのフォルダを選択することによりプロジェクトを保存しておく。
ここでは、[Nays2DH_flow_bed]という名前で保存する。( :numref:`02_save_project` )

.. _02_save_project:

.. figure:: images/02/save_project.png
   :width: 600pt

   : 計算プロジェクトの保存

メインメニューから[計算]->[実行]を選択すると、今保存したばかりなのにしつこく[保存しますか？]
と聞かれるので(:numref:`02_jikko1` ) [はい]を選ぶと計算が開始される。(:numref:`02_jikko2` ) 

.. _02_jikko1:

.. figure:: images/02/jikko1.png
   :width: 400pt

   : 「保存しますか？」

.. _02_jikko2:

.. figure:: images/02/jikko2.png
   :width: 100%

   : 「計算実行中」
 
計算が終了したら、メインメニューから[計算結果]->[保存]を選択して計算結果を保存しておく。

計算結果の表示
----------------

オブジェクトブラウザーから[iRICZone]->[スカラー]->[ElevationChange(m)]に☑マークを付け、
[ElevationChange(m)]を右クリックして[プロパティ]を選択して、[スカラー設定]を
:numref:`02_hyoji1` のように設定する。

.. _02_hyoji1:

.. figure:: images/02/hyoji1.png
   :width: 600pt

   : 「スカラー設定」

オブジェクトブラウザーから[ベクトル]->[Velocity(ms-1)]に☑マークを付け、
[ベクトル]を右クリックして[プロパティ]を選択して、[ベクトル設定]を
:numref:`02_hyoji2` のように設定する。

.. _02_hyoji2:

.. figure:: images/02/hyoji2.png
   :width: 600pt

   : 「ベクトル設定」

メインメニューに[タイムスケールバー]をゼロに戻し、[アニメーション]->[開始/停止]を選択する
( :numref:`02_hyoji3` )

.. _02_hyoji3:

.. figure:: images/02/hyoji3.png
   :width: 100%

   : 「アニメーションの実行」

:numref:`02_hyoji4` のようにアニメーションが表示され、河床変動がほぼ定常に達していることが分かる。

.. _02_hyoji4:

.. figure:: images/02/hyoji4.gif
   :width: 70%

   : 「河床変動と流速ベクトルのアニメーション」

計算結果のエクスポート
---------------------------

計算で得られた河床形状を次節で行うNays2d+による準3次元流れの計算の境界条件に使用するために
計算結果をテキストファイルにエクスポートする。:numref:`02_export` に示すように、メインメニューから、
[ファイル]->[エクスポート]->[計算結果]を選ぶ.


.. _02_export:

.. figure:: images/02/export.png
   :width: 100%

   : 「計算結果のエクスポート(1)」

[計算結果のエクスポート]ウィンドウ( :numref:`02_export` )が表示されるので、
[形式]を[地勢データファイル形式(tpo)]に設定する( :numref:`02_export2` )。

.. _02_export2:

.. figure:: images/02/export2.png
   :width: 250pt

   : 「計算結果のエクスポート(2)」


出力フォルダは任意の名前で、
[全タイムステップ]の前にあるチェックボックスの☑を外し、[開始][終了]を10,800に設定して、[OK]をクリックすると、計算結果のエクスポートが完了する( :numref:`02_export3` )。

.. _02_export3:

.. figure:: images/02/export3.png
   :width: 250pt

   : 「計算結果のエクスポート(3)」

エクスポートされた計算結果は、( :numref:`02_export4` )に示すように、水深、流速、流砂量、河床高。。。。
など種類別に様々なファイルに保存されているが、このうち次節の計算に使用するのは河床高のみであるので、
[Results_1_Elevation(m).tpo]という名前のファイル以外は不要なので消しても構わない。

.. _02_export4:

.. figure:: images/02/export4.png
   :width: 600pt

   : 「計算結果のエクスポート(3)」

Nays2d+による準3次元流れの計算
===================================

ソルバの選択
---------------

iRICの起動画面から、[新しいプロジェクト]を選ぶと表示されるソルバの選択画面
( :numref:`02_select2` )で[Nays2d+簡単に3次元の流れの計算が出来ます]
を選択して[OK]を押す。

.. _02_select2:

.. figure:: images/02/select2.png
   :width: 600pt

   : 「ソルバーNays2d+の選択」

計算格子と河床形状のインポートとマッピング
--------------------------------------------

格子のインポート
^^^^^^^^^^^^^^^^^

メインメニューから[インポート]->[格子]を選択し、前記のNays2DHのプロジェクトフォルダー
[Nays2DH_flow_bed]の中の[Case1.cgn]を選ぶ。
:numref:`02_koshi10` のような警告が出るが、「余計なお世話です」と心の中で思いながら、
構わず[はい]をクリックすると、格子のインポートが完了する。
( :numref:`02_koshi11` )

.. _02_koshi10:

.. figure:: images/02/koshi10.png
   :width: 400pt

   : 「警告」

.. _02_koshi11:

.. figure:: images/02/koshi11.png
   :width: 100%

   : 「格子のインポート完了」

河床高のインポート
^^^^^^^^^^^^^^^^^^^^

メインメニューから[インポート]->[地理情報]->[河床高]を選択する( :numref:`02_import2` ).

.. _02_import2:

.. figure:: images/02/import2.png
   :width: 100%

   : 「河床高のインポート」

インポートファイルの選択画面が現れる(:numref:`02_import3` )ので、前節のNays2dHの計算結果として
エクスポートした [Results_1_Elevation(m).tpo]を選択して[開く]。

.. _02_import3:

.. figure:: images/02/import3.png
   :width: 600pt

   : 「河床高のインポート(ファイルの選択)」

:numref:`02_import4` のようにデータを間引くかどうか来かれるが、特に間引く必要がなければ、そのまま
[OK]を押すと[河床高]のインポートが完了する( :numref:`02_import5` )

.. _02_import4:

.. figure:: images/02/import4.png
   :width: 400pt

   : 「河床高のインポート(間引き設定)」



.. _02_import5:

.. figure:: images/02/import5.png
   :width: 100%

   : 「河床高のインポート完了」

マッピング
^^^^^^^^^^^^^^^

インポートした河床高データをインポートした格子上にマッピングを行う。

:numref:`02_mapping2` のように[格子]->[属性のマッピング]->[実行]を選ぶ。 

.. _02_mapping2:

.. figure:: images/02/mapping2.png
   :width: 100%

   : 「マッピング」

:numref:`02_mapping3` マッピングする[地理情報]を聞かれるので、
[河床高(m)]に☑を入れて[OK]をクリックすると 

.. _02_mapping3:

.. figure:: images/02/mapping3.png
   :width: 200pt

   : 「マッピングする情報の選択」

マッピングが完了する( :numref:`02_mapping4` )ので、[OK]をクリックして
完了。

.. _02_mapping4:

.. figure:: images/02/mapping4.png
   :width: 200pt

   : 「マッピングの完了」


Nays2d＋の計算条件の設定
-----------------------------

メインメニューから[計算条件]->[設定]で現れる[計算条件]ウィンドウの、
[グループ]において、
[流量および下流端水位の設定]、[時間および浸食に関するパラメータパラメータ]、
[境界条件]、[他の計算条件]、[３次元流速分布]を
それぞれ、
:numref:`02_joken6` 、
:numref:`02_joken7` ,
:numref:`02_joken8` ,
:numref:`02_joken9` ,
:numref:`02_joken10` 
のようにパラメータを設定する。

.. _02_joken6:

.. figure:: images/02/joken6.png
   :width: 600pt

   : 計算条件(流量および下流端水位の設定)

.. _02_joken7:

.. figure:: images/02/joken7.png
   :width: 600pt

   : 計算条件(時間および浸食に関するパラメーター)

.. _02_joken8:

.. figure:: images/02/joken8.png
   :width: 600pt

   : 計算条件(境界条件)

.. _02_joken9:

.. figure:: images/02/joken9.png
   :width: 600pt

   : 計算条件(他の計算条件)

.. _02_joken10:

.. figure:: images/02/joken10.png
   :width: 600pt

   : 計算条件(3次元流速分布)


なお。:numref:`02_joken6` の[流量および下流端水位の設定]においては、
[流量と下流端水位の時系列]の隣の[Edit]を押して現れる、
:numref:`02_joken11` の[流量時間変化設定ウィンドウ]で時間と流量の関係を与える。

.. _02_joken11:

.. figure:: images/02/joken11.png
   :width: 600pt

   : 計算条件(流量の時間配分の設定)

計算条件の設定が終了したら、[計算条件]ウィンドウで[OK]を押す。

Nays2d+の計算の実行
--------------------------

計算の実行方法は前節[Nays2DHによる計算の実行]と全く同じで、タダでさえ長いのに
これ以上同じことをクドクド書くと嫌われそうなので省略する。
ただ、計算の実行の前に、必ず、プロジェクトを保存しておくことを推奨する。
ここでは、[Nays2d+Flow]とう名前のプロジェクトに保存する。

.. _02_save_project2:

.. figure:: images/02/save_project2.png
   :width: 600pt

   : プロジェクトの保存(Nays2d+Flow)

計算結果は[Case1.cgn]というCGNSファイルに保存されるが、次のGELATOで使用するのはこの
フォルダに保存される[Case1.cgn]を使用する。
計算の実行が終わった時も必ず[計算結果]->[保存]で結果を保存すること。

GELATOによる仮想トレーサーの追跡計算
=========================================

ソルバの選択
---------------

iRICの起動画面から、[新しいプロジェクト]を選ぶと表示されるソルバの選択画面
( :numref:`02_select_GELATO` )で[GELATO]
を選択して[OK]を押す。

.. _02_select_GELATO:

.. figure:: images/02/select_GELATO.png
   :width: 100%

   : 「ソルバーGELATOの選択」

格子のインポート
------------------

:numref:`02_import_grid1` のようにオブジェクトブラウザーの[格子(データなし)]を右クリック
して、[インポート]をクリックする。

.. _02_import_grid1:

.. figure:: images/02/import_grid1.png
   :width: 100%

   : 「格子のインポート(1)」

ファイル選択ウィンドウが現れるので、先ほど[Nays2d+]の計算結果を保存したフォルダ
[Nays2d+Flow]の中の[Case1.cgn]を選ぶ( :numref:`02_import_grid2`)

.. _02_import_grid2:

.. figure:: images/02/import_grid2.png
   :width: 600pt

   : 「格子のインポート(2)」

お馴染みの :numref:`02_import6` の警告が表示されるが、構わず[はい]を押して進むと
格子のインポートが完了する。( :numref:`02_import7`)

.. _02_import6:

.. figure:: images/02/import6.png
   :width: 400pt

   : 「お馴染みの警告」

.. _02_import7:

.. figure:: images/02/import7.png
   :width: 100%

   : 「格子のインポート完了」

GELATOによるトレーサー追跡計算
-------------------------------

計算条件の設定
^^^^^^^^^^^^^^^

[計算条件]->[設定]で表示される[計算条件]ウィンドウで、

[基本設定]、[プライマリートレーサーの供給条件]、[通常トレーサーの時間設定]、[乱れの影響]
をそれぞれ、
:numref:`02_joken20` 、:numref:`02_joken21` 、:numref:`02_joken22`、 :numref:`02_joken23`
のようにパラメータを設定する。ここではまず、[乱れの影響]を考慮しない場合のトレーサー追跡を行う。

.. _02_joken20:

.. figure:: images/02/joken20.png
   :width: 600pt

   : 「GELATOの計算条件(1)」

.. _02_joken21:

.. figure:: images/02/joken21.png
   :width: 600pt

   : 「GELATOの計算条件(2)」

.. _02_joken22:

.. figure:: images/02/joken22.png
   :width: 600pt

   : 「GELATOの計算条件(3)」

.. _02_joken23:

.. figure:: images/02/joken23.png
   :width: 600pt

   : 「GELATOの計算条件(4)」

なお、:numref:`02_joken20` 中の[流れの計算結果を読み込むCGNSファイル]は前節[Nays2d+による流れの計算]
の結果を保存した[Nays2d+Flow]プロジェクトフォルダにある[Case1.cgn]を選択する。


計算の実行
^^^^^^^^^^^^^^

メインメニューから[計算]->[実行]を選択すると、「プロジェクトの保存がお勧めされる」ので、
ここは大人しく言うことを聞いて、新たにプロジェクトを保存しておく
( :numref:`02_save_project3`).

.. _02_save_project3:

.. figure:: images/02/save_project3.png
   :width: 400pt

   : 「GELATOプロジェクトの保存(1)」

[ファイルに保存(ipro)]か[プロジェクトとして保存]どちらでも良い。

.. _02_save_project4:

.. figure:: images/02/save_project4.png
   :width: 250pt

   : 「GELATOプロジェクトの保存(3)」


計算が始まるとお馴染みの :numref:`02_jikko20` この画面が登場し。終了すると、これまたお馴染みの
:numref:`02_jikko21` が表示されるので、[OK]を押す。

.. _02_jikko20:

.. figure:: images/02/jikko20.png
   :width: 100%

   : 「計算の実行(1)」

.. _02_jikko21:

.. figure:: images/02/jikko21.png
   :width: 250pt

   : 「計算の実行(2)」

計算結果の表示
^^^^^^^^^^^^^^^^^^^^

メインメニューから[計算結果]->[新しい可視化ウィンドウ(2D)を開く]を選択すると、計算結果が表示される。
(:numref:`02_kekka20` )

.. _02_kekka20:

.. figure:: images/02/kekka20.png
   :width: 100%

   : 「可視化ウィンドウ(2D)」


本章冒頭に示した実験の画像 :numref:`02_jikken` と向きが反対なので、:numref:`02_kekka20` に
矢印で示す(小さく分かりにくいが)90°回転のマークを2回クリックして180°回転させる
( :numref:`02_kekka21`).

.. _02_kekka21:

.. figure:: images/02/kekka21.png
   :width: 100%

   : 「可視化ウィンドウ(180°回転)」

時刻表示が小さくてメチャ見にくいので、オブジェクトブラウザーの[時刻]->[プロパティ]で
[時刻設定]を表示させて( :numref:`02_jikoku`) フォントサイズを適当に大きくする。

.. _02_jikoku:

.. figure:: images/02/jikoku.png
   :width: 100%

   : 「時刻表示設定」

:numref:`02_anime1` に示すように[時刻バーを戻し]、メインメニューから
[アニメーション]->[実行]でトレーサーの流動アニメーションが開始される
( :numref:`02_GELATO00`)

.. _02_anime1:

.. figure:: images/02/anime1.png
   :width: 100%

   : 「アニメーションの開始」

.. _02_GELATO00:

.. figure:: images/02/GELATO00.gif
   :width: 70%

   : [トレーサーのアニメーション(乱流拡散強度A=0)」

トレーサーは殆ど拡散せずに、線状に流れて行くのが分かる。

乱流拡散強度の違いの比較
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:numref:`02_A01` [計算条件]->[設定]の、[グループ][乱れの影響]で、
[ランダムウォークによるセル以下スケールの乱れ考慮]を[する]にして、[Aの値]を[1]にして
再度[計算を実行]、[計算結果のアニメーション表示を]すると、
:numref:`02_GELATO01` のようになる。

.. _02_A01:

.. figure:: images/02/A01.png
   :width: 600pt

   : 「ランダムウォークパラメータ(A=1)の設定」

.. _02_GELATO01:

.. figure:: images/02/GELATO01.gif
   :width: 70%

   : [トレーサーのアニメーション(乱流拡散強度A=1)」

同様に、[A=5]、[A=10]、[A=50]でランダムウォークをやってみると。。。

.. _02_GELATO05:

.. figure:: images/02/GELATO05.gif
   :width: 70%

   : [トレーサーのアニメーション(乱流拡散強度A=5)」

.. _02_GELATO10:

.. figure:: images/02/GELATO10.gif
   :width: 70%

   : [トレーサーのアニメーション(乱流拡散強度A=10)」

.. _02_GELATO50:

.. figure:: images/02/GELATO50.gif
   :width: 70%

   : [トレーサーのアニメーション(乱流拡散強度A=50)」

:numref:`02_jikken` の実験と比較すると、[A=10]位の感じであることが分かる。

トレーサーのクローン
^^^^^^^^^^^^^^^^^^^^^^^^^^

:numref:`02_clone01` [計算条件]->[設定]の、[グループ]
[トレーサーのクローニング(分割)と再結合]の設定で[クリーニング]を[する]、
[方法の選択]を[トレーサーが1個のセルだけ新規トレーサーを発生させる]、
[最大クローニング世代数]を[20]に設定すし、
[乱れの影響]は[A=10]として再度計算を実行し、結果を表示する( :numref:`02_clone10` )

.. _02_clone01:

.. figure:: images/02/clone01.png
   :width: 600pt

   : [トレーサークローンの設定」


.. _02_clone10:

.. figure:: images/02/clone10.gif
   :width: 70%

   : [トレーサークローン表示(最大20世代、A=10)」

トレーサーの拡散範囲は :numref:`02_jikken` の実験動画の緑色染料の拡散範囲に近くなっている。
ここで、オブジェクトブラウザーで、[粒子]->[スカラー]->[Generations]に☑マークを入れると、世代が表示される。
これをアニメーション表示すると、 :numref:`02_clone10_gen` のようになる。

.. _02_clone10_gen:

.. figure:: images/02/clone10_gen.gif
   :width: 70%

   : [トレーサークローン表示(最大20世代、A=10、世代色別表示)」

**基本事項(共通事項)** で述べたように、実質の重みは10世代目で :math:`W=0.00195`、20世代目だと
:math:`W=0.00000195` なので、 :numref:`02_clone10_gen` おける、緑・黄・赤等のトレーサー
濃度は中心部の青色系のトレーサーに比べ対数的に低いことになる。
格子内のトレーサー数に重みを乗じて、実質の濃度を見るには、

1．オブジェクトブラウザーで[スカラー]の☑マークを外す( :numref:`02_concent1`).

.. _02_concent1:

.. figure:: images/02/concent1.png
   :width: 350pt

   : [スカラー」の☑マークを外す

2．オブジェクトブラウザーで[スカラー(セル中心)][Weghted numbers of tracers]に☑マーク
を入れる(:numref:`02_concent2`).

.. _02_concent2:

.. figure:: images/02/concent2.png
   :width: 350pt

   : [Weighted numbers of tracers]に☑マークを入れる

3．[Weighted numbers of tracers]を右クリックして[プロパティ]を押す。

.. _02_concent3:

.. figure:: images/02/concent3.png
   :width: 350pt

   : [Weighted numbers of tracers]->[プロパティ]

4．[スカラー設定]ウィンドウで、以下のように設定して[設定]を押す。

.. _02_concent4:

.. figure:: images/02/concent4.png
   :width: 600pt

   : スカラー設定

:numref:`02_concent7` の[可視化ウィンドウ:2D]が表示されるので、
タイムバーをゼロに戻してメインメニューから[アニメーション]->[開始/停止]を
押すと、 :numref:`02_concent8` のアニメーションが開始される。

.. _02_concent7:

.. figure:: images/02/concent7.png
   :width: 100%

   : アニメーションの実行

.. _02_concent8:

.. figure:: images/02/concent8.gif
   :width: 70%

   : 重みを考慮したトレーサー濃度のアニメーション

:numref:`02_jikken` の実験動画の緑色染料の拡散状況に類似した拡散状況が再現された。

トレーサークローンを利用した流れの可視化
-----------------------------------------------

トレーサーのクローンツールを用いた流れの可視化の例を示す。


[Weighted numbers of tracers]の☑マークを外し、メインメニューの[計算条件]->[設定]を開く。
:numref:`02_settei1` および :numref:`02_settei2` のように条件を設定して保存する。
ここで、:numref:`02_settei2` の[トレーサーの無いセルはすべて発生させる] によって、可視化用の多数の
トレーサーを発生さる。

.. _02_settei1:

.. figure:: images/02/settei1.png
   :width: 600pt

   : 計算条件の設定(1)

.. _02_settei2:

.. figure:: images/02/settei2.png
   :width: 600pt

   : 計算条件の設定(2)

設定終了後、計算を実行し、 オブジェクトブラウザーの[粒子]と[スカラー]の☑マークを入れて、[Generations]の☑マークを外した後に
[アニメーション]->[開始/停止]で :numref:`02_kashika` のようにアニメーションが表示され、水路全体にトレーサーが
満遍なく配置された可視化となる。

.. _02_kashika:

.. figure:: images/02/kashika.gif
   :width: 70%

   : トレーサーを用いた可視化

魚の遊泳シミュレーション
---------------------------------

[計算条件]->[設定]で以下の設定を行う。

.. _02_fish1:

.. figure:: images/02/fish1.png
   :width: 600pt

   : 魚の条件設定(1)

.. _02_fish2:

.. figure:: images/02/fish2.png
   :width: 600pt

   : 魚の条件設定(2)

.. _02_fish3:

.. figure:: images/02/fish3.png
   :width: 600pt

   : 魚の条件設定(3)

.. _02_fish4:

.. figure:: images/02/fish4.png
   :width: 600pt

   : 魚の条件設定(4)

.. _02_fish5:

.. figure:: images/02/fish5.png
   :width: 600pt

   : 魚の条件設定(5)

この条件で、[計算]->[実行]を行った後に、オブジェクトブラウザーで[ポリゴン]->[Fish]->[Type]に☑マークを入れて
[アニメーション]->[開始/停止]を選択すると、:numref:`02_fish5` が再生される。

.. _02_fish6:

.. figure:: images/02/fish6.png
   :width: 350pt

   : アニメーションの設定

.. _02_fish7: 

.. figure:: images/02/fish.gif
   :width: 70%

   : 魚の遊泳アニメーション
  
NaysDw2による流木の追跡計算
===================================

本節では2次元流木追跡ソルバNayswd2により流木の追跡を行う。

ソルバの選択
---------------

iRICの起動画面から、[新しいプロジェクト]を選ぶと表示されるソルバの選択画面
( :numref:`02_select_Dw2` )で[NaysDw2シンプルな2次元流木追跡ツール]
を選択して[OK]を押す。

.. _02_select_Dw2:

.. figure:: images/02/select_Dw2.png
   :width: 600pt

   : 「ソルバーNaysDw2の選択」

格子のインポート
------------------

:numref:`02_import_grid3` のようにオブジェクトブラウザーの[格子(データなし)]を右クリック
して、[インポート]をクリックする。

.. _02_import_grid3:

.. figure:: images/02/import_grid3.png
   :width: 100%

   : 「格子のインポート(3)」

ファイル選択ウィンドウが現れるので、先ほど[Nays2d+]の計算結果を保存したフォルダ
[Nays2d+Flow]の中の[Case1.cgn]を選ぶ( :numref:`02_import_grid4`)

.. _02_import_grid4:

.. figure:: images/02/import_grid4.png
   :width: 600pt

   : 「格子のインポート(4)」

:numref:`02_import6` の警告が表示されるが、構わず[はい]を押して進むと
格子のインポートが完了する。( :numref:`02_import9`)

.. _02_import8:

.. figure:: images/02/import8.png
   :width: 400pt

   : 「警告」

.. _02_import9:

.. figure:: images/02/import9.png
   :width: 100%

   : 「格子のインポート完了」



計算条件の設定
--------------

[計算条件]->[設定]で以下の設定を行う。 
:numref:`02_dw1` [基本設定]の[流況計算結果を読み込むファイル名]を選ぶ

.. _02_dw1:

.. figure:: images/02/dw1.png
   :width: 600pt

   : [基本設定]->[計算結果を読み込むファイル名](1)
   
:numref:`02_dw2`  前節[Nays2d+]の計算結果の[Case1.cgn]を選ぶ

.. _02_dw2:

.. figure:: images/02/dw2.png
   :width: 600pt

   : [Cgnsファイルの指定]
   
[基本設定]の他のパラーメタは :numref:`02_dw3` のようにパラメータを設定する。

.. _02_dw3:

.. figure:: images/02/dw3.png
   :width: 600pt

   : [基本設定]

[流木の供給条件]パラーメタは :numref:`02_dw4` のようにパラメータを設定する。

.. _02_dw4:

.. figure:: images/02/dw4.png
   :width: 600pt

   : [流木の供給条件]

[流れおよび流木に関する]パラーメタは :numref:`02_dw5` のようにパラメータを設定する。


.. _02_dw5:

.. figure:: images/02/dw5.png
   :width: 600pt

   : [流れおよび流木に関するパラメーター]

[DEM(個別要素法)パラメーター]は :numref:`02_dw8` のようにパラメータを設定して、最後に
[OK]をクリックする。

.. _02_dw8:

.. figure:: images/02/dw8.png
   :width: 600pt

   : [DEM(個別要素法)パラメーター]


流木追跡計算の実行
------------------------

:numref:`02_dw6` メインメニューから[計算]->[実行]を選択。

.. _02_dw6:

.. figure:: images/02/dw6.png
   :width: 100%

   : [計算]->[実行]

:numref:`02_dw7` [プロジェクトを保存しますか?]と聞かれるので、[はい]を選んで保存する。

.. _02_dw7:

.. figure:: images/02/dw7.png
   :width: 400pt

   : [プロジェクトを保存しますか？]

[プロジェクトを保存方法の選択]が問われるので、ここでは
[プロジェクトとして保存]を選択して[OK]を押し、保存するフォルダ(空のフォルダ)を指定して、[フォルダの選択]をを押す

計算が開始されると、:numref:`02_dw10` の画面が表示され、終了すると
:numref:`02_dw11` が表示されるので[OK]をクリックする。 

.. _02_dw10:

.. figure:: images/02/dw10.png
   :width: 100%

   : [計算の実行]

.. _02_dw11:

.. figure:: images/02/dw11.png
   :width: 200pt

   : [計算の終了]


流木追跡計算結果の表示
------------------------

:numref:`02_dw12` メインメニューから[計算結果]->[新しい可視化ウィンドウ(2D)を開く]を選択

.. _02_dw12:

.. figure:: images/02/dw12.png
   :width: 100%

   : [可視化ウィンドウの表示]

:numref:`02_dw13` オブジェクトブラウザーで、[iRICZone][スカラー(格子点)][Res-Velocity]に☑マーク
を入れて、[右クリック]->[プロパティ]を選択

.. _02_dw13:

.. figure:: images/02/dw13.png
   :width: 100%

   : [スカラーの表示]


:numref:`02_dw14` [スカラー設定]ウィンドウを図のように設定して[OK]を押す。

.. _02_dw14:

.. figure:: images/02/dw14.png
   :width: 600pt

   : [スカラー設定]


:numref:`02_dw15` タイムバーをゼロに戻し、[アニメーション]->[開始/停止]を押す。

.. _02_dw15:

.. figure:: images/02/dw15.png
   :width: 100%

   : [アニメーションの開始]


:numref:`02_dw16` のようなアニメーションが表示される。

.. _02_dw16:

.. figure:: images/02/dw.gif
   :width: 70%

   : [流木追跡のアニメーション]

