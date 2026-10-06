[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19729938.svg)](https://doi.org/10.5281/zenodo.19729938)

# cognitive-engineering-foundations
## 認知工学基底理論体系・公開原典アーカイブ

本リポジトリは、がっちむち♂による**認知工学体系の基底理論・公開可能な原典・翻訳・境界宣言・適用論文**を管理するリポジトリである。

リポジトリ名 `cognitive-engineering-foundations` は、本体系を閉包位相Ψやトリニティ原理の個別仕様集ではなく、**認知工学を上位に置く基底理論体系**として位置づける現在の構造を表す。

基底言語・規定言語は**日本語**である。

```text
日本語原典を先に成立
→ 日本語で監査・改訂
→ 実務上必要な場合のみ英語等へ翻訳
```

英語その他の言語は日本語原典の後段翻訳であり、独立した正本ではない。

---

# 共通理論状態

現行00〜07は、内容だけでなく**理論状態と記述粒度**を共通化している。

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

---

# 現行正本

root に置く番号付き文書は、現在の公開正本だけである。

| 順 | 文書 | 現行役割 |
|---|---|---|
| 00 | `00_認知工学とは何か_v0_3_ja_en.md` | Science / Engineering の分別、認知工学の再定義、全学問の成立前段としての位置づけ、認知工学自身への自己適用 |
| 01 | `01_情報工学における言語基底論_v0_3_ja_en.md` | 世界→認知→情報、情報科学批判、情報工学、意味構造保持、日本語基底、評価軸まで含む再開放 |
| 02 | `02_Umami_Gap_v1_0_ja_en.md` | intelligence の語彙圧縮、欠落変数問題、C / Ψ / Eを現行分別として扱う導入 |
| 03 | `03_トリニティ原理_v1_0_ja_en.md` | X / R / Mによる時点付き局所閉包、原理と現在記述の分離、SUSPEND、全体開放 |
| 04 | `04_閉包位相Ψ_v0_9_ja_en.md` | 時点・対象・観測条件付きの安定出力相、ΨとΨ記述の分離、安定性自体の再監査 |
| 05 | `05_神の領域原理（仮）_v1_0_ja_en.md` | 認知後世界像の誤投影防止、局所的強採用／全体開放、原理自身への完全自己適用 |
| 06 | `06_トリニティ原理適用_論証監査_v0_3_ja_en.md` | 時点付き論証監査、PASS / SUSPEND / FAILの局所判定化、監査器自身の監査 |
| 07 | `07_トリニティ原理適用_ゲーム理論と均衡_v0_4_ja_en.md` | ゲーム世界・均衡を時点付き条件解として扱い、プレイヤー・利得・ゲーム境界まで再構成可能にする適用 |

推奨読書順は 00 → 07 とする。

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
  = 認知後記述を X_t / R_t / M_t で局所閉包
  = 未閉包では SUSPEND
  = 原理と現在の三項記述を非同一として扱う
  = 局所閉包を全体最終閉包へ昇格しない

閉包位相Ψ
  = 特定時点・対象・観測条件で外部へ残る安定出力相
  = 「安定」は永久不変を意味しない
  = ΨとΨの現在記述を非同一として扱う

神の領域原理（仮）
  = 認知後世界像を認知以前の世界本体へ誤投影しない境界
  = 局所モデルの強い使用を妨げない
  = 原理自身、境界語彙、総暫定性を自己例外化しない
```

この関係図自体も現在の公開Projectionであり、世界本体の最終階層図ではない。

---

# 現行名称

正式名称・表記は `PUBLICATION_POLICY.md` を正とする。

- **神の領域原理（仮）**
  - 略称：**神域原理（仮）**
- **トリニティ原理**
- **閉包位相Ψ**
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

# English Translation

## cognitive-engineering-foundations — Cognitive Engineering Foundations

This repository manages the publicly disclosed foundational theories, originals, translations, boundaries, and application papers of a Cognitive Engineering theoretical system authored by **がっちむち♂**.

The repository was renamed from `closure-phase-specs` to `cognitive-engineering-foundations` to reflect its current scope: the repository is no longer organized around one closure-phase specification family, but around Cognitive Engineering as the upstream theoretical field.

Japanese is the base and normative language.

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

1. `00_認知工学とは何か_v0_3_ja_en.md`
2. `01_情報工学における言語基底論_v0_3_ja_en.md`
3. `02_Umami_Gap_v1_0_ja_en.md`
4. `03_トリニティ原理_v1_0_ja_en.md`
5. `04_閉包位相Ψ_v0_9_ja_en.md`
6. `05_神の領域原理（仮）_v1_0_ja_en.md`
7. `06_トリニティ原理適用_論証監査_v0_3_ja_en.md`
8. `07_トリニティ原理適用_ゲーム理論と均衡_v0_4_ja_en.md`

Only the following HDS names are public:

```text
Human Decision-making System（仮）
人間意思決定理論（仮）
HDS
```

The other public theories are aligned to the same maturity of provisionality, temporal reopening, and self-application without disclosing HDS internals.
