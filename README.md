[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19729938.svg)](https://doi.org/10.5281/zenodo.19729938)

# cognitive-engineering-foundations
## 認知工学基底理論体系・公開原典アーカイブ

**現行監査反映日**：2026-10-07

本リポジトリは、がっちむち♂による**認知工学体系の基底理論・公開可能な原典・翻訳・境界宣言・適用論文**を管理するリポジトリである。

リポジトリ名 `cognitive-engineering-foundations` は、本体系を閉包位相Ψやトリニティ原理の個別仕様集ではなく、**認知工学を上位に置く基底理論体系**として位置づける現在の構造を表す。

基底言語・規定言語は**日本語**である。

```text
日本語原典を先に成立
→ 日本語で監査・改訂
→ 実務上必要な場合のみ英語等へ翻訳
```

英語その他の言語は、日本語正本から派生する下流言語層であり、独立した正本ではない。

翻訳・射影の権限階層は `TRANSLATION_POLICY.md` を正とする。

```text
J0 日本語正本
> T1 節対応全文翻訳
> T2 要約射影
> T3 解説射影
> W  作業翻訳
```

**制度語として `Translation` と呼ぶのはT1だけ**である。

現行番号付き正本群の英語部は全文翻訳ではなく、すべて **T2 / English Summary Projection** として明示する。

---

# 共通理論状態

現行番号付き正本群は、内容だけでなく**理論状態と記述粒度**を共通化している。

```text
時点付きProjection
→ 版内では明示的に固定
→ 現在条件では強く局所閉包してよい
→ 局所閉包を全体最終閉包へ昇格しない
→ 新観測・時間経過・実装結果で上流まで再開放可能
→ 旧版を消さず時点付き記録として保存
→ 各理論を自身にも自己適用
```

したがって、現行文書でいう「暫定」は弱さ・恣意性・判断不能を意味しない。

> **現在条件で強く成立するものは強く採用する。ただし、その強さを永久不可侵性へ変換しない。**

再開放対象は、モデル内の値だけではない。必要なら主体、対象、主体／対象の区別、対象同一性、関係、文脈、時間・空間・因果、目的・価値・評価規則、定義、前提、射程、観測方法、過去判断の意味、理論記述自身まで戻る。

詳細は [`PUBLICATION_POLICY.md`](PUBLICATION_POLICY.md) を正とする。

翻訳・要約・解説の上下関係、用語ロック、翻訳残差、STALE管理は [`TRANSLATION_POLICY.md`](TRANSLATION_POLICY.md) を正とする。

---

# 現行正本

root に置く番号付き文書は、現在の公開正本だけである。

| 順 | 文書 | 現行役割 |
|---|---|---|
| 00 | `00_認知工学とは何か_v0_4_ja_en.md` | Science / Engineering の分別、**「認知科学は成立しない」**という成立判定、認知工学の再定義、全学問の成立前段としての位置づけ、自己適用 |
| 01 | `01_情報工学における言語基底論_v0_4_ja_en.md` | 世界→認知→情報、**「情報科学は成立しない」**という成立判定、情報工学、意味構造保持、日本語基底、比較主張の証拠状態分離 |
| 02 | `02_Umami_Gap_v1_3_ja_en.md` | intelligence の語彙圧縮、欠落変数問題、C / Ψ / E分別、旧「知性Ψ」から現行「閉包位相Ψ」への更新理由 |
| 03 | `03_トリニティ原理_v1_2_ja_en.md` | **世界は3で閉じる／3が世界構築の最小構造**という三項最小性、X / R / Mを代表的Projectionとして分離、非対称循環・非対称再帰、SUSPEND |
| 04 | `04_閉包位相Ψ_v1_2_ja_en.md` | 閉包位相Ψの操作定義、旧「知性Ψ / Signature Phase」との理論史的分離、C/K/Ψ/E/A、自己同一性観測、因果同定の分離 |
| 05 | `05_神の領域原理（仮）_v1_3_ja_en.md` | 観測者依存の不可視位相差、神域帯、誤投影境界、G1〜G5、ブラックボックス尊重、封印、人類ゲームオーバー回避、生存・経済価値、自己適用 |
| 05A | `05A_原理とは何かと原理判別法_v0_2_ja_en.md` | 原理の定義、観測・パターン・モデル・機構との分別、**命題に数学の完全証明を当てて自己循環・再起・回帰するかを見る原理判別法**、補助監査、原理→原則、適用範囲付き暫定原理 |
| 06 | `06_トリニティ原理適用_論証監査_v0_5_ja_en.md` | 時点付き論証監査、命題型別の反論監査、停止状態の型分離、監査器自身の監査 |
| 07 | `07_トリニティ原理適用_ゲーム理論と均衡_v0_7_ja_en.md` | ゲーム世界・均衡を時点付き条件解として扱い、**ナッシュ均衡を単独逸脱・最適反応・相互固定点へ分解**し、X / R / Mで前提・関係・判定を可視化する適用 |
| 08 | `08_意識論_v0_1_ja_en.md` | 外界拘束、自己／非自己、認知・メタ認知、主観、自我を分離し、自我を時間安定した結果として扱う意識論 |
| 09 | `09_認知工学適用_情報熱力学とマクスウェルの悪魔_v0_1_ja_en.md` | 情報熱力学を、系境界・相関・測定・制御・「情報」ラベルの成立順序から監査し、情報の物理実体化を分離する認知工学適用 |
| 10 | `10_認知工学適用_進化論とダーウィンの過ち_v0_1_ja_en.md` | 自然選択を否定せず、進化の下流機構を生命の最上流原理へ昇格させる説明階層の越境を監査。「生きるために生きている」を境界文として定置 |
| 11 | `11_認知工学適用_相対性理論における時間と空間_v0_1_ja_en.md` | 相対論の観測・数理的成功と、時間・空間・時空の存在論を分離し、座標記述から世界本体への誤投影を監査 |
| 12 | `12_認知工学適用_量子重力問題の問題設定監査_v0_1_ja_en.md` | GRと量子論の非整合を前に、統合対象の同一性・語の役割・成功条件を再監査し、「統合問題そのもの」の成立条件を問う |

推奨読書順は **00 → 01 → 02 → 03 → 04 → 05 → 05A → 08 → 06 → 07 → 09 → 10 → 11 → 12** とする。06・07・09〜12は適用・監査論文として、基底理論群と意識論の後段に置く。

---

# 体系の最小関係

```text
認知工学
  ↓
認知による対象化・差異化・関係化・判断・再認知
  ↓
情報の成立
  ↓
情報工学
  ↓
言語基底
  ↓
日本語原典先行

旨味ギャップ
  = 欠落変数を見えなくする語彙圧縮の導入
  = 現行変数集合自体も再分別可能

トリニティ原理
  = 世界は3で閉じる
  = 世界を構築する最小構造は3
  = 三項性そのものが原理
  = X_t / R_t / M_t は代表的操作Projection
  = 三項閉包は非対称循環・非対称再帰する
  = 未閉包では SUSPEND
  = 局所閉包を全体最終閉包へ昇格しない

閉包位相Ψ
  = 特定時点・対象・観測条件で外部へ残る安定出力相
  = 「安定」は永久不変を意味しない
  = ΨとΨの現在記述を非同一として扱う

神の領域原理（仮）
  = 観測者依存の不可視位相差を前提にする
  = 認知後世界像を認知以前の世界本体へ誤投影しない
  = ブラックボックス尊重・G1〜G5・封印・可逆性を中核に持つ
  = 人類ゲームオーバー回避を第一安全目的として扱う
  = 安全境界の内側で現実の生存・経済価値へ接続する
  = 原理自身、境界語彙、総暫定性を自己例外化しない

原理とは何か／原理判別法
  = 原理質問「何がこれを成立させているのか」
  = 命題Pに数学の完全証明を当てる
  = 証明を完全展開し、P自身または機能同型構造へ自己循環・再起・回帰するかを見る
  = 再帰するなら原理候補、別上位構造で閉じるなら定理・規則・派生命題等へ再分類
  = 除去・同型再導入試験は後段の補助監査
  = 最小性・同型性・生成性・横断性・失敗検出性・適用範囲を再監査
  = 原理→原則の順序を保持
  = 原理も適用範囲付き暫定Projectionとして再開放する

意識論
  = 外界拘束の下で自己 / 非自己を分別する
  = 認知とメタ認知の再帰的関係として意識を扱う
  = 主観を一人称的制御原点の擬似固定点として扱う
  = 自我を時間軸上で自己同一性として安定した結果とする
  = 閉包位相Ψを意識・自我の証明へ昇格しない
  = 構造記述と起動因果を分離する

認知工学適用監査
  = 既存科学の計算結果を直接否定するのではなく、問い・対象・系境界・座標・因果・存在論への昇格を監査する
  = 情報熱力学：情報ラベルと物理状態・相関を分離
  = 進化論：進化機構と生命の最上流原理を分離
  = 相対論：観測座標と時間・空間の存在論を分離
  = 量子重力：統合解探索の前に統合問題そのものの成立条件を監査する
```

この関係図自体も現在の公開Projectionであり、世界本体の最終階層図ではない。

---

# 現行名称

正式名称・表記は `PUBLICATION_POLICY.md` を正とする。

- **神の領域原理（仮）**
  - 略称：**神域原理（仮）**
- **トリニティ原理**
- **閉包位相Ψ**
- **意識論**
- **Human Decision-making System（仮）**
  - 和名：**人間意思決定理論（仮）**
  - 略称：**HDS**

`（仮）` を付すのは、神の領域原理（仮）／神域原理（仮）と HDS のみである。

---

# HDS公開境界

HDSについて本リポジトリで公開する情報は、原則として名称のみである。

```text
Human Decision-making System（仮）
人間意思決定理論（仮）
HDS
```

HDSの内部構造、相、層、ループ、判断機構、評価設計、運用手順、実装、再現可能なレシピ等は現行公開範囲に含めない。

別公開リポジトリに残る旧HDSデモ・旧層構造・旧実装は **Legacy Public Projection** として扱い、現行HDS仕様または現行公開境界の拡張とはみなさない。

本リポジトリの他理論は、**HDS内部を公開するのではなく、理論の成熟状態・認識精度・暫定性・時間軸・自己適用の粒度を同水準へ揃える。**

---

# 版履歴と archive

`archive/` は旧版・旧適用例・旧ツールを保存する履歴領域である。

本リポジトリは旧称 `closure-phase-specs` から `cognitive-engineering-foundations` へ改称された。archive 内には旧リポジトリ名を含む当時の文書が残り得るが、それらは歴史状態として保持する。

archive 内の文書には、現行方針と異なる、

- 英語先行レイアウト
- 旧名称
- 旧HDS公開記述
- 過去のTCP固定表現
- 現在より静的な暫定性
- 過去の理論粒度

が残り得る。

これらは削除・改竄せず履歴として保存するが、**現行正本として参照してはならない**。

---

# 参照文献

`REFERENCES.md` は座標合わせ用の参考情報であり、本理論群の正しさを権威によって証明するものではない。

---

# License

文書本文は、特記がない限り `LICENSE` に従う。

---

# English Summary Projection

## cognitive-engineering-foundations — Cognitive Engineering Foundations

**Translation class**: T2 / English Summary Projection  
**Source authority**: Japanese Canonical Original (J0)  
**Translation status**: CURRENT  
**Authority**: Non-authoritative and non-exhaustive  

This repository manages the publicly disclosed foundational theories, originals, translations, boundaries, and application papers of a Cognitive Engineering theoretical system authored by **がっちむち♂**.

The repository was renamed from `closure-phase-specs` to `cognitive-engineering-foundations` to reflect its current scope: the repository is no longer organized around one closure-phase specification family, but around Cognitive Engineering as the upstream theoretical field.

Japanese is the sole authoritative language. Downstream language products follow `TRANSLATION_POLICY.md`: J0 Japanese Canonical Original > T1 Aligned Full Translation > T2 Summary Projection > T3 Explanatory Projection > W Working Translation.

All current documents share a common theory state:

```text
Time- and version-bounded Projection
→ Explicit fixation inside the version for auditability
→ Strong local closure when current conditions justify it
→ No promotion of local closure into global finality
→ Reopen upstream assumptions when material new observation requires it
→ Preserve older versions as historical records
→ Apply each theory to itself
```

“Provisional” does not mean weak or arbitrary. Strong current conclusions remain strong while being denied permanent immunity from future observation.

### Current canonical reading order

1. `00_認知工学とは何か_v0_4_ja_en.md`
2. `01_情報工学における言語基底論_v0_4_ja_en.md`
3. `02_Umami_Gap_v1_3_ja_en.md`
4. `03_トリニティ原理_v1_2_ja_en.md`
5. `04_閉包位相Ψ_v1_2_ja_en.md`
6. `05_神の領域原理（仮）_v1_3_ja_en.md`
7. `05A_原理とは何かと原理判別法_v0_2_ja_en.md`
8. `08_意識論_v0_1_ja_en.md`
9. `06_トリニティ原理適用_論証監査_v0_5_ja_en.md`
10. `07_トリニティ原理適用_ゲーム理論と均衡_v0_7_ja_en.md`
11. `09_認知工学適用_情報熱力学とマクスウェルの悪魔_v0_1_ja_en.md`
12. `10_認知工学適用_進化論とダーウィンの過ち_v0_1_ja_en.md`
13. `11_認知工学適用_相対性理論における時間と空間_v0_1_ja_en.md`
14. `12_認知工学適用_量子重力問題の問題設定監査_v0_1_ja_en.md`

Only the following HDS names are public:

```text
Human Decision-making System（仮）
人間意思決定理論（仮）
HDS
```

The other public theories are aligned to the same maturity of provisionality, temporal reopening, and self-application without disclosing HDS internals.
